# # 洛谷P3735 没解出来0分
# k = int(input("num"))
# s = input("请输入字符串")
# n = int(input("num"))
# c = input()
# res = s.split("s", n)
# print(s.count(str(res == c)))
#
# # python学习
# # 断点调试
# x = 1
# y = 2
# print(x, y)
# x = 10
# print(x)
# x = 100
# print(x)
#
# # while
# """
# while 表达式：
#     循环语句块
# """
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# cont = 1
# while cont <= 100:
#     print(cont)
#     cont += 1
# import random
# char_pool = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# code = ""
# i = 0
# # while生成4位验证码
# while i < 4:
#     c = random.choice(char_pool)
#     code = code + c
#     i = i + 1
# print("验证码：", code)
# # while循环校验
# while True:
#     user = input("请输入验证码：")
#     if user == code:
#         print("验证成功")
#         break
#     else:
#         print("错误，重新输入")
