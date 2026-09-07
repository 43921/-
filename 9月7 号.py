# 循环案例之验证码
import random

count = 0
s = ""
while count < 5:
    char = random.choice("string.digits+string.ascii_letters")
    s += char
    count += 1
print("验证码", s)

# for循环
"""
for i in 容器对象：
   循环语句
"""
for i in range(5):
    char = random.choice("string.digits+string.ascii_letters")
    print("char", char)

# 计算和
l = [35, 66788, 67, 9965, 66, 899]
ret = 0
for i in l:
    ret += i
print(ret)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("hrgrt")
    elif i % 3 == 0:
        print("df")
    elif i % 5 == 0:
        print("gtr")
    else:
        print(i)

import random

coin = 0
exp = 0
blood = 100

room = "怪物房"
if room == "怪物房":
    # for循环，连续打3只怪
    for i in range(3):
        print(f"\n====第{i + 1}只史莱姆出现====")
        choice = input("[1.攻击/2.逃跑]")
        if choice == "1":
            print("选择干史莱姆！")
            is_success = random.choice([100, 200])
            if is_success >= 120:
                print("战胜史莱姆！")
                coin += 20
                exp += 20
            else:
                print("没打过史莱姆！")
                coin -= 20
                exp -= 20
                blood -= 20
        elif choice == "2":
            print("逃跑ing")
            break  # 逃跑直接跳出循环，不打下一只
print(f"\n战斗结束！金币：{coin} 经验：{exp} 血量：{blood}")

# 打印扑克
poke_types = ["♥", "♦", "♠", "♣"]
poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
# 外层循环：遍历4种花色
for pt in poke_types:
    # 内层循环：遍历13个牌面数字
    for p_num in poke_nums:
        print(f"{pt}{p_num}")

# break 退出整个循环
