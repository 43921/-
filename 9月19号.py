# n = int(input())
# a = 1
# s = 0
# for i in range(1, n + 1):
#     a *= i
#     s += a
# print(s)
#
#
# import math
#
# a, b, c = map(int, input().split())
# p = (a + b + c) / 2
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(f"{s:.1f}")
#
# a, b, c = map(int, input().split())
# s = a * 0.2 + b * 0.3 + c * 0.5
# print(int(s))

import sys


# 填上你觉得需要的其他模块

def main():
    T = int(input())
    if T == 1:
        print("I love Luogu!")
    elif T == 2:
        print(2 + 4, 10 - 2 - 4)
    elif T == 3:
        print(3)
        print(12)
        print(2)
    elif T == 4:
        a = 500 / 3
        print(f"{a:.6g}")
    elif T == 5:
        print(int(260 / 32))
    elif T == 6:
        import math
        print(math.sqrt(9 * 9 + 6 * 6))
    elif T == 7:
        print(f"{110}\n")
        print(f"{90}\n")
        print(f"{0}\n")
    elif T == 8:
        pai = 3.141593
        print(2 * pai * 5)
        print(pai * 5 * 5)
        print(pai * 5 * 5 * 5 * 4 / 3)
    elif T == 9:
        res = 1
        for i in range(3):
            res = (res + 1) * 2
        print(res)
    elif T == 10:
        import math
        n1, t1, n2, t2 = map(int, (input().split()))
        x = (n1 * t1 - n2 * t2) / (t1 - t2)
        y = n1 * t1 - x * t1
        t3 = int(input())
        res = (y + x * t3) / t3
        print(math.ceil(res))
    elif T == 11:
        # 请自行完成问题 11 的代码
        pass
    elif T == 12:
        # 请自行完成问题 12 的代码
        pass
    elif T == 13:
        # 请自行完成问题 13 的代码
        pass
    elif T == 14:
        # 请自行完成问题 14 的代码
        pass


if __name__ == "__main__":
    main()
