# w, x, h = map(int, input().split())
# q = int(input())
# v = [[[False] * (h + 1) for o in range(x + 1)] for r in range(w + 1)]
# for a in range(q):
#     x1, y1, z1, x2, y2, z2 = map(int, input().split())
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             for k in range(z1, z2 + 1):
#                 v[i][j][k] = True
#     c = 0
#     for i in range(1, w + 1):
#         for j in range(1, x + 1):
#             for k in range(1, h + 1):
#                 if not v[i][j][k]:
#                     c += 1
# print(c)
#
# w, x, h = map(int, input().split())
# q = int(input())
# # 三维数组
# v = [[[False] * (h + 1) for o in range(x + 1)] for r in range(w + 1)]
# for a in range(q):
#     x1, y1, z1, x2, y2, z2 = map(int, input().split())
#     for i in range(x1, x2 + 1):
#         for j in range(y1, y2 + 1):
#             for k in range(z1, z2 + 1):
#                 v[i][j][k] = True
# c = 0
# for i in range(1, w + 1):
#     for j in range(1, x + 1):
#         for k in range(1, h + 1):
#             if not v[i][j][k]:
#                 c += 1
# print(c)


c = 0
num = int(input())
if num <= 150:
    b = f"{num * 0.4463:.1f}"
if 151 <= num <= 400:
    b = f"{(num - 150) * 0.4663 + 150 * 0.4463:.1f}"
if num >= 401:
    b = f"{(num - 400) * 0.5663 + (num - 150) * 0.4663 + 150 * 0.4463:.1f}"
print(b)
