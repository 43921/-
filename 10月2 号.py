# 哈希单向 加密双向
# 哈希冲突的时候：封闭寻址法(链表) 开放寻址法(线性探测，双重哈希，布谷鸟哈希)
# 哈希算法：MD5 SHA
#
# 力扣求两数之和 循环找下标和数值 在就返回 不在存
# def twosum(nums, target):
#     hashmap = {}
#     for idx, num in enumerate(nums):
#         need = target - num
#         if need in hashmap:
#             return [hashmap[need], idx]
#         hashmap[num] = idx #没有这个数字就存一下，有就更新了下标
#     return []
#
#
# if __name__ == "__main__":
#     nums = [2, 7, 11, 15]
#     target = 9
#     result = twosum(nums, target)
#     print(result)
#
# enumerate python内置函数给列表每一项自动配上序号
# for num in [2, 7, 11, 15]:
#     print(num)
# for idx, num in enumerate([2, 7, 11, 15]):
#     print(f"下标：{idx},数值：{num}")
