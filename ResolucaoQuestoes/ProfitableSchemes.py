class Solution:
    def profitableSchemes(
        self,
        n: int,
        minProfit: int,
        group: list[int],
        profit: list[int]
    ) -> int:
        MOD = 1_000_000_007
        G = len(group)

        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            for people in range(n, g - 1, -1):
                for prof in range(minProfit, -1, -1):
                    new_prof = min(minProfit, prof + p)
                    dp[people][new_prof] += dp[people - g][prof]
                    dp[people][new_prof] %= MOD

        return sum(dp[people][minProfit] for people in range(n + 1)) % MOD
