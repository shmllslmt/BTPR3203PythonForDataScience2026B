import math
import random
from datetime import datetime

radius = 5
area = math.ceil(math.pi * math.pow(radius, 2))
print(f"The area of a circle with radius {radius} is {math.ceil(area)} (rounded up to higher integer)")
print(f"The area of a circle with radius {radius} is {math.floor(area)} (rounded down to lower integer)")

dice_roll = random.randint(1, 6)
print(f"You rolled a {dice_roll}.")

current_time = datetime.now()
print(f"The current date and time is: {current_time}")
print(f"The current date and time is: {current_time.strftime('%d-%m-%Y %H:%M')}")
print(f"The current year is : {current_time.year}")
print(f"The current month is: {current_time.month}")
print(f"The current day is  : {current_time.day}")

def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
min_num, max_num, avg_num = get_stats(numbers)
print(f"Min: {min_num}, Max: {max_num}, Average: {avg_num}")