# # 双指针法 例子找两数之和等于目标值
# nums = [2, 3, 4, 7, 11]
# target = 9
# left = 0
# right = len(nums) - 1
# while left < right:
#     s = nums[left] + nums[right]
#     if s == target:
#         print(nums[left], nums[right])
#         break
#     elif s < target:
#         left += 1
#     else:
#         right -= 1

# 二分查找 例子在数组里找目标值
# nums = [1, 2, 3, 8, 10, 22, 43]
# left = 0
# right = len(nums) - 1
# target = 43
# while left <= right:
#     mid = (right + left) // 2
#     if nums[mid] == target:
#         print(mid)
#         break
#     elif nums[mid] > target:
#         right = mid - 1
#     else:
#         left = mid + 1
# else:
#     print(-1)

# 三数之和
# class Solution:
#     def threeSum(self, nums):
#         result = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             left = i + 1
#             right = len(nums) - 1
#             while left < right:
#                 sum_ = nums[i] + nums[left] + nums[right]
#                 if sum_ == 0:
#                     result.append([nums[i], nums[left], nums[right]])
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#                 elif sum_ > 0:
#                     right -= 1
#                 else:
#                     left += 1
#         return result
#
#
# sol = Solution()
# print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
