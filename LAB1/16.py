#Define a class Vehicle with attributes make and model, and a method drive() which prints
#"Driving the [make] [model]". Then, create a subclass Car that inherits from Vehicle and overrides
#the drive() method to print "Driving the [make] [model] car".
class Vehicle:
    """
    A class to represent a generic vehicle.
    """

    def __init__(self, make, model):
        """
        Initialize a Vehicle with make and model.

        Parameters:
        make (str): The make of the vehicle.
        model (str): The model of the vehicle.
        """
        self.make = make
        self.model = model

    def drive(self):
        """
        Print a message indicating that the vehicle is being driven.
        """
        print(f"Driving the {self.make} {self.model}")


class Car(Vehicle):
    """
    A subclass of Vehicle representing a car.
    """

    def drive(self):
        """
        Print a message indicating that the car is being driven.
        """
        print(f"Driving the {self.make} {self.model} car")


# Example usage
vehicle = Vehicle("Toyota", "Corolla")
vehicle.drive()  # Output: Driving the Toyota Corolla

car = Car("Honda", "Civic")
car.drive()  # Output: Driving the Honda Civic car
