data = input("请输入一段文本：")
count = 0
for char in data:
    if char.lower() in "aeiou":
        count += 1
print("元音字母出现次数：", count)
prev = 0
current = 1
next_num = 0
for _ in range(18):
    next_num = prev + current
    prev = current
    current = next_num
print("第20个斐波那契数:", next_num)
