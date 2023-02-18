# class Restaurant:
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"The restaurant is called {self.restaurant_name}.")
#         print(f"The cuisine type is {self.cuisine_type}.")
#
#     def open_restarurant(self):
#         print(f"The restaurant {self.restaurant_name} is open.")
#
# restaurant = Restaurant('Brasserie', 'French')
# print(f"Restaurant name: {restaurant.restaurant_name}.")
# print(f"Restaurant cuisine: {restaurant.cuisine_type}.")
# restaurant.describe_restaurant()
# restaurant.open_restarurant()

# class User:
#
#     def __init__(self, first_name, last_name, location, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.location = location
#         self.age = age
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f"The user name is {self.first_name} {self.last_name}.")
#         print(f"The user is {self.age} years old and lives in {self.location}.")
#
#     def greet_user(self):
#         print(f"Hello, {self.first_name} {self.last_name}!")
#
# class Admin(User):
#     def __init__(self, first_name, last_name, location, age, privileges):
#         super().__init__(first_name, last_name, location, age)
#         self.privileges = Privileges(privileges)
#
# class Privileges:
#     def __init__(self, privileges):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print("Privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege}")
#
# admin_1 = Admin('Adam', 'Admin', 'NYC', 28, ['can add post', 'can delete post', 'can ban user'])
# admin_1.privileges.show_privileges()
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# user_1 = User('Bob', 'the Builder', 'London', '42')
# user_1.describe_user()
# user_1.greet_user()


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
# car = Car('auti', 'a4', 2019)
# car.odometer_reading = 23
# car.read_odometer()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
#
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restarurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")

    def set_number_served(self, guests):
        self.number_served = guests

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, restaurant_type, flavors):
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = flavors

    def display_flavor(self):
        print(f"The flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# ice_cream = IceCreamStand('ice cream parlor', 'ice cream', ['chocolate', 'banana'])
# ice_cream.display_flavor()
# restaurant = Restaurant('Brasserie', 'French')
# print(f"Restaurant name: {restaurant.restaurant_name}.")
# print(f"Restaurant cuisine: {restaurant.cuisine_type}.")
# restaurant.describe_restaurant()

