import  re

str ="javascript:Comment.newLoadPaginationOfComment({type:'all',currentPage:1,totalCount:'47',placeId:'100640',productId:'',placeIdType:'PLACE',isPicture:'',isBest:'',isPOI:'Y',isELong:'N'});"
a = re.findall(r"totalCount:'(.*?)',",str)

for i in a:
    print(i)