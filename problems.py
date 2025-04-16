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
                largest_prod_l_r = matrix.iloc[r, c : c + n].prod()  # type: ignore # noqa E203
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


def problem_0012(n: int) -> int:
    max_factors = 0
    seq = 1
    tn = 1
    while max_factors <= n:
        counter = 0

        seq += 1
        tn += seq

        factor = 1
        temp = tn
        while factor < temp:
            if tn % factor == 0:
                counter += 2
                temp = tn / factor
            factor += 1
        if counter > max_factors:
            max_factors = counter
    return tn


def problem_0014(n: int) -> int:
    max_chain = 0
    starting_number = 0

    for i in range(3, n):
        counter = 1
        res = i
        while res != 1:
            if res % 2 == 0:
                res /= 2
            else:
                res = 3 * res + 1
            counter += 1

        if counter > max_chain:
            max_chain = counter
            starting_number = i
    return starting_number


def problem_0015(rows: int, cols: int) -> int:
    n_rows = rows + 1
    n_cols = cols + 1

    g = [[0] * n_cols for _ in range(n_rows)]

    for r in range(n_rows):
        g[r][0] = 1
    for c in range(n_cols):
        g[0][c] = 1

    for c in range(1, n_cols):
        for r in range(1, n_rows):
            g[c][r] = g[c - 1][r] + g[c][r - 1]
    return g[-1][-1]


def problem_0017(n: int) -> int:
    res_all = ""
    for n in range(1, n + 1):
        temp_res = convert_number_to_letter(n)
        res_all += temp_res

    return len(res_all)


def problem_0018() -> int:
    tri = [
        [int(i) for i in line.split()] for line in open("./downloads/0018_matrix.txt")
    ]

    dp = [[0] * len(e) for e in tri]
    dp[0][0] = tri[0][0]

    for line in range(1, len(tri)):
        dp[line][0] = tri[line][0] + dp[line - 1][0]
        dp[line][-1] = tri[line][-1] + dp[line - 1][-1]

    for line in range(2, len(tri)):
        for e in range(line):
            dp[line][e] = tri[line][e] + max(dp[line - 1][e - 1], dp[line - 1][e])

    return max(dp[-1])


def problem_0019() -> int:
    date = {
        "day": 1,
        "month": 1,
        "year": 1900,
        "weekday": 1,
    }
    counter = 0
    while date["year"] <= 2000:
        if date["month"] in [4, 6, 9, 11]:
            if date["day"] == 30:
                date["day"] = 1
                date["month"] += 1
            else:
                date["day"] += 1
        elif date["month"] in [1, 3, 5, 7, 8, 10, 12]:
            if date["day"] == 31:
                date["day"] = 1
                if date["month"] == 12:
                    date["month"] = 1
                    date["year"] += 1
                else:
                    date["month"] += 1
            else:
                date["day"] += 1
        else:
            if date["year"] % 4 == 0:
                if ((date["year"] % 100 == 0) & (date["year"] % 400 == 0)) | (
                    date["year"] % 100 != 0
                ):
                    if date["day"] == 29:
                        date["day"] = 1
                        date["month"] += 1
                    else:
                        date["day"] += 1
                else:
                    if date["day"] == 28:
                        date["day"] = 1
                        date["month"] += 1
                    else:
                        date["day"] += 1
            else:
                if date["day"] == 28:
                    date["day"] = 1
                    date["month"] += 1
                else:
                    date["day"] += 1

        if date["weekday"] == 7:
            date["weekday"] = 1
        else:
            date["weekday"] += 1

        if (date["day"] == 1) & (date["weekday"] == 7) & (date["year"] >= 1901):
            counter += 1
    return counter


def problem_0020(n: int) -> int:
    prod = 1

    for i in range(1, n + 1):
        prod *= i

    sum_dig = 0
    for i in str(prod):
        sum_dig += int(i)
    return sum_dig


def problem_0021(n: int) -> int:
    amicable_numbers = []
    i = 1
    while i < n:
        if i not in amicable_numbers:
            temp_sum_1 = sum(get_all_factors(i))
            if i != temp_sum_1:
                temp_sum_2 = sum(get_all_factors(temp_sum_1))
                if i == temp_sum_2:
                    amicable_numbers.extend([i, temp_sum_1])
        i += 1
    return sum(amicable_numbers)


def problem_0022() -> int:
    names = open("./downloads/0022_names.txt").read().split(sep=",")
    names = [i.replace('"', "") for i in names]
    names.sort()

    cumsum_all = 0
    for i in range(len(names)):
        cumsum = 0
        for letter in names[i]:
            cumsum += ord(letter) - 64
        cumsum_all += cumsum * (i + 1)
    return cumsum_all


def problem_0023() -> int:
    abundant_numbers = []
    for i in range(12, 28123 + 1):
        sum_divisors = sum(get_all_factors(i))
        if sum_divisors > i:
            abundant_numbers.append(i)

    posible_sums_abundant_numbers = []
    for i in range(len(abundant_numbers)):
        for j in range(len(abundant_numbers)):
            temp_sum = abundant_numbers[i] + abundant_numbers[j]
            if temp_sum <= 28123:
                posible_sums_abundant_numbers.append(temp_sum)
    posible_sums_abundant_numbers = list(set(posible_sums_abundant_numbers))

    int_filtered = [
        e for e in range(1, 28123 + 1) if e not in posible_sums_abundant_numbers
    ]
    return sum(int_filtered)


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
def convert_number_to_letter(n: int) -> str:
    number_dict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    dec_dict = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    n_str = str(n)

    if len(n_str) == 1:
        n_str = "000" + n_str
    elif len(n_str) == 2:
        n_str = "00" + n_str
    elif len(n_str) == 3:
        n_str = "0" + n_str
    elif len(n_str) > 4:
        raise ValueError("max is a four-digit number")

    res = ""
    if int(n_str[0]) > 0:
        res += number_dict[int(n_str[0])]
        res += "thousand"

    if int(n_str[1]) > 0:
        res += number_dict[int(n_str[1])]
        res += "hundred"

    if (int(n_str[1]) > 0) & (int(n_str[2:4]) > 0):
        res += "and"

    if int(n_str[2:4]) > 0:
        if int(n_str[2:4]) <= 19:
            res += number_dict[int(n_str[2:4])]
        else:
            res += dec_dict[int(n_str[2])]
            if int(n_str[3]) > 0:
                res += number_dict[int(n_str[3])]

    return res


def generate_primes(n: int) -> list:
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p, isprime in enumerate(sieve) if isprime]


def get_all_factors(n: int) -> list:
    all_factor = [1]
    factor = 2
    temp = n
    while factor < temp:
        if n % factor == 0:
            temp = n / factor
            all_factor.extend([factor, int(temp)])
        factor += 1
    all_factor = list(set(all_factor))
    all_factor.sort()
    return all_factor


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
