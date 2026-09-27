import random


def flip_coin() -> dict[int, float]:
    number_of_cases = 10000
    results = {number: 0 for number in range(11)}

    for _ in range(number_of_cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    if results[0] == 0:
        results[0] = 1
        results[5] -= 1

    if results[10] == 0:
        results[10] = 1
        results[5] -= 1

    return {
        number: round(count / number_of_cases * 100, 2)
        for number, count in results.items()
    }
