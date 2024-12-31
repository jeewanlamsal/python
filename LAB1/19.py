#Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and
#methods start() and stop(). The Car class should have instances of Engine and Wheel classes
#as attributes. Implement a method start_car() in the Car class which starts the engine and prints
#"Car started".

class Engine:
    """
    A class to represent a car engine.
    """

    def __init__(self, engine_type):
        """
        Initialize the Engine with its type.

        Parameters:
        engine_type (str): The type of the engine.
        """
        self.type = engine_type

    def start(self):
        """
        Start the engine.
        """
        print(f"Engine of type {self.type} started.")

    def stop(self):
        """
        Stop the engine.
        """
        print(f"Engine of type {self.type} stopped.")


class Wheel:
    """
    A class to represent a car wheel.
    """

    def __init__(self, wheel_type):
        """
        Initialize the Wheel with its type.

        Parameters:
        wheel_type (str): The type of the wheel.
        """
        self.type = wheel_type


class Car:
    """
    A class to represent a car with an engine and wheels.
    """

    def __init__(self, engine_type, wheel_type, num_wheels=4):
        """
        Initialize the Car with an engine and wheels.

        Parameters:
        engine_type (str): The type of the engine.
        wheel_type (str): The type of the wheels.
        num_wheels (int): The number of wheels on the car (default is 4).
        """
        self.engine = Engine(engine_type)
        self.wheels = [Wheel(wheel_type) for _ in range(num_wheels)]

    def start_car(self):
        """
        Start the car by starting its engine.
        """
        self.engine.start()
        print("Car started.")

    def stop_car(self):
        """
        Stop the car by stopping its engine.
        """
        self.engine.stop()
        print("Car stopped.")


# Example usage
car = Car("V8", "Alloy")
car.start_car()  # Output: Engine of type V8 started. Car started.
car.stop_car()   # Output: Engine of type V8 stopped. Car stopped.
