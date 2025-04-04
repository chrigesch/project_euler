# https://projecteuler.net/archives


def problem_0001(below: int) -> int:
    results = []
    for i in range(below):
        if (i % 3 == 0) | (i % 5 == 0):
            results.append(i)
    return sum(results)


def problem_0002(below: int) -> int:
    results = [1, 2]

    while results[-1] < below:
        results.append(sum([results[-1], results[-2]]))
    results_even = [e for e in results if e % 2 == 0]
    return sum(results_even)


def problem_0003(number: int) -> int:
    divisor = 2
    divisors = []
    while divisor <= number:
        if number % divisor == 0:
            number //= divisor
            divisors.append(divisor)
        else:
            divisor += 1 if divisor == 2 else 2
    return divisors[-1]


def problem_0004() -> int:
    largest_palindrome = 11
    for first in range(999, 100, -1):
        for second in range(999, 100, -1):
            product = first * second
            if is_palindrome(product) & (product > largest_palindrome):
                largest_palindrome = product
    return largest_palindrome


def problem_0009():
    for a in range(1, 998):
        for b in range(a + 1, 998):
            for c in range(b + 1, 998):
                if (a**2 + b**2 == c**2) & (a + b + c == 1000):
                    return [a, b, c]


def problem_0027() -> list:
    highest_n = -1
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            for n in range(100):
                result = n * n + a * n + b
                if is_prime(result) is False:
                    break
                if n > highest_n:
                    highest_n = n
                    results = [a, b, n, a * b]
    return results


def problem_0081(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    dp[0][0] = grid[0][0]

    # Initialize first row and column
    for i in range(1, n):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
        dp[0][i] = grid[0][i] + dp[0][i - 1]

    # Fill the rest of the table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


####################
# Helper functions #
####################
def is_palindrome(value: int) -> bool:
    value_str = str(value)
    length = len(value_str)
    if length % 2 != 0:
        return False
    for i in range(1, int(length / 2) + 1):
        if value_str[i - 1] != value_str[-i]:
            return False
    return True


def is_prime(n) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
