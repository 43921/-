#昨天的又补了一部分
# a, b, c = map(int, input().split())
# list = sorted([a, b, c])
# print(list[0], list[1], list[2])

n = int(input())
b = []
for i in range(2, n + 1):
    num = int(input())
    for i in range(2, i + 1):
        if num % i == 0:
            b.append(i)
print(b)
