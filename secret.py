import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]
