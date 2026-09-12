lst = []
for i in range(1, 11):
    lst.append(i ** 2)
print(lst)
# 进阶：只存偶数的平方
lst2 = []
for i in range(1, 11):
    if i % 2 == 0:
        lst2.append(i ** 2)
print(lst2)
poke_types = ["♥", "♦", "♠", "♣"]
poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
poke_list = []
for p_type in poke_types:
    for p_num in poke_nums:
        poke_list.append(f"{p_type}{p_num}")
print(poke_list)
shopping_cart = []
while True:
    print("--- 购物车清单 ---")
    print("1. 添加商品")
    print("2. 删除商品")
    print("3. 查看购物车")
    print("4. 结束程序")
    choice = input("请输入选项：")
    if choice == "1":
        item = input("请输入要添加的商品：")
        shopping_cart.append(item)
        print("已添加商品：", item)
        print()
    elif choice == "2":
        if len(shopping_cart) == 0:
            print("购物车为空, 无法删除商品。")
        else:
            item = input("请输入要删除的商品：")
            if item in shopping_cart:
                shopping_cart.remove(item)
                print("已删除商品：", item)
            else:
                print("购物车中没有该商品。")
        print()
    elif choice == "3":
        if len(shopping_cart) == 0:
            print("购物车为空。")
        else:
            print("*" * 15)
            for item in shopping_cart:
                print(item)
            print("*" * 15)
        print()
    elif choice == "4":
        print("程序结束")
        break
# 不可变类型：int
x = 1
print(id(x))
x = 2
print(id(x))
# 不可变类型：字符串
s = "yuan"
print(id(s))
s = "Yuan"
print(id(s))
# 可变类型：列表
l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l))  # 内存地址不变
