# 布尔值
print(bool(2 < 1))  # 假
print(bool("2<1"))  # 因为是字符串所以为真

# id函数,id()查看内存地址，判断两个变量是不是指向同一个东西
x = 100
print(id(100))
print(id(x))
# type
print(type(100))

# 输入圆的半径求面积周长
r = int(input("请输入圆的半径："))
c = 2 * 3.14 * r
s = 3.14 * r * r
print(c)
print(s)

# count增加五次
count = 0
count += 1
count += 2
count += 3
count += 4
count += 5
print(count)

# 判断成绩是不是在80~100
score = int(input("输入分数"))
if (score >= 80 and score <= 100):
    print("合格")
else:
    print("不合格")
# 或者
print(score >= 80 and score <= 100)

# 输入一个数字，判断是不是三位数且能被13整除
a = int(input("请输入一位三位数"))
print(a / 100 > 0 and a < 999, "三位数")
if (a % 13 == 0):
    print("yes")
else:
    print("no")
# 或者
num = input("请输入数字")
print(len(num) == 3 and int(num) % 13 == 0)

# 判断是不是闰年
year = int(input("请输入年份"))
print(year % 4 == 0 and year % 100 != 0 or (year % 400 == 0))
