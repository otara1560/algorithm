import io
import sys

INF = 1 << 60

_INPUT = """\
ABADBDADCB
DBACADBADACC
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)

    dp = [[0] * (T_len + 1) for _ in range(S_len + 1)]

    for i in range(S_len + 1):
        for j in range(T_len + 1):
            if i > 0 and j > 0 and S[i - 1] == T[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])

    print(dp[S_len][T_len])
if __name__ == "__main__":
    main()