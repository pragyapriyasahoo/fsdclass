import random

def get_random_greeting():
    greetings = ["Hello", "Hi", "Hey", "Greetings", "Welcome"]
    return random.choice(greetings)

def generate_random_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

if __name__ == "__main__":
    print(f"{get_random_greeting()}!")
    print(f"Your random number is: {generate_random_number()}")