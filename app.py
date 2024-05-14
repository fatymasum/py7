import random
import math

def square_even_numbers():
    random_numbers = [random.randint(20, 50) for _ in range(5)]
    print("Random Numbers:", random_numbers)
    
    squared_even_numbers = [math.pow(num, 2) for num in random_numbers if num % 2 == 0]
    return squared_even_numbers

print("Squared Even Numbers:", square_even_numbers())
