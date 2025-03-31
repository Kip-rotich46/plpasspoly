# Polymorphism and Class Design in Python

## Overview
This project demonstrates the implementation of **Polymorphism** and **Inheritance** in Python through the creation of two different themes:

1. **Smartphone Class**:
   - A basic class representing a smartphone, with methods to display information, make calls, and take photos. 
   - An inherited class (`CameraSmartphone`) extends the base class, adding a specialized feature for taking high-quality photos based on camera specifications.

2. **Vehicle Classes**:
   - This section demonstrates **Polymorphism**, where three vehicle classes (`Car`, `Plane`, and `Boat`) each implement the same `move()` method but with different behaviors based on the vehicle type.

## Classes and Functions

### 1. **Smartphone Class**:

- **Attributes**:
  - `brand`: The brand of the smartphone.
  - `model`: The model of the smartphone.
  - `color`: The color of the smartphone.
  - `storage`: The storage capacity of the smartphone (in GB).
  
- **Methods**:
  - `display_info()`: Displays the brand, model, color, and storage of the smartphone.
  - `make_call(number)`: Simulates making a phone call to a given number.
  - `take_photo()`: Simulates taking a photo.

### 2. **CameraSmartphone Class** (Inheritance):

- **Attributes**:
  - `camera_quality`: The camera quality in megapixels.
  
- **Methods**:
  - `take_photo()`: Overridden to include camera quality in the photo-taking simulation.

### 3. **Vehicle Classes** (Polymorphism):

- **Base Class**:
  - `Vehicle`: An abstract class with a `move()` method that is intended to be overridden by subclasses.
  
- **Subclasses**:
  - `Car`: Overrides `move()` to simulate "Driving 🚗".
  - `Plane`: Overrides `move()` to simulate "Flying ✈️".
  - `Boat`: Overrides `move()` to simulate "Sailing ⛵".

## How to Run

1. Copy the Python code into a file, for example, `polymorphism_and_class_design.py`.
2. Run the file in your Python environment (Python 3.x).
3. Observe the output, which will display information about the smartphone objects and the different `move()` behaviors for each vehicle.

```bash
python polymorphism_and_class_design.py
```

## Output Example:

```
Samsung Galaxy S21 - Color: Phantom Gray, Storage: 128GB
Apple iPhone 13 Pro - Color: Graphite, Storage: 256GB
Calling 123-456-7890...
Taking a 12MP photo...
Driving 🚗
Flying ✈️
Sailing ⛵
```

## Key Concepts Demonstrated:
- **Polymorphism**: The same method name (`move()`) is implemented in different ways for different vehicle types.
- **Inheritance**: The `CameraSmartphone` class inherits from the `Smartphone` class and overrides the `take_photo()` method.
- **Class Design**: Creation of classes with attributes and methods to represent real-world objects and behaviors.
