# m, n = map(int, input().split())
# c = [0] * 10
# for i in range(m, n + 1):
#     x = i
#     while x:
#         c[x % 10] += 1
#         x = x // 10
# print(' '.join(map(str, c)))
#
# c = [0] * 26
# for _ in range(4):
#     line = input()
#     for i in line:
#         if 'A' <= i <= 'Z':
#             c[ord(i) - ord('A')] += 1
# max1 = max(c)
# for i in range(max1, 0, -1):
#     line1 = []
#     for e in c:
#         if e >= i:
#             line1.append('*')
#         else:
#             line1.append(' ')
#     print(' '.join(line1))
# p = [chr(ord('A') + i) for i in range(26)]
# print(' '.join(p))
#
# import numpy as np
#
# a, b, c, d = map(int, input().split())
# s = np.roots([a, b, c, d])
# s.sort()
# res = [f"{x:.2f}" for x in s]
# print(' '.join(res))
#
# def student():
#     n = int(input())
#     list = []
#     for i in range(n):
#         n, y, s, x = input().split()
#         d = {"name": n, "yu": int(y), "shu": int(s), "ying": int(x), "zong": int(y) + int(s) + int(x)}
#         list.append(d)
#     return list
#
#
# def check(list):
#     m = len(list)
#     for i in range(m):
#         a = list[i]
#         for j in range(i + 1, m):
#             b = list[j]
#             dy = abs(a["yu"] - b["yu"])
#             ds = abs(a["shu"] - b["shu"])
#             dx = abs(a["ying"] - b["ying"])
#             dz = abs(a["zong"] - b["zong"])
#             if (dy <= 5 and dz <= 10 and dx <= 5 and ds <= 5):
#                 print(a["name"], b["name"])
#
#
# data = student()
# check(data)
#
# m, n = map(int, input().split())
# b = []
# c = 0
# a = list(map(int, input().split()))
# for i in range(n):
#     word = a[i]
#     if word not in b:
#         c += 1
#         b.append(word)
#         if len(b) > m:
#             b.pop(0)
# print(c)
def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


a, b, c, d = map(int, input().split())
ans = []
for i in range(-100, 100):
    L = i
    R = i + 1
    y1 = f(L, a, b, c, d)
    y2 = f(R, a, b, c, d)
    if abs(y1) < 1e-6:
        ans.append(L)
    elif y1 * y2 < 0:
        l = L
        r = R
        for _ in range(100):
            m = (l + r) / 2
            y = f(m, a, b, c, d)
            if y * y1 <= 0:
                r = m
            else:
                l = m
        ans.append(l)
print(f"{ans[0]:.2f} {ans[1]:.2f} {ans[2]:.2f}")
