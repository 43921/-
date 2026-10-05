class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            sum_sq = 0
            # 计算每一位的平方和
            while n > 0:
                digit = n % 10
                sum_sq += digit * digit
                n = n // 10
            n = sum_sq
            if n == 1:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(2))
    num = int(input("请输入数字判断是否快乐数："))
    print(sol.isHappy(num))
