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


# Example usage
result = add_three_numbers(5, 10, 15)
print(f"Sum: {result}")

# Example usage
print(f"Is 13 prime? {is_prime(13)}")
print(f"Is 14 prime? {is_prime(14)}")