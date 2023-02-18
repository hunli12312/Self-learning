# message = input("Tell me something, and I will repeat it back to you:")
# print(message)
# name = input("Please enter your name:")
# print(f"\n hello,{name.title()}")

# prompt = "If you tell us who are, we can personalize the message you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print(f"\nHello,{name}!")

# height = input("How tall are you, in inches?")
# height = int(height)
#
# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou are not tall enough to ride!")
#
# number = input("Enter a number, and I'll tell you if it's even or odd:")
# number = int(number)
#
# if number % 2 == 0:
#     print(f"\n The number {number} is even.")
# else:
#     print(f"The number {number} is odd.")
# rental_car = input("What kind of rental car would you like?")
# print(f"Let me see if I can find you a {rental_car}.")

# people = input("How many people are in your dinner group?")
# people = int(people)
#
# if people > 8:
#     print("Sorry, you'll have to wait for a table.")
# else:
#     print("We have a table ready.")

# number = input("Please provide a number:")
# number = int(number)
#
# if number % 10 == 0:
#     print(f"The number {number} is a multiple of 10.")
# else:
#     print(f"The number {number} is not a multiple of 10.")

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
#
# while message != 'quit':
#     message = input(prompt)
#     if message != "quit":
#         print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

# active = True
#
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)

# prompt = "Which pizza topping would you like?"
# prompt += "(Type 'quit' tp stop adding toppings)"
#
# while True:
#     topping = input(prompt)
#
#     if topping == 'quit':
#         break
#     else:
#         print(f"Adding {topping} to your pizza.")
#
# prompt = "\nHow old are you?"
# prompt = "\n(Type 'quit' to stop.)"
#
# active = True
#
# while active:
#     age = input(prompt)
#
#     if age == 'quit':
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age < 13:
#             price = 10
#         else:
#             price = 15
#
#         print(f"The ticket price is ${price}.")

# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     print(pets)
#     pets.remove('cat')
#
# print(pets)

# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is your name?")
#     response = input("Which mountain would you like to climb someday?")
#
#     responses[name] = response
#
#     repeat = input("Would you like to let another person respond? (yes/no)")
#     if repeat == 'no':
#         polling_active = False
# print("\n---Poll Results---")
# for name, response in responses.items():
#     print(f"{name} would you like to climb {response}?")
#
# sandwich_orders = ['pastrami','tuna', 'chicken','pastrami', 'pastrami']
# finished_sandwiches = []
#
# print("Sorry, we ran out of Pastrami.")
#
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich} sandwich.")
#
#     finished_sandwiches.append(sandwich)
#
# print("---Finished Sandwiches---")
# for sandwich in finished_sandwiches:
#     print(f"We made you {sandwich} sandwich.")

# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is your name?")
#     response = input("If you could visit one place in the world, where would you go?")
#
#     responses[name] = response
#
#     repeat = input("Would you like to let another person respond?(yes/no)")
#     if repeat == 'no':
#         polling_active = False
#
# print("---Pole Results---")
# for name,response in responses.items():
#     print(f"{name.title()} would like to visit {response}.")