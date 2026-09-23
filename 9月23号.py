# x, y = map(int, input().split())
# print(x // y)

# nums = list(map(int, input().split()))
# nums.sort()
# a = input()
# b = []
# for i in a:
#     if i == 'A':
#         b.append(nums[0])
#     elif i == 'B':
#         b.append(nums[1])
#     elif i == 'C':
#         b.append(nums[2])
# print(' '.join(map(str, b)))
# #
# n = int(input())
# c = 0
# for i in range(n + 1):
#     c += i
# print(c)


l, n, m = map(int, input().split())
rock = [0]
for i in range(n):
    a = int(input())
    rock.append(a)
rock.append(l)


def check(mid):
    remove = 0
    last = 0
    for i in range(1, len(rock)):
        if rock[i] - rock[last] < mid:
            remove += 1
        else:
            last = i
    return remove <= m


left = 1
right = l
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
