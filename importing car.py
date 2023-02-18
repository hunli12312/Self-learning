# from Classes import Restaurant
#
# french_restaurant = Restaurant('Brasserie', 'Frence')
#
# french_restaurant.describe_restaurant()
# from random import randint
#
# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def roll_die(self):
#         print(randint(1, self.sides))
#
# die = Die()
# for _ in range(0,10):
#     die.roll_die()

# from random import choice
#
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
#
# my_ticket = choice(values)
#
# for i in range(0, len(values)):
#     print(choice(values))
#     if values[i] == my_ticket:
#         print(f"It took {i+1} iterations to get the tickets {values[i]}")
#         break
# print("The following tickets have won a prize:")
# for _ in range (0,4):
#     print(choice(values))
import random

# Set the seed to a specific value
random.seed(42)

# Generate a set of random integers using the randint function
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Print the set of random numbers
print(random_numbers)
