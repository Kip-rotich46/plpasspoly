# Assignment 1: Design Your Own Class - Smartphone with Inheritance

class Smartphone:
    def __init__(self, brand, model, color, storage):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage

    def display_info(self):
        return f'{self.brand} {self.model} - Color: {self.color}, Storage: {self.storage}GB'

    def make_call(self, number):
        return f'Calling {number}...'

    def take_photo(self):
        return 'Taking a photo...'


class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, color, storage, camera_quality):
        super().__init__(brand, model, color, storage)
        self.camera_quality = camera_quality

    def take_photo(self):
        return f'Taking a {self.camera_quality}MP photo...'

# Creating objects of Smartphones
phone1 = Smartphone('Samsung', 'Galaxy S21', 'Phantom Gray', 128)
phone2 = CameraSmartphone('Apple', 'iPhone 13 Pro', 'Graphite', 256, 12)

# Displaying information of smartphones
print(phone1.display_info())  
print(phone2.display_info())

# Calling methods of smartphones
print(phone1.make_call('123-456-7890'))  
print(phone2.take_photo())  

# Activity 2: Polymorphism Challenge with Vehicles (Car, Plane, Boat)

class Vehicle:
    def move(self):
        pass  # Base method to be overridden by subclasses

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Creating instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Calling the move() method on each vehicle
print(car.move())  # Output: Driving 🚗
print(plane.move())  # Output: Flying ✈️
print(boat.move())  # Output: Sailing ⛵
