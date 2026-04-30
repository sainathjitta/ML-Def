def add_three_numbers(a, b, c):
    """Add three numbers and return the result."""
    return a + b + c


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
#1234
def find_odd_number567s_in_range_12234(start, end):
    """Return a list of odd numbers in the given range."""
    return [num for num in range(start, end + 1) if num % 2 != 0]


# Example usage
result = add_three_numbers(5, 10, 15)
print(f"Sum: {result}")

# Example usage
odd_numbers = find_odd_number567s_in_range_12234(1, 10)
print(f"Odd numbers in range: {odd_numbers}")

# Example usage
print(f"Is 13 prime? {is_prime(13)}")
print(f"Is 14 prime? {is_prime(14)}")