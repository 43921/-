# # break continue
# for i in range(1, 101):
#     if i == 88:
#         break
#     print(i)
# for i in range(1, 101):
#     if i == 88:
#         continue
#     print(i)
# for i in range(1,101):
#     if i!=88:
#         print(i)
# # 计算1-100整除13之和
# ret = 0
# for i in range(1, 101):
#     if i % 13 == 0:
#         ret += i
# print(ret)
#
# # 分支练习
# char = input("请输入字符")
# #转小写
# # char=char.lower
# if char in "aeiouAEIOU":
#     print("yes")
# else:
#     print("no")
#
# # 身份证判断男女
# id = input("请输入身份证号")
# if len(id) == 18:
#     num = int(id[17])
#     if num % 2 == 0:
#         print("女生")
#     else:
#         print("男生")
# else:
#     print("身份证错误请重新输入")
