# # 流程控制语句
# # 1分支语句
# # 冒号+缩进4个：标识语句块
# """
# if 表达式：
#     语句一
#     语句二
# else：
#     语句三
#     语句四
# print() #这句和else无关
# """
# score = 75
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")
#
#     print("测试一下")
# print("跳出循环")
#
# year = int(input("请输入年份"))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("闰年")
# else:
#     print("not")
# print("over")
#
# # 版本1双分支：
# num01 = int(input("num01:"))
# num02 = int(input("num02:"))
# if num02 < num01:
#     print("较小值：", num02)
# else:
#     print("较小值：", num01)
# # 版本2单分支：
# num01 = int(input("num01:"))
# num02 = int(input("num02:"))
# if num01 < num02:
#     num02, num01 = num01, num02
# print("大值", num01)

# 多分支语句
"""
if ...:

elif ...:

elif ...:

else:

"""
# height = float(input("请输入身高(米):"))
# weight = float(input("请输入体重(千克):"))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     advise = f"您的BMI的值{bmi:.3f}, 体重过轻, 建议多吃少动"
# elif 18.5 <= bmi < 24:
#     advise = f"您的BMI的值{bmi:.3f}, 体重正常, 建议保持!"
# elif 24 <= bmi < 28:
#     advise = f"您的BMI的值{bmi:.3f}, 体重稍胖, 建议多动少吃!"
# else:
#     advise = f"您的BMI的值{bmi:.3f}, 太肥胖, 建议控制饮食!"
# print("我们的建议: ", advise)

# import random
#
# room = random.choice(["森林", "海洋", "陆地", "天空"])
# print(room)
#
# # 分支嵌套
# age = int(input("输入年龄："))
# if age >= 18:
#     print("已经成年")
#     if age < 30:
#         print("青年")
#     elif age < 60:
#         print("中年")
#     else:
#         print("老年")
# else:
#     print("未成年")
