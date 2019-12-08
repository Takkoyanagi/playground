class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            if n == 1:
                return x
            else:
                return x * self.myPow(x, n-1)
        elif n < 0:
            if n == -1:
                return (1/x)
            else:
                return (1/x) * self.myPow(x, n+1)


s = Solution()
print(s.myPow(2, -5))
