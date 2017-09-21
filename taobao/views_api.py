from taobao.models import goods

from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage

from django.views.decorators.csrf import  csrf_exempt
import io

#验证码制作，str存session中，图片返回。
def verifyCode(req):
    import random
    from PIL import Image, ImageDraw, ImageFont, ImageFilter

    _letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
    _upper_cases = _letter_cases.upper()  # 大写字母
    _numbers = ''.join(map(str, range(3, 10)))  # 数字
    init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

    def create_validate_code(size=(120, 30),
                             chars=init_chars,
                             img_type="GIF",
                             mode="RGB",
                             bg_color=(255, 255, 255),
                             fg_color=(0, 0, 255),
                             font_size=30,
                             font_type="Arial.ttf",
                             length=4,
                             draw_lines=True,
                             n_line=(1, 4),
                             draw_points=True,
                             point_chance=2):
        """
        @todo: 生成验证码图片
        @param size: 图片的大小，格式（宽，高），默认为(120, 30)
        @param chars: 允许的字符集合，格式字符串
        @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
        @param mode: 图片模式，默认为RGB
        @param bg_color: 背景颜色，默认为白色
        @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
        @param font_size: 验证码字体大小
        @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
        @param length: 验证码字符个数
        @param draw_lines: 是否划干扰线
        @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
        @param draw_points: 是否画干扰点
        @param point_chance: 干扰点出现的概率，大小范围[0, 100]
        @return: [0]: PIL Image实例
        @return: [1]: 验证码图片中的字符串
        """

        width, height = size  # 宽高
        # 创建图形
        img = Image.new(mode, size, bg_color)
        draw = ImageDraw.Draw(img)  # 创建画笔

        def get_chars():
            """生成给定长度的字符串，返回列表格式"""
            return random.sample(chars, length)

        def create_lines():
            """绘制干扰线"""
            line_num = random.randint(*n_line)  # 干扰线条数

            for i in range(line_num):
                # 起始点
                begin = (random.randint(0, size[0]), random.randint(0, size[1]))
                # 结束点
                end = (random.randint(0, size[0]), random.randint(0, size[1]))
                draw.line([begin, end], fill=(0, 0, 0))

        def create_points():
            """绘制干扰点"""
            chance = min(100, max(0, int(point_chance)))  # 大小限制在[0, 100]

            for w in range(width):
                for h in range(height):
                    tmp = random.randint(0, 100)
                    if tmp > 100 - chance:
                        draw.point((w, h), fill=(0, 0, 0))

        def create_strs():
            """绘制验证码字符"""
            c_chars = get_chars()
            strs = ' %s ' % ' '.join(c_chars)  # 每个字符前后以空格隔开

            # font = ImageFont.truetype(font_type, font_size)
            font = ImageFont.truetype('E:\workspace\PycharmProjects\shopping-website\Arial.ttf', random.randint(21, 25))

            draw.text((random.randint(0, 10), random.randint(0, 5)),
                      strs, font=font, fill=fg_color)

            return ''.join(c_chars)

        if draw_lines:
            create_lines()
        if draw_points:
            create_points()
        strs = create_strs()
        del draw

        # 图形扭曲参数
        params = [1 - float(random.randint(1, 2)) / 100, 0, 0, 0, 1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500, 0.001, float(random.randint(1, 2)) / 500]
        img = img.transform(size, Image.PERSPECTIVE, params)  # 创建扭曲
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）

        return img,strs

    res = create_validate_code()
    strs , img = res[1],res[0]
    req.session['verifycode'] = strs
    buf = io.BytesIO()
    img.save(buf, 'png')
    # img.save('code.jpg', 'jpeg')
    # print(strs)
    return HttpResponse(buf.getvalue(), 'image/png')



#判断用户是否登录
def user_session(req):
    context = {'status': 200}
    if 'username' in req.session:
        username = req.session['username']
        context['isLogin'] = True
        context['username'] = username
    else:
        context['isLogin'] = False
        context['username'] = ''
    return JsonResponse(context)

#分类展示
@csrf_exempt
def classify(req):
    context ={'status':200}
    type = req.POST.get('type','')
    page = req.POST.get('page','')

    context['type'] , context['page'] = type ,page
    if type == '0':
        goods_list = goods.objects.order_by('sales_Volume').all()
    else:
        goods_list = goods.objects.all().filter(category = int(type)).order_by('sales_Volume').all()

    if goods_list == None:
        return JsonResponse({'status':10021,'message':'parameter error'})

    paginator = Paginator(goods_list,8)
    try:
        goodss = paginator.page(int(page))
    except PageNotAnInteger:
        goodss = paginator.page(1)
    except EmptyPage:
        goodss = paginator.page(paginator.num_pages)

    context['queryNum'],context['hasPrevios'],context['hasNext'] = len(goodss),goodss.has_previous(),goodss.has_next()
    context['endIndex'] = paginator.num_pages
    data = []

    if goodss:
        for i in goodss:
            good = {}
            good['goods_id'] = i.goods_id
            good['goods_name'] = i.goods_name
            good['goods_price'] = i.goods_price
            good['goods_stock'] = i.goods_Stock
            good['sales_volume'] = i.sales_Volume
            good['goods_introduce'] = i.goods_introduce
            data.append(good)
        context.update({'data':data})
        return JsonResponse(context)
    else:
        return  JsonResponse({'status':10022,'message':'query goods isempty'})


# return render(req,'classify.html',context)
# category = models.IntegerField('分类',default=0)
#     goods_id = models.CharField('商品ID',max_length=10)
#     goods_name = models.CharField('商品名',max_length=100,default='')
#     goods_price = models.DecimalField('商品价格',max_digits=10,decimal_places=2)
#     goods_Stock = models.IntegerField('商品库存',default=100)
#     sales_Volume = models.IntegerField('销量',default=0)
#     goods_introduce = models.CharField('商品简介',max_length=250,default='')