from django.conf.urls import url
from taobao import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^classify/(\d+)/(\d+)/$',views.classify),
    url(r'^login$', views.login_view,name='login'),
    url(r'^logout', views.logout_view),
    url(r'^register$', views.register_view,name='register'),
    url(r'^goods/(?P<goods_id>\d+$)',views.goodsDetail,name='goodsDetail'),
    url(r'^cart/$',views.cart),
    url(r'^search_name/$',views.search_name),
    url(r'^additem/(\d+)/(\d+)/$',views.add_to_cart,name='additem-url'),
    url(r'^removeitem/(\d+)/$',views.remove_from_cart,name='removeitem-url'),
]

