# while True:
#     s = input()
#     left, right = s.split(".")
#     num = float(s)
#     if 100 <= num < 1000 and len(s.split(".")[-1]) == 1:
#         res = right + "." + left[::-1]
#         print(res)
#         break
#     else:
#         print("要求输入100~1000一位小数的浮点数，请重输")
# # 呃呃呃
# s = input()
# print(float(s[::-1]))
# 闰年判断
# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(1)
# else:
#     print(0)
# # 闰年个数
# a, b = map(int, input().split())
# count = 0
# c = []
# for i in range(a, b + 1):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         count += 1
#         c.append(i)
#     else:
#         continue
# print(count)
# print(' '.join(map(str, c)))
#
# list = []
# for i in range(1, 11):
#     list.append(i ** 2)
# print(list)
# even = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i ** 2)
# print(even)
# res1 = [i ** 2 for i in range(1, 11)]
# print(res1)
# res2 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
# print(res2)
# import random
#
# list = [1, 34, 56789, 765, 45]
# even = [3, 556, 87, "A4", 67]
# for i in range(0, len(list)):
#     for j in range(0, len(even)):
#         card = f"{list[i]},{even[j]}"
#         print(card)
# # 随机生成，不重复
# hand = random.sample(even, 2)
# print(hand)
# numbers = [1, 2, 3]
# letters = ['A', 'B', 'C']
# combined = [(number, letter) for number in numbers for letter in letters]
# print(combined)
#
# # 关键字参数：用形参名=值的形式传参
# def info(name, age):
#     print(name, age)
#
#
# info("xiaoming", 18)

# 关键字参数最大优势是什么？
# 参数多时，可以跳过中间默认参数，直接给指定参数赋值；传参不受形参顺序约束，可读性更强。
# 函数定义 def func(a, b=None):，为什么用None作为默认值？
# 用None占位，用来区分两种情况：用户没有传参（使用默认）、用户主动传入了值；遵循 PEP8 规范，用is None判断。
#
# # *星号两大功能
# x, y, *z = [1, 2, 3, 4, 5, 6]
# # 1x=1，y=2，z=[3,4,5,6]收集多余元素，打包成列表
# # 首尾取值：中间打包
# o, *p, q = [1, 2, 3, 4]
#
#
# # 2函数可变参数 args（函数定义时的）
# # *args：接收任意多个位置参数，打包成元组 tuple
# def add(*arges):
#     print(arges)
#     ret = 0
#     for a in arges:
#         ret += a
#     print(ret)
#
#
# add(1, 2, 34, 5)
#
# print(1, 2, 3, sep=',', end='')
# # 输出：1,2,3 ，不会自动换行
#
# # **kwargs：接收任意数量关键字参数，打包成字典
# def print_info(**kwargs):
#     print(kwargs)
#
#
# print_info(name="yuan", age=18, gender="男")
