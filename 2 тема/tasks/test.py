# x=1986
# def a(y):
#     global x
#     x=x*y
#     return y
# def b(x, y):
#     x=3/x+2*y
#     return x
# def c(y):
#     return 16/x*y
# def d(y):
#     y = 3.14*x+16/y
#     return y
# print(a(2))
# print(b(2, 8))
# print(c(3))
# print(d(4))

# import math

# def sphere_volume(radius):
#     """Возвращает объем шара, если известен его радиус."""
#     print(math.pi*4*radius**3/3)


# r = 25
# print("Объем шара с радиусом", r, "равен", sphere_volume(r), ".")

# a = 1

# def fun(x):
#     global a
#     a += a + 1
#     return x * 3 * 4 * 5

# a = 134
# print(fun(fun(fun(fun(1)))))

# a = "356"
# b = "e2"
# try:
#     c = a + '.' + b
#     c = float(float(c))
# except:
#     c = -1
# print(c)

# n = 42
# while n <= 42:
#     print(n)
# print("Цикл закончился!")

# r = 42
# a = 32

# def f(a):
#     d = 123*(a+r)
#     return d
# print(f())

# import math

# d = 1
# try:
#     a = 2 + 2 * 2
#     b = (a - 2) // 2 - 2
#     d = a + b
#     c = a / b
# except:
#     d = -1 / math.sqrt(b - a)
#     d = -1
# print(d)

# r = 42
# a = 32

# def f(a):
#     d = 123*(a+r)
#     return d

# k = 1

# def dice_roll():
#     global  k
#     n = k
#     m = 8
#     a = 1664525
#     c = 1013904223
#     r = 2015
#     while n > 0:
#         r = (a * r + c) % m
#         n = n - 1
#     k = k + 1
#     return (r % 6) + 1
# print(dice_roll

# n = 0
# new_word = ""
# while n < len("Hello world"):
#     if n % 2 == 0:
#         new_word += "a"
#     else:
#         new_word += (len(new_word) // 3)*"b"
#     n += len('Hello') % 2
# print(new_word)

# r = 42
# a = 32

# def f(a):
#     d = 123*(a+r)
#     return d

# c = 54
# def getKollatc(num):
#     count = 0
#     while True:
#         if num == 1:
#             break
#         if (num % 2 == 0):
#             num /= 2
#         else:
#             num *= 3
#             num += 1
#         count += 1
#     return count
# print(getKollatc(80))

# a=True
# b=True

# def f1():
#     if a == True and b == True:
#         return False
#     elif a == True or b == False:
#         return True
#     else:
#         return False
# def f2():
#     return not (a and b) and (a or not b)
# def f3():
#     return (not a) and b
# def f4():
#     return (not a) or (not b)
# print(f1())
# print(f2())
# print(f3())
# print(f4())

# a=False
# b=False
# def f1():
#     if a == True:
#         return False
#     elif b == False:
#         return False
#     elif a == False:
#         return False
#     else:
#         return True
# print(f1())

n1, n2 = map(int, input().split(' '))
arr = []
count = 0
while count < n1:
    arr.append(map(int, input().split(' ')))
    count += 1
print(arr)