# # 可变：可以原地修改、增加、删除元素；不可变：不能修改内部元素，只能生成新对象。
#
# # 1.列表list[1,2,3]可变，有序，允许重复
# lst = [10, 20, 30]
# lst.append(40)  # 末尾追加一个
# print(lst)
# lst.extend([50, 60])  # 把可迭代对象拆开追加
# print(lst)
# lst.insert(1, 15)  # 指定下标插入
# print(lst)
# lst.pop()  # 默认删最后一个，可传下标 pop(2)
# print(lst)
# lst.remove(20)  # 删除第一个匹配的元素
# print(lst)
# lst.index(30)  # 返回元素下标
# print(lst.index(30))
# lst.count(10)  # 统计元素出现次数
# print(lst.count(10))
# lst.sort()  # 原地排序
# print(lst)
# lst.reverse()  # 原地反转
# print(lst)
##error:赋值不是拷贝：b = lst，b 和 lst 指向同一个列表；改 b，原列表也变。复制要用 b = lst.copy() 或者 b = lst[:]
# a = [1, 2]
# b = a
# b[0] = 99
# print(a)  # a被修改！
##remove如果删除的值不在列表里报错
##pop按下标删除，下标不存在报错
##切片会产生新列表[:]
##sort原地修改列表，返回none（没有return新结果）lst.sort
##sorted(lst)返回新列表
##遍历列表的时候删除元素，下标会错乱，应该创建新列表把需要的放进去
# lst = [1,2,3,4,5]
# new_lst = []
# for i in lst:
#     if i % 2 != 0: # 留下奇数
#         new_lst.append(i)
# print(new_lst)
#
# # 2.元组tuple(1，2，3)不可变(元组内部存放的内存地址不能改)(如果里边有列表这种可变对象，那列表内可以修改)，有序，允许重复
# # 创建元组 ①t1=(10,20,30,20),②t2=100,200,3000
# # 单元素元组必须写逗号
# a = (6)
# print(type(a))  # <class 'int'> ，这只是整数6，不是元组
# b = (6,)
# print(type(b))  # <class 'tuple'> ，加逗号才是元组
# # 空元组
# empty_t = ()
# print(empty_t)
#
# t = (10, 20, 30, 40)  # 元组有序，支持数字下标、负数下标、切片，和列表一模一样。
# print(t[0])  # 10，取第0位
# print(t[-1])  # 40，取最后一位
# print(t[1:3])  # (20, 30)，切片返回新元组
# # t[0] = 99  # 报错！元组不允许修改元素
#
# # 元组仅有的两个内置方法 count()、index()
# t = (1, 2, 2, 3)
# print(t.count(2))  # 2，数字2出现2次
# print(t.index(2))  # 1，数字2第一次出现在下标1
# # print(t.index(99)) # 99不存在，报错
# t = (1, 2, [3, 4])
# print(t)
#
# t[2][0] = 99  # 修改里面列表的内容，允许
# t[2].append(100)  # 给内部列表追加元素，允许
# print(t)
# # t[2] = [77,88]  # 试图把元组第2位，换成一个新列表，不允许
#
# #元组转换
# lst = [10,20,30]
# t = tuple(lst)   # 列表 → 元组
# lst2 = list(t)   # 元组 → 列表
#
# # 3.字典dict{"name":"student","age":"18"}可变，有序，key(name)不可重复，value(student)可以重复
# # 字面量创建
# d1 = {"name":"张三", "age":18, "score":90}
# # 空字典
# empty_d = {}
# # key重复：后面的会覆盖前面的
# d2 = {"a":10, "a":99}
# print(d2) # {'a': 99}，后面覆盖前面
# # 合法key：int、str、tuple（不可变）
# d_ok = { 1:"数字key", "hi":"字符串key", (1,2):"元组key" }
# # 非法key：列表、集合是可变，不能做key
## d_bad = { [1,2]: 666 }
#
# 读取字典中的值
# d = {"name": "张三", "age": 18}
# # ①
# print(d["name"])
# # ②
# print(d.get("age"))
# # 修改
# d = {"name": "张三", "age": 18}
# d["age"] = 19
# # 新增
# d["gender"] = "male"
# # 删除
# res = d.pop("age")
# print(res)
# print(d)
# # 三个视图方法
# d = {"name": "张三", "age": 18}
# print(d.keys())
# print(d.values())
# print(d.items())
# # 把items转成列表
# d = {"a":1,"b":2}
# lst = list(d.items())
# print(lst)
#
# # 4.集合set{1，2，3}可变，无序，不允许重复
# # 直接写，自动去重
# s1 = {1, 2, 2, 3, 3, 3}
# print(s1)
# # 空集合不能写 {} ，{}是空字典！
# empty_set = set()
# empty_dict = {}
# print(type(empty_set), type(empty_dict))
# # 可迭代对象转集合：列表、元组转set
# lst = [5, 5, 6, 6]
# s2 = set(lst)
# print(s2)
# # 集合内部不能放列表（可变类型）
# # s_bad = { [1,2], 3 } # 报错
#
# s = {1, 2, 3}
# s.add(4)  # 添加单个元素
# print(s)
# # remove(x)：删除x，如果集合没有x → 报错KeyError
# s.remove(2)
# # s.remove(99)
# # discard(x)：删除x；就算元素不存在，什么都不干，不报错
# s.discard(99)
# # pop()：随机删除一个元素（集合无序，不知道删哪个）
# s.pop()
#
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# jiaoji = s1 & s2  # 交集，两边同时存在元素 {3}
# bingji = s1 | s2  # 并集，全部元素去重 {1,2,3,4,5}
# chaji = s1 - s2  # 差集：s1有，s2没有 {1,2}
# print("交集", jiaoji)
# print("并集", bingji)
# print("差集", chaji)
#
# s = {10,20,30}
# print(10 in s)   # True
# print(99 in s)   # False
