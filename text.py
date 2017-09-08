import math

# a = input()
# list1 = a.strip(' ').split(' ')

#python2
# list1 = map(int,list1)
# python3
# list1 = list(map(int,list1))

# i, j  = int(list1[0]) ,int(list1[1])
# sum = i
# for ii in range(1,j):
#     sum  = sum + math.sqrt(i)
#     i = math.sqrt(i)
#
# print('{0:.2f}'.format(sum,'.2e'))
#
# print(list1)
from operator import itemgetter
import sys
n = int(input())
List = []
for i in range(0,n):
    index = input()
    index = index.strip(' ').split(' ')
    index = list(map(int, index))
    List.append(index)

List = sorted(List,key = itemgetter(0,1))

List.reverse()

res ,maxRow,indMaxRow ,indexCol= [] ,0 , 0 ,List[0][0]

for i in List:
    if i[0] == indexCol:
        if i[1] >= indMaxRow:
            res.append(i)
        if i[1] > maxRow:
            maxRow = i[1]
    else:
        indexCol = i[0]
        indMaxRow = maxRow
        if i[1] >= indMaxRow:
            res.append(i)
        if i[1] > maxRow:
            maxRow = i[1]
res = sorted(res,key = itemgetter(0,1))
for i in res:
    sys.stdout.write('{} {}\n'.format(i[0],i[1]))


