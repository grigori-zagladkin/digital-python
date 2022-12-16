# C. Четные, но не кратные шести
# N, K = map(int, input().split())
# A = map(int, input().split())
# counter=0
# _c = 0
# for el in A:
#     if el % 2 == 0 and el % 6 != 0:
#         _c = _c + 1
#         if _c >= K:
#             counter = counter + 1
#     else:
#         _c = 0
# print(counter)
# интересный делитель
# L, R = map(int, input().split())
# if (R % L == 0):
#     print(1)
# else:
#     print(0)

#A. Несуразные отношения
# print(max(list(map(int, input().split())))+min(list(map(int, input().split()))))

# D. Счастливые 28-04-K-
# def prod(arr):
#     i=1
#     for j in arr:
#         i = i*j
#     return i
# N, K = map(int, input().split())
# A = [int(i) for i in input().split()]
# counter=0
# for i in range(N-2):
#     if (sum([A[i], A[i+1], A[i+2]]) % 28 == 0 and prod([A[i], A[i+1], A[i+2]]) % 4 == 0):
#         counter += 1
# print(counter)
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# if len(A) < K:
#     print(0)
#
# wind = A[:K]
# sum_=  sum(wind)
# product = prod(wind)
# counter =  1 if sum_ % 28 == 0 and product % 4 == 0 else 0
# last_elem = A[0]
#
# idx = 0
# for idx in range(N):
#     if idx >= K:
#         wind = wind[1:] + [A[idx]]
#         sum_ = sum(wind)
#         product = prod(wind)
#
#         counter +=  1 if sum_ % 28 == 0 and product % 4 == 0 else 0
#
#     idx += 1
#
