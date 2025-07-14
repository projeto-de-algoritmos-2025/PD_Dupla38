from bisect import bisect_right

class Solution:
    def jobScheduling(self, ini, fim, lucro):
        n = len(ini)

        trabalhos = sorted(zip(ini, fim, lucro), key=lambda x: x[1])
        ini, fin, val = zip(*trabalhos)

        def calcular_p():
            p = [0] * n
            for j in range(n):
                i = bisect_right(fin, ini[j]) - 1
                p[j] = i
            return p

        p = calcular_p()

        memo = [-1] * (n + 1)

        def max_lucro(j):
            if j == -1:
                return 0
            if memo[j] != -1:
                return memo[j]
            incluir = val[j] + max_lucro(p[j])
            excluir = max_lucro(j - 1)
            memo[j] = max(incluir, excluir)
            return memo[j]

        return max_lucro(n - 1)
