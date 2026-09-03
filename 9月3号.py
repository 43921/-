# # 字符串
# # 转义符普通符号特殊化
# a = "apple\tbanana"  # 自动空格
# b = "orange\nmango"  # 换行
# c = "abcdef\b"  # 删掉最后一个字母
# print(a, b, c)
# # 特殊符号普通化
# # \\就变普通
# print("htggghtp.com\\tohjyjken")
# # 或者raw-string原生字符串
# s = r'fherugerrevj\ndefre'
# print(s)
#
# # 引号
# print("i am \"xiaoliu\"")

# 格式化输出
# # %占位符
# name = "student"
# age = 20
# s = """
#      信息：
#      姓名:%s
#      年龄:%s
# """ % (name, age)
# print(s)
# f-str
# name = "student"
# age = 20
# S = f"姓名:{name:15}，年龄:{age:<10}"
# # name后边的15为占位符,age后边 < 表示左对齐
# print(S)
#
# # 索引的语法，字符串对象[索引]，获取一个字符
# # 正着数 0 1 2 3 4 5 6 7 倒着数 -1 -2 -3 -4 -5 从小数写到大数
# s = "i have a dream"
# print(s[6], type(s[6]))
# print(s[0])
# print(s[-1])
# s = "abcdefgefguh"
# print(s[::2])
# # 下标：0:a 1:b 2:c 3:d 4:e 5:f 6:g
# # 取出 0,2,4,6 → "aceg"
# print(s[::-1])  # 从右向左取
# print(s[3:0])  # 这个是不行的
# print(s[3:0:-1])  # 这个可以
# # 切片的语法：字符串对象[开始索引:结束索引:步长(默认为1)] [左闭右开]，包括下标为左边的不包括右边的
# print(s[0:5])
# print(s[6:9])
# print(s[6:])  # 缺省取到末尾
# print(s[0:5])  # 缺省从开头开始

# # 字符串不能修改，只能再创建一个新的
# #不可变（只能替换）：int /float/str /bool/tuple 可变（原地修改）：list /dict/set
# s1 = "abc"
# s1 = "def"
# # 这种是重新赋值，原来的被释放
# # s1[0]="R“这种修改是不行的

# # 内置函数len
# s = "hello world"
# print(len(s))
# # 取数
# print(s[-1])  # -1代表最后一位，负数索引
# print(s[len(s) - 1])  # 用长度换算出最后一位下标
#
# # 拼接 +拼接起来， *拼接很多遍
# s1 = "123"
# s2 = "456"
# s3 = "789"
# a = s1 + s2 + s3
# print(a)
# print(s1 * 20)
#
# # in返回布尔值(可以写in或者not in)
# print("i am" in "i am a student")
#
# # 字符串的内置方法(类型方法) 某某某.某某某 例:str.upper
# s = "apple"  # "apple"是字符串对象，s是字符串变量的对象
# s1 = s.upper()
# print(s, s1)
# # 直接写
# print("i am a student".upper())
