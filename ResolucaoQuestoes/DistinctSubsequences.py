class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m: 
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  

        for ch_s in s:
            for j in range(n, 0, -1):
                if ch_s == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
