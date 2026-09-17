# # 一个从1加到100的函数
# def cel(n):
#     ret = 0
#     for i in range(1, n + 1):
#         ret += i
#     return ret
#
#
# # 调用
# print(cel(100))
#
#
# # 默认参数(输入用新的，没有用旧的）
# def show(name, age, gender="male"):
#     print(name, age, gender)
#
#
# show(name="ss", age=23)
#
#
# def discount(cart, acart=0.7):
#     total = 0
#     for goods in cart:
#         total += goods["price"] * goods["weight"]
#     return round(total * acart)
#
#
# cart1 = [{"name": "apple", "price": 5, "weight": 4}]
# print(discount(cart1, acart=0.2))
#

# 默认参数两个
def cal(end=None, start=None):
    if end is None and start is None:
        return 0
    if start is None and end is not None:
        start = 1
    if start > end:
        start, end = end, start
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


print(cal())
print(cal(100))
print(cal(66, 88))
