# A. Файловый шифратор

print(ord('T'))

# def coder(stri, key):
#     res = ''
#     for a in stri:
#         p = ord(a) - ord('a')
#         q = ord(a) - ord('A')
#         if 0 <= p < len(key):
#             res = res + key[p]
#         elif 0 <= q < len(key):
#             res = res + key[q].upper()
#         else:
#             res = res + a
#     return res
# def start(finp, fout):
#     with open(finp, "r") as fi, open(fout, "w") as fo:
#         key = fi.readline()
#         while True:
#             text = fi.readline()
#             if len(text) == 0:
#                 break
#             fo.write(coder(text, key))
# start("input.txt", "output.txt")

# B. Кофеманы

def intersectionCoffeehouse(arr):
    arrName, arrCoffee, resArr = [], [], []
    for el in arr:
        els = el.split()
        arrName.append(els[1])
        arrCoffee.append(els[0])
    allCoffee=set(arrCoffee)
    countCoffee = len(allCoffee)
    allName=set(arrName)
    for name in allName:
        subArr, subCoffee=[], []
        for coffee in allCoffee:
            str = coffee+' '+name
            addedStr=str+'\n'
            if (str) in arr or addedStr in arr:
                subArr.append(str)
        if len(set(subArr)) == countCoffee:
            resArr.append(name)
    sortedArr=sorted(resArr)
    return (' '.join(sortedArr) if len(sortedArr) >= 1 else "No")
def start(fileInput, fileOutput):
    arr=[]
    with open(fileInput, "r") as fi, open(fileOutput, "w") as fo:
        while True:
            text = fi.readline()
            if len(text) == 0:
                break
            arr.append(text)
        fo.write(intersectionCoffeehouse(arr))
start("input.txt", "output.txt")

# C. Объединение кофеен

# моё решение почти рабочее, падает на 16ом тесте с ошибкой уточню у чалого на вебинаре(не уточнил :(((((
# from collections import defaultdict
# def difference(firstList, secondList):
#     return list(set(firstList) - set(secondList))
# def intersectionCoffeehouse(arr):
#     if len(arr) == 0:
#         return '0'
#     arr=set(arr)
#     _dict=defaultdict()
#     for el in arr:
#         text = el.split()
#         if text[1].endswith('\n'):
#             text[1]=text[1][:-2]
#         if not (text[0] in _dict.keys()):
#             _dict[text[0]] = [text[1]]
#         else:
#             _dict[text[0]].append(text[1])
#     interString=[]
#     for key1 in _dict.keys():
#         for key2 in _dict.keys():
#             if key1 == key2:
#                 continue
#             elif not (key2+key1 in interString):
#                 if len(_dict[key1])/len(difference(_dict[key2], _dict[key1])+_dict[key1]) < 0.75 and len(_dict[key2])/len(difference(_dict[key1], _dict[key2])+_dict[key2]) < 0.75:
#                     interString.append(key1+key2)
#     return str(len(interString))
# def start(fileInput, fileOutput):
#     arr=[]
#     with open(fileInput, "r") as fi, open(fileOutput, "w") as fo:
#         while True:
#             text = fi.readline()
#             if len(text) == 0:
#                 break
#             arr.append(text)
#         fo.write(intersectionCoffeehouse(arr))
# start("input.txt", "output.txt")

# правильное решение
# f = open('input.txt','r')
# f1 = open('output.txt','w')
# def union(c1,c2,visitors):
#     s1 = s2 = 0
#     for k in visitors.keys():
#         if c1 in visitors[k] and not(c2 in visitors[k]):
#             s1 +=1
#         elif c2 in visitors[k] and not(c1 in visitors[k]):
#             s2+=1
#     return s1,s2
# sum = 0
# cafes = []
# cafesss = {}
# people = {}
# all = []
# for line in f:
#     m = []
#     a,b = line.split()
#     m.append(a);m.append(b)
#     if not(m in all):
#         all.append(m)
#     if not(b in people):
#         people[b]=[]
#         people[b].append(a)
#     else:
#         people[b].append(a)
#     if not (a in cafes):
#         cafesss[a] = 0
#         cafes.append(a)
# i=0
# for k in cafesss.keys():
#     while i<len(all):
#         if k == all[i][0]:
#             cafesss[k]+=1
#         i+=1
#     i=0
# for i in range(len(cafes)-1):
#     for j in range(i+1,len(cafes)):
#         s1, s2 = union(cafes[i],cafes[j],people)
#         if s2+cafesss[cafes[i]]>cafesss[cafes[i]]+(cafesss[cafes[i]]/4) and s1+cafesss[cafes[j]]>cafesss[cafes[j]]+(cafesss[cafes[j]]/4):
#             sum+=1
# f1.write(str(sum))

# D. Гости
# f = open('input.txt','r')
# f1 = open('output.txt','w')
# line= f.readline()
# l = []
# a=''
# for i in range(len(line)):
#     if line[i] == ' ':
#         if a!= '':
#             l.append(int(a))
#         a = ''
#     else:
#         a = a+line[i]
# l.append(int(a))
# flats = l[1]-l[0]+1
# i=1
# error = 0
# while l[1]>=flats*i:
#     if l[1] == flats*i:
#         error=1
#     i+=1
# podezd = 0
# k = 0
# while k <max(l):
#     podezd+=1
#     k+=flats
# if error==0 or podezd==1:
#     f1.write("Error")
# else:
#     l.sort()
#     visitors = {}
#     i = 0
#     m = -1
#     k = 1
#     while k<=podezd:
#         while i < len(l):
#             if (k*flats+1)-flats<=l[i]<=k*flats:
#                 if not k in visitors.keys():
#                     visitors[k] = 0
#                     visitors[k] += 1
#                     m=i
#                     i += 1
#                 else:
#                     visitors[k] += 1
#                     m = i
#                     i += 1
#             else:
#                 break
#         k+=1
#         i = m+1
#     most_visited = []
#     for k in visitors.keys():
#         if visitors[k] == max(visitors.values()):
#             most_visited.append(str(k))
#     s = ' '.join(most_visited)
#     f1.write(s)

