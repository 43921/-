# # strip:去除两端的空格或换行符
# name = " cedehcyued   "
# print(name)
# print(name.strip())
#
# # 去除多余的符号
# s = "&&&&abcd&&&&"
# print(s.strip("&"))
# print(s.lstrip("&"))  # 去除一侧的
#
# # 判断字符串是否为数字字符串
# print("apple".isdigit())
#
# cities = "北京 哈尔滨 重庆 大连"
# ret = cities.split(" ")  # ['北京', '哈尔滨', '重庆', '大连']
# print(ret)
# print(len(ret))
#
# ret = ['北京', '哈尔滨', '重庆', '大连']
# # ret.join(",")
# print(",".join(ret))
#
# info = "yuan|19|185"
# ret = info.split("|")  # ["yuan", "19", "185"]
# print(ret)
#
# text = "yuan|19|185"
# res = text.replace("|", "-")
# # replace(旧字符,新字符)
# # 旧 = |
# # 新 = -
# print(res)  # yuan-19-185
#
# # count计算出现次数
# a = "ab dd dfffefrrrrf ab  ab"
# print(a.count("ab"))
#
# # 练习
# s = "abcdefg"
# print(s[2:])
#
# ret = input('输入"Y"或"N"')
# print(ret == "Y" or ret == "y")
#
# exp = input("双值加法表达式")  # 用户输入：3+5
# ret = exp.split("+")  # 切割后 ret = ['3','5']
# num1 = int(ret[0].strip())  # ret[0]取第一个元素 '3'，转成数字3
# num2 = int(ret[1].strip())  # ret[1]取第二个元素 '5'，转成数字5
# print(num1 + num2)  # 计算 3+5
#
# # 拆分三位数
# ret = input("请输入数字")
# bai = ret[0]
# shi = ret[1]
# ge = ret[2]
# print(bai, shi, ge)
#
# # 定义一个Linux风格的文件路径字符串（斜杠 / 分隔）
# path = "/Users/yuan/npm/index.js"
# # 方式1：直接用replace把所有 / 替换成 \
# # print(path.replace("/", "\\"))
# # 方式2：先切割，再拼接
# # 以斜杠"/"作为分隔符，把路径切成字符串列表
# print(path.split("/"))
# ret = path.split("/")
# # 使用join，用双反斜杠"\\"把列表里的每一段重新拼起来，变成Windows路径格式
# print("\\".join(ret))
#
# # 判断回文
# s = "shdufhnr"
# print(s == s[::-1])
#
# # 输入字符串，长度4的倍数
# # 用户输入字符串
# data = input("请输入字符串：")
# if len(data) % 4 != 0:
#     data += "=" * (4 - len(data) % 4)
# print(data)
