import random
import datetime

def generate_random_data(count=10):
    """Generate random data with timestamps"""
    data = []
    for i in range(count):
        data.append({
            'id': i + 1,
            'value': random.randint(1, 100),
            'timestamp': datetime.datetime.now().isoformat(),
            'name': f'item_{random.choice("abcdefghij")}'
        })
    return data

def main():
    random_data = generate_random_data(5)
    for item in random_data:
        print(item)

if __name__ == '__main__':
    main()