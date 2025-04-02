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
