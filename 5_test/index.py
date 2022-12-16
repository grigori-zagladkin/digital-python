# a = [49, 27, 101, -10]
# b = a
# c = list(a)
# d = c
# a[3] = 68
# c[2] = a[1]
# b = a[1:3]
# b[1] = c[2]
# print(b)

# lst = [1, 2, 3, 5, 7, 11]
# t = tuple([[30, 40], lst, [20]])
# lst.append(25)
# l2 = t[2]
# l2.append(10)
# print(t[2])
# print(len(t[1]))
# print((t[1]))
# print((t[2]))

# def function1(a):
#     b = list(a)
#     b.pop()
#     a.pop()
#     return a[0]+1
#
# def function2(b):
#     for i in range(len(b)):
#         b[i] += 1
#
# lst = [1, 2, 5, 7, 9]
# function2(lst)
# function1(lst)
# print(lst)

# class Account:
#     def __init__(self, id):
#         self.id = id
#         id = 666
#
# acc = Account(123)
# print(acc.id)

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, deltax=0, deltay=0):
        self.x += deltax
        self.y += deltay
# point1 = Point2D(3, 9)
# point2 = Point2D()
# point2.translate(20, 4) - true

# point = Point2D([3, 9])
# point.translate(5, -2)

# Point2D = (3, 9)
# Point2D.translate(5, -2)

# point = Point2D(7.0, 13.5)
# point.translate(8.16, 12.1) - true

# points = [(2, 5), (8, 3), (0, 2)]
# for point in points:
#     point.translate(-1, -1)

# points = [Point2D(2, 5), Point2D(8, 3), Point2D(0, 2)]
# for point in points:
#     point.translate(-1, -1) - true

# point0 = Point2D(2, 5)
# point1 = Point2D(8, 3)
# point2 = Point2D(0, 2)
# points = [point0, point1, point2]
# points.translate(-1, -1)

# point = Point2D(-1, 5)
# s = str(point)

# point = Point2D(10, 8)
# tup = tuple(point)

# point = Point2D(7, 21)
# lst = list(point)

# names1 = ['Виктор', 'Егор', 'Арсений', 'Иван']
# names2 = names1
# names3 = names1[:]
#
# names2[0] = 'Alice'
# names3[1] = 'Bob'
#
# s = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         s += 1
#     elif ls[1] == 'Bob':
#         s += 10
# print(s)

# b = [3, 4]
# d = b[1] / b[0]
# print(type(b), type(d), type(b[1]), type(b[1]/b[0]))

# t = ([1], [2], 3, 10)
# t1 = t[0]
# t1.append(10)

