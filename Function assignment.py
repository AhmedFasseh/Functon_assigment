def sum_list(numbers):
    return sum(numbers)
numbers = [5, 7, 9]
print((sum_list(numbers)))  # Output: 21

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
num = 3
print(factorial(num))  # Output: 6
