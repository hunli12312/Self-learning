# def favorite_book(title):
#     print(f"One of my favorite books is {title.title()}.")
#
# favorite_book('Alice in Wonderland')

# def describe_pet(animal_type, pet_name='harry'): #defalut value should always be put in the end.
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet('hamster')
# describe_pet(animal_type='hamster')
#
# describe_pet('hamster', 'willie')
# describe_pet(pet_name='willie', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='willie')

# def make_shirt(size='L', message='I love Python'):
#     print(f"The shirt has size {size} and shows the message {message}.")
#
# make_shirt()
# make_shirt('M',)
# make_shirt('L', 'I really love Python')

# def describe_city(city, country='United States'):
#     print(f"{city} is in {country}.")
#
# describe_city('New York')
# describe_city('Chicago')
# describe_city('London', 'United Kingdom')
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('jimi','hendrix')
# print(musician)

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('jimi', 'hendrix', 27)
# print(musician)
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# while True:
#     print(f"\nPlease tell me your name:")
#     print("Enter 'q' at any time to quit")
#     f_name = input("First name:")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")
#
# def city_country(city,country):
#     return f"{city.title()}, {country.title()}"
#
# print(city_country('chicago','united states'))
#
# def make_album(artist, title, songs=None):
#     album = {'artist': artist, 'title': title, 'songs': songs}
#     return album
#
# while True:
#     print("\nEnter album information.")
#     print("(enter 'q' at any time to quit)")
#
#     artist = input("Artist name: ")
#     if artist == 'q':
#         break
#
#     title = input("Title name: ")
#     if title == 'q':
#         break
#
#     songs = input("Song number (optional): ")
#     if songs == 'q':
#         break
#
#     album = make_album(artist, title, songs)
#     print(album)

# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model:{current_design}")
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_models in completed_models:
#         print(completed_models)
#

# def show_messages(messages):
#     for message in messages:
#         print(message)
#
# def send_messages(messages, sent_messages):
#     while messages:
#         message = messages.pop()
#         print(message)
#         sent_messages.append(message)
#
# messages = ['Hi', 'How are you?', 'Hello, there!']
# sent_messages = []
#
# send_messages(messages[:], sent_messages)
# print(messages)
# print(sent_messages)

# def make_pizza(*toppings):
#     print(toppings)
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushroom', 'green peppers', 'extra cheese')
#
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# user_profile = build_profile('albert', 'einstein', location='princeton', filed='physics')
# print(user_profile)

# def sandwich_ingrediens(*args):
#     print("\nThese are the sandwich ingredients: ")
#     for arg in args:
#         print(f"- {arg}")
#
# sandwich_ingrediens()
# sandwich_ingrediens('salad', 'cucumber', 'chicken')

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# user_profile = build_profile('albert', 'einstein', location='gothenburg', filed='python', mood='great')
# print(user_profile)

# def make_car(manufacturer, model, **car_info):
#     car_info['manufacturer'] = manufacturer
#     car_info['model'] = model
#     return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=False)
# print(car)
