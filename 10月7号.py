# k = int(input())
# s = str(input())
# n = int(input())
# hashmap = dict()
# p = dict()
# for i in range(n):
#     p[i] = str(input())
#     if p[i] in s:
#         if p[i] in hashmap:
#             hashmap[p[i]] += 1
#         else:
#             hashmap[p[i]] = 1
# print(hashmap)
k = int(input())
s = input()
n = int(input())

for _ in range(n):
    p = input()
    m = len(p)
    count = 0
    for i in range(len(s) - m + 1):
        sub = s[i: i + m]
        diff = []
        for j in range(m):
            if sub[j] != p[j]:
                diff.append(j)
        if len(diff) <= 1:
            count += 1
        else:
            if diff[-1] - diff[0] < k:
                count += 1

    print(count)