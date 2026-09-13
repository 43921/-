poke_types = ["♥", "♦", "♠", "♣"]
poke_nums = ["A", 2, 3, 4, 6, 'J']
poke_list = []
for p_type in poke_types:
    for p_num in poke_nums:
        poke_list.append(f"{p_type}{p_num}")
        print(poke_list)
o_list = ["a", "8", "b"]
oo_list = o_list.copy()
oo_list[0] = "6"
print(o_list)
oo_list = ["9", "8", "2", "1", "0"]
print(oo_list)
# 洛谷P1225
p = int(input())
if p == 1:
    print(1)
elif p == 2:
    print(2)
else:
    a, b = 1, 2
    for i in range(3, p + 1):
        a, b = b, a + b
    print(b)
