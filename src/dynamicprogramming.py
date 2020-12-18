def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    dp = (n + 1) * [0]
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        # from the i-1th step we take 1 step to get to ith step
        # from the i-2th step we take 2 step to get to ith step
        # if there are dp[i-1] ways to reach i-1th step
        # and there are dp[i-2] ways to reach i-2th step
        # hence there are dp[i-1] + dp[i-2] ways to reach ith step
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Uplift
def compute_sum(num1: list, num2: int) -> list:
    res = []
    if num1:
        carry = 0
        num1 = reversed(num1)
        for i in num1:
            r = num2 % 10
            q = num2 // 10
            res.append((i + r + carry) % 10)
            carry = (i + r) // 10
            num2 = q

    while num2 > 0:
        r = num2 % 10
        num2 = num2 // 10
        res.append(r)

    return list(reversed(res))


if __name__ == "__main__":
    num1 = [1, 9]
    num2 = 123
    print(compute_sum(num1, num2))