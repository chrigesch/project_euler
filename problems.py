import pandas as pd

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


def problem_0003(number: int) -> list:
    divisor = 2
    divisors = []
    while divisor <= number:
        if number % divisor == 0:
            number //= divisor
            divisors.append(divisor)
        else:
            divisor += 1 if divisor == 2 else 2
    return divisors


def problem_0004() -> int:
    largest_palindrome = 11
    for first in range(999, 100, -1):
        for second in range(999, 100, -1):
            product = first * second
            if is_palindrome(product) & (product > largest_palindrome):
                largest_palindrome = product
    return largest_palindrome


def problem_0005(n: int) -> int:
    primes = generate_primes(n)

    cum_prod = 1
    for prime in primes:
        max_factors = 1
        if 2 * prime < n:
            for i in range(prime * 2, n + 1):
                i_temp = i
                counter = 0
                while i_temp % prime == 0:
                    i_temp /= prime
                    counter += 1
                if counter > max_factors:
                    max_factors = counter
        cum_prod *= prime**max_factors

    return cum_prod


def problem_0006(n: int) -> int:
    sum_of_sq = 0
    for i in range(1, n + 1):
        sum_of_sq += i**2
    sq_of_sum = ((n**2 + n) / 2) ** 2

    return int(sq_of_sum - sum_of_sq)


def problem_0008(n: int) -> int:
    digits = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )

    greatest_product = 0
    for i in range(n - 1, len(digits)):
        temp_digits_str = digits[i - n : i]  # noqa E203
        temp_product = 1
        for d in temp_digits_str:
            temp_product *= int(d)
        if temp_product > greatest_product:
            greatest_product = temp_product
    return greatest_product


def problem_0009():
    for a in range(1, 998):
        for b in range(a + 1, 998):
            for c in range(b + 1, 998):
                if (a**2 + b**2 == c**2) & (a + b + c == 1000):
                    return [a, b, c]


def problem_0010(n: int) -> int:
    primes = generate_primes(n)
    cumsum = 0
    for p in primes:
        cumsum += p
    return cumsum


def problem_0011(matrix: pd.DataFrame, n: int) -> int:

    largest_prod = 0

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            # right & left
            if c < len(matrix) - n:
                largest_prod_l_r = matrix.iloc[r, c : c + n].prod()  # noqa E203
            # up & down
            if r < len(matrix) - n:
                largest_prod_u_d = matrix.iloc[r : r + n, c].prod()  # noqa E203
            # diag ul_dr & diag ur_dl
            if (c < len(matrix) - n) & (r < len(matrix) - n):
                largest_prod_ul_dr = (
                    matrix.iloc[r, c]
                    * matrix.iloc[r + 1, c + 1]  # type: ignore
                    * matrix.iloc[r + 2, c + 2]
                    * matrix.iloc[r + 3, c + 3]
                )
                largest_prod_ur_dl = (
                    matrix.iloc[r, c + n - 1]
                    * matrix.iloc[r + 1, c + n - 2]  # type: ignore
                    * matrix.iloc[r + 2, c + n - 3]
                    * matrix.iloc[r + 3, c + n - 4]
                )

            temp_max = max(
                largest_prod_l_r,  # type: ignore
                largest_prod_u_d,  # type: ignore
                largest_prod_ul_dr,  # type: ignore
                largest_prod_ur_dl,  # type: ignore
            )

            if temp_max > largest_prod:
                largest_prod = temp_max

    return largest_prod


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
def generate_primes(n: int) -> list:
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p, isprime in enumerate(sieve) if isprime]


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
