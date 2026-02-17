import random

def generate_random_numbers(count: int, min_val: int = 1, max_val: int = 100) -> list:
    """Generate a list of random numbers."""
    return [random.randint(min_val, max_val) for _ in range(count)]

def calculate_statistics(numbers: list) -> dict:
    """Calculate basic statistics for a list of numbers."""
    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "count": len(numbers)
    }

if __name__ == "__main__":
    random_nums = generate_random_numbers(10)
    print(f"Random numbers: {random_nums}")
    
    stats = calculate_statistics(random_nums)
    print(f"Statistics: {stats}")