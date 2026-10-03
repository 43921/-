# def st(s, t):
#     from collections import defaultdict
#     d = defaultdict(int)
#     for c in s:
#         d[c] += 1
#     for c in t:
#         d[c] -= 1
#         if d[c] < 0:
#             return False
#     return True
#
#
# if __name__ == "__main__":
#     s = "anagram"
#     t = "nagaram"
#     print(st(s, t))
#
# def isAnagram(s, t):
#     record = [0] * 26
#     for i in s:
#         record[ord(i) - ord("a")] += 1
#     for i in t:
#         record[ord(i) - ord("a")] -= 1
#     for num in record:
#         if num != 0:
#             return False
#     return True
#
#
# if __name__ == "__main__":
#     s = input()
#     t = input()
#     print(isAnagram(s, t))
###
# #
# from collections import defaultdict
#
#
# def canConstruct(ransomNote, magazine):
#     d = defaultdict(int)
#     for i in magazine:
#         d[i] += 1
#     for i in ransomNote:
#         d[i] -= 1
#     for _ in d.values():
#         if _ < 0:
#             return False
#     return True
#
#
# if __name__ == "__main__":
#     r = input()
#     m = input()
#     print(canConstruct(r, m))
