from os import times_result

# #5736质数筛
# def fun(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# n = int(input())
# a = [int(i) for i in input().split()]
# for i in range(n):
#     if fun(a[i]):
#         print(a[i], end=' ')
##a = list(map(int, input().split()))
#
# n, m = map(int, input().split())
# for i in range(n):
#     if i % m == 0:
#         print(i)
#         n -= 1
#         i -= 1
#         if i == n:
#             i = 1
#
#
# n, m = map(int, input().split())
# people=list(range(1,n+1))
# i=0
# while len(people)>0:
# for _ in range(m-1):
#     i+=1
#     if i>=len(people):
#         i=0
# print(people.pop(i))
# n, m = map(int, input().split())
#
# people = list(range(1, n + 1))
# i = 0
# list = []
#
# while people:
#     i = (i + m - 1) % len(people)
#     list.append(str(people.pop(i)))
#
# print(" ".join(list))
#
# n = int(input())
# a = list(map(int, input().split()))
# min = a[0]
# max = a[0]
# for i in range(1, n):
#     if a[i] > max:
#         max = a[i]
#     if a[i] < min:
#         min = a[i]
# print(max - min)

# ai = list(map(int, input().split()))
# for i in ai:
#     if i == 0:
#         break
# ai.pop()
# print(' '.join(map(str, ai[::-1])))
