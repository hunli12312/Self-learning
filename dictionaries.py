# alien_0 ={'color':'green'}
#
# print(alien_0['color'])
# print(alien_0['points'])
#
# new_points = alien_0['points']
# alien_0 ={'color':'green','points': 5 }
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
#
# alien_0 = {}
#
# alien_0['color'] = "green"
# alien_0['points'] = 5
# alien_0 = {'color':'green'}
#
# print(f"The alien is {alien_0['color']}.")
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#
# print(f"Original position: {alien_0['x_position']}.")
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
#
# print(f"New position: {alien_0['x_position']}")

# favorite_languages = {
#     'jen':'python',
#     'sarah':'C',
#     'edward':'ruby',
#     'phil':'python'
# }
#
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite programming language is {language}.")
# print(favorite_languages.get('jenny','No such user.'))
# person = {'first_name':'peter', 'last_name': 'parker', 'age': 28, 'city': 'New York'}
#
# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])
# favorite_number = {
#         'peter': 7,
#         'bob': 3,
#         'logan': 5,
#         'john': 7,
#         'lisa': 9
# }
# print(f"Peter's favorite number is {favorite_number['peter']}.")
# print(f"Bob's favorite number is {favorite_number['bob']}.")
# print(f"Logan's favorite number is {favorite_number['logan']}.")
# print(f"John's favorite number is {favorite_number['john']}.")
# print(f"Lisa's favorite number is {favorite_number['lisa']}.")
# glossary = {
#     'string': 'sequence of characters warpped in quotes',
#     'boolean': 'truth values - either True or Flase',
#     'list': 'mutable, ordered sequence of elements',
#     'tuple': 'immutable ,ordered sequence of values',
#     'dictionary': 'collection of a key-value pairs'
# }
# print(f"String:{glossary['string']}.\n")
# print(f"Boolean:{glossary['boolean']}.\n")
# print(f"List:{glossary['list']}.\n")
# print(f"Tuple:{glossary['tuple']}.\n")
# print(f"Dictionary:{glossary['dictionary']}.\n")
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi'
# }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
    #     print(f"Value: {value}")

    # for key, value in user_0.items():
    #     print(f"\nKey: {key}")
    #     print(f"\nValue: {value}")
    # favorite_languages = {
#     'jen':'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
#
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}.")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# glossary = {
#     'string': 'sequence of characters warpped in quotes',
#     'boolean': 'truth values - either True or Flase',
#     'list': 'mutable, ordered sequence of elements',
#     'tuple': 'immutable ,ordered sequence of values',
#     'dictionary': 'collection of a key-value pairs'
# }
#
# for key,value in glossary.items():
#     print(f"{key.title()}:{value}")

# print(f"String:{glossary['string']}.\n")
# print(f"Boolean:{glossary['boolean']}.\n")
# print(f"List:{glossary['list']}.\n")
# print(f"Tuple:{glossary['tuple']}.\n")
# print(f"Dictionary:{glossary['dictionary']}.\n")

# rivers = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'yangtse': 'china'
# }
#
# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country}.")
#
# print("\n")
#
#
# for river in rivers.keys():
#     print(river.title())
#
# print("\n")
#
# for country in rivers.values():
#     print(country.title())

# nesting!

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

# aliens = []
#
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
# for alien in aliens[:5]:
#     print(alien)
#
# print(f"Total number of alien:{len(aliens)}.")

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }
#
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# users = {
#     'aeinstein':{
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton'
#     },
#
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris'
#     }
# }
#
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")
#
# person_0 = {'first_name': 'peter', 'last_name': 'parker', 'age': 28, 'city': 'New York'}
# person_1 = {'first_name': 'marie', 'last_name': 'parker', 'age': 28, 'city': 'New York'}
# person_2 = {'first_name': 'bob', 'last_name': 'parker', 'age': 28, 'city': 'New York'}
#
# people = [person_0, person_1, person_2]
#
# for person in people:
#     for k,v in person.items():
#         print(f"{k}: {v}")
#     print("\n")
#
# pet_0 = {'animal': 'dog', 'owner': 'bob'}
# pet_1 = {'animal': 'cat', 'owner': 'peter'}
#
# pets = [pet_0, pet_1]
#
# for pet in pets:
#     print(f'The pet is a {pet["animal"]}. The owner is {pet["owner"].title()}.')
# favorite_places = {
#     'peter': ['new york', 'london'],
#     'john': ['new york'],
#     'lisa': ['tokio', 'bali', 'toronto']
# }
#
# for name,places in favorite_places.items():
#     print(f"{name.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")
#     print("\n")
favorite_numbers = {
    'peter': [3,7],
    'bob': [3],
    'logan': [3, 5, 8]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
    print("\n")

cities = {
    'new york': {'country': 'united states', 'population': 8.4, 'fact': 'more than 800 languages spokenin NYC'},
    'london': {'country': 'united kingdom', 'population': 8.9, 'fact': 'capital of the UK'},
    'berlin': {'country': 'germany', 'population': 3.6, 'fact': 'was separated by the Berlin wall'}
}
for city, details in cities.items():
    print(f"{city.title()} is located in {details['country'].title()}, has a population of ~{details['population']} million.")
    print(f"Fact about {city.title()}: {details['fact']}\n")