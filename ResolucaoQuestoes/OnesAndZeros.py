class Solution:
    def findMaxForm(self, strs, m, n):
        contagem = []
        for s in strs:
            zeros = s.count('0')
            uns = len(s) - zeros
            contagem.append((zeros, uns))
        
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        
        for i in range(1, len(strs)+1):
            z, u = contagem[i-1]
            for zeros_disp in range(m+1):
                for uns_disp in range(n+1):
                    if z > zeros_disp or u > uns_disp:
                        dp[i][zeros_disp][uns_disp] = dp[i-1][zeros_disp][uns_disp]
                    else:
                        dp[i][zeros_disp][uns_disp] = max(
                            dp[i-1][zeros_disp][uns_disp],
                            1 + dp[i-1][zeros_disp - z][uns_disp - u]
                        )
        
        return dp[len(strs)][m][n]

