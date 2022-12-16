# B. Идентификаторы

# 1-строчное решение(не проходит по времени в полтора раза, не могу понять Чалого, на хера тайм лимиты такие устанавливать
# для студентов не технических направлений)

# print(' '.join(filter(lambda s: s.isalpha() is True, input().split())))
# рабочее решение

# data=input().split()
# c = 0
# for elem in data:
#     if elem.isalpha() and c != 0:
#         print(' '+elem, end='')
#     elif elem.isalpha():
#         print(elem, end='')
#         c += 1

# D. Самый длинный общий префикс

# count = int(input())
# prefix = input()
# for i in range(count-1):
#     curStr=input();
#     if len(prefix) > len(curStr):
#         prefix, curStr = curStr, prefix
#     for j in range(len(prefix)-1, -1, -1):
#         print(j)
#         if prefix[j] != curStr[j]:
#             prefix = prefix[:-1]
# print(prefix)

# A. Поворот на Ауру

#
# k,n=map(int, input().split())
# cars=list(map(int, input().split()))
# resCar=0
# for el in cars:
#     resCar += el - k
#     if (resCar < 0):
#         resCar = 0
# print(resCar)

# C. Лампочка на складе

# тоже правильное но не проходящее по времени

# k, n = map(int, input().split())
# time = [0 for _ in range(480)]
# t = [[map(int, input().split())] for _ in range(k)]
# for i in t:
#     for j in range(i[0], i[1] + 1):
#         if (time[j]==0):
#             time[j] += 1
# a=time.count(0)
# if n-a <= 0 or n == 0:
#     print(0)
# else:
#     print(n-a)

# k, n = map(int, input().split())
# t=[[int(i) for i in input().split()] for _ in range(k)]
# t = sorted(t, key=lambda x: x[0])
# res = []
# left, right = t[0][0], t[0][1]
# for i in t:
#     if i[0] > right:
#         res.append((left, right))
#         left, right = i[0], max(right, i[1])
#     else:
#         right = max(right, i[1])
# res.append((left, right))
# a=480-sum(x2 - x1 + 1 for x1, x2 in res)
# if (n==0):
#     print(0)
# elif (n-a<0):
#     print(0)
# else:
#     print(n-a)

# E. Машинное зрение

# s1, s2, s3, resStr = input(), input(), input(), ''
# for i in range(0, len(s1)-1, 4):
#     if(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]=='|' and s2[i+1]=='_' and s2[i+2]=='|' and s3[i]=='|' and s3[i+1]=='_' and s3[i+2]=='|'):
#         resStr += '8'
#     if(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]=='|' and s2[i+1]==' ' and s2[i+2]=='|' and s3[i]=='|' and s3[i+1]=='_' and s3[i+2]=='|'):
#         resStr += '0'
#     elif(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]=='|' and s2[i+1]=='_' and s2[i+2]=='|' and s3[i]==' ' and s3[i+1]=='_' and s3[i+2]=='|'):
#         resStr += '9'
#     elif(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]=='|' and s2[i+1]=='_' and s2[i+2]==' ' and s3[i]=='|' and s3[i+1]=='_' and s3[i+2]=='|'):
#         resStr += '6'
#     elif(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]==' ' and s2[i+1]=='_' and s2[i+2]=='|' and s3[i]==' ' and s3[i+1]=='_' and s3[i+2]=='|'):
#         resStr += '3'
#     elif(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]=='|' and s2[i+1]=='_' and s2[i+2]==' ' and s3[i]==' ' and s3[i+1]=='_' and s3[i+2]=='|'):
#         resStr += '5'
#     elif(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]==' ' and s2[i+1]=='_' and s2[i+2]=='|' and s3[i]=='|' and s3[i+1]=='_' and s3[i+2]==' '):
#         resStr += '2'
#     elif(s1[i]==' ' and s1[i+1]==' ' and s1[i+2]==' ' and s2[i]=='|' and s2[i+1]=='_' and s2[i+2]=='|' and s3[i]==' ' and s3[i+1]==' ' and s3[i+2]=='|'):
#         resStr += '4'
#     elif(s1[i]==' ' and s1[i+1]=='_' and s1[i+2]==' ' and s2[i]==' ' and s2[i+1]==' ' and s2[i+2]=='|' and s3[i]==' ' and s3[i+1]==' ' and s3[i+2]=='|'):
#         resStr += '7'
#     elif(s1[i]==' ' and s1[i+1]==' ' and s1[i+2]==' ' and s2[i]==' ' and s2[i+1]==' ' and s2[i+2]=='|' and s3[i]==' ' and s3[i+1]==' ' and s3[i+2]=='|'):
#         resStr += '1'
# print(int(resStr))