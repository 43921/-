# s = "hello yuan"
# # 字符串不可变！不能直接 s[-2] = "A" 修改字符
# ret = list(s)  # 把字符串转成列表，列表可以修改
# print(ret)  # ['h', 'e', 'l', 'l', 'o', ' ', 'y', 'u', 'a', 'n']
# ret[-2] = "A"  # 修改列表倒数第二个元素，a → A
# print(ret)  # ['h', 'e', 'l', 'l', 'o', ' ', 'y', 'u', 'A', 'n']
# ret2 = "".join(ret)  # 把列表拼接回字符串
# print(ret2)  # hello yAn
# name_list = ["rain", "eric", "alvin", "yuans"]
# print("yuan" in name_list)
# print("yuans" in name_list)
#
# a = "duhfyern"
# b = "csdgtgfy"
# print(a + b)
# # 列表内置方法 三个增加三个删除
# name_list = ['fe', 'fr', 'fe', 'fu', 'fi']
# name_list.append("fw")
# print(name_list)
# lst = [10, 20, 30]
# lst.append(40)
# print(lst)
# lst2 = [10, 20, 30]
# lst2.insert(1, 99)
# print(lst2)
# lst3 = [10, 20, 30]
# lst3.extend([50, 60])
# print(lst3)
# lst = [11, 22, 33, 44, 55]
# v1 = lst.pop()
# print("删掉的元素", v1)
# print(lst)
# lst2 = [11, 22, 33, 44, 55]
# v2 = lst2.pop(1)  # 删除下标1的元素22
# print("删掉的元素", v2)
# print(lst2)
# lst3 = [11, 22, 33, 22, 44]
# lst3.remove(22)
# print(lst3)
# lst4 = [11, 22, 33]
# lst4.clear()
# print(lst4)
# lst = [10, 2, 34, 4, 5, 2]
# # 1. sort() 原地升序排序
# lst.sort()
# print(lst)
# # 降序写法1
# lst = [10, 2, 34, 4, 5, 2]
# lst.sort(reverse=True)
# print(lst)
# # sorted() 生成新列表，原列表不变
# lst2 = [10, 2, 34, 4, 5, 2]
# new_lst = sorted(lst2)
# print(lst2)
# print(new_lst)
# # 2. reverse() 原地翻转
# lst3 = [2, 2, 4, 5, 10, 34]
# lst3.reverse()
# print(lst3)
# # 切片[::-1]生成新翻转列表，原列表不变
# lst4 = [2, 2, 4, 5, 10, 34]
# new_lst4 = lst4[::-1]
# print(lst4)
# print(new_lst4)
# # 3. index() 查找第一个匹配元素的下标
# lst5 = [10, 2, 34, 4, 5, 2]
# idx = lst5.index(2)
# print(idx)
# # 4. count() 统计元素出现多少次
# lst6 = [10, 2, 34, 4, 5, 2]
# c = lst6.count(2)
# print(c)
