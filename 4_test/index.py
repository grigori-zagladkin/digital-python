# 1 задание

# x = (4, 2, 9)
# s=(4,2,9)
# s=(0, 100, 100)
# s=(4, 2)
# s=(4, 2, 9, 0) - true
# s=(8, 3) - true
# s=(4, 1, 2)
# s=(10, 1, 1) - true
# if s > x:
#     print("Bigger!")

# 2 задание

# stuff = dict()
# stuff['orange'] = 'orange'
# stuff['apple'] = 'green'
# print(stuff['banana']) - error

# 3 задание

# a={}
# # b=<>
# c=[]
# d=dict()
# e=set()
# f=()
# g={}
# # h=(,)
# print(a,c, d,e,f,g)

# 4 задание

# ifile = open('myfile.txt')
# while ifile:
#     l = ifile.readline()
#     print(l)
# while (getline(ifile, line)):
#     l = getline(ifile, line)
# for line in ifile:
#     print(line) - true

# 5 задание

# s = input("Введите строку:")
# words = dict()
# m = 0
# for w in s.split():
#     c = words.get(w, 0)
#     if c >= m:
#         m = c + 1
#     words[w] = c + 1
# print(m)

# 6 задание

# a=(3,2,1)
# b={3: 'c', 2: 'b', 1: 'a'}
# # a.sort()
# # b.sort()
# print(a.count())
# print(b.count(2))

# 10 задание

# fhand = open("myfile.txt")
# x = 0
# for line in fhand:
#     x = x + 1
# print(x) - count line

# 11 задание

# key = "A"
# counts = {1: "c", 2: "g"}
# if key in counts:
#     counts[key] = counts[key] + 1
# else:
#     counts[key] = 1
# print(counts) - {1: 'c', 2: 'g', 'A': 1}
# counts[key] = (key in counts) + 1 - true
# print(counts)

# 12 задание

# primes1 = {2, 3, 5, 7}
# primes2 = {3, 7, 11, 17}
# print(primes1.union(primes2))
# print(primes1.difference(primes2))
# print(primes1.intersection(primes2))
# print(primes1.symmetric_difference(primes2)) - true

# 13 - задание

# 14 - задание

# primes = {2, 3, 5, 7}
# pd = {0: primes, 1: {11, 13, 17, 19}}
# pd[2] = pd[0].union(pd[1]).difference({13, 17})
# # pd[primes] = 'Primes'
# # pd[primes] += ' - New Collection'
# pd.update({13: {13}})
# for k, v in pd.items():
#     if 13 in v:
#         del pd[k]

# 15 задание

# crypt = {"a":"c", "t":"g", "g":"a", "c":"t"}
# s = "acatgc"
# r = ""
# for i in range(len(s)):
#     for k, v in crypt.items():
#         if v == s[i]:
#             r += k
# print(r) - gagcta