def divide(a, b):
    return a / b


def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(divide(10, 2))
    print(calculate_average([1, 2, 3, 4, 5]))
    print(find_max([3, 1, 4, 1, 5, 9]))
    print(factorial(5))
