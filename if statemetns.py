# # # # cars = ['audi', 'bmw', 'subaru', 'toyota']
# # # #
# # # # for car in cars:
# # # #     if car == 'bmw':
# # # #         print(car.upper())
# # # #     else:
# # # #         print(car.title())
# # #
# # # age = 19
# # #
# # # print(age < 21)
# # # print(age <= 21)
# # #
# # # print(age > 21)
# # # # print(age >= 21)
# # # #
# # # # print(age <= 21 or age == 19)
# # # # print(age <= 21 and age >= 1)
# # # requested_toppings = ['mushrooms', 'onions', 'pinapple']
# # #
# # # print('pepperoni' not in requested_toppings)
# # # print('onions' in requested_toppings)
# # banned_users = ['andrew', 'carolina', 'david']
# # user = 'marie'
# #
# # if user not in banned_users:
# #     print(f"{user.title()}, you can post a response if you wish.")
#
# car = 'subaru'
# print("is car =='subaru'? I predict Ture.")
# print(car == 'subaru')
#
# car = "Audi"
# print(car.lower() == "audi")
# age = 17
# if age >= 18:
#     print("Yes, you are age 18.\nHave you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.\nPlease register to vote when you are 18 or older.")
# alien_color = 'yellow'
#
# if alien_color == 'green':
#     print("You earned 5 points.")
# elif alien_color == 'yellow':
#     print("You earned 15 points.")
# else:
#     print("You earned 10 points.")

# age = 99
#
# if age < 2:
#     print("The person is a baby.")
# elif age < 4:
#     print("The person is a toddler")
# elif age < 13:
#     print("The person is a kid.")
# elif age < 20:
#     print("The person is a teenager.")
# elif age < 65:
#     print("The person is a adult.")
# elif age >= 65:
#     print("The person is an elder.")
#
# favorite_fruits = ['kiwi', 'orange', 'apple']
#
# if 'kiwi' in favorite_fruits:
#     print("You really like kiwis.")
# if 'banana' in favorite_fruits
#     print("You really like bananas.")
# #
# requests_toppings = ["extra cheese"]
# if requests_toppings:
#     for requests_topping in requests_toppings:
#         if requests_topping == 'green peppers':
#             print("Sorry, we are out of green peppers right now.")
#         else:
#             print(f"Adding {requests_topping}")
# else:
#     print("Are you sure want a plain pizza?")
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
#
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}")
# print("\nFinished making your pizza!")
# usernames = ['john', 'adam', "admin", "logan", 'paul']
# if usernames:
#     for username in usernames:
#         if username == "admin":
#             print(f"Hello {username.title()}, would you like to see a status report?")
#         else:
#             print(f"Hello {username.title()}, thank you for logging in again.")
# else:
#     print("We need to find some users!")
# current_users = ['john', 'adam', 'admin', 'logan', 'paul']
#
# new_users = ['johan', 'peter', 'kai', 'adam', 'bob']
#
# for new_user in new_users:
#     if new_user in current_users:
#         print(f"Hello, {new_user.title()}. The username is already in use, please use a different one.")
#     else:
#         print(f'Hello,{new_user.title()}. This username is available.')
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")