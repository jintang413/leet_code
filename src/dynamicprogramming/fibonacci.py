def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_rec_memo(n, memo):
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = fib_rec_memo(n - 1, memo) + fib_rec_memo(n - 2, memo)
    return memo[n]


def fib_dp(n):
    if n == 0 or n == 1:
        return 1
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[-1]


print(fib_rec(5))
print(fib_rec(6))
# print(fib_rec(50))
print(fib_rec_memo(50, {}))
print(fib_dp(50))
