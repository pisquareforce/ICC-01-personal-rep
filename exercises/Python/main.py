'''
# A review of the Python Language

       1. Classes are blueprints for creating objects;
       2. Objects are instances of classes;
       3. Abstration: Hiding implementation details and exposing only what's necessary;
       4. Method Overloading - Python does not natively support method, but can have similiar
          functionality using default arguments or variable-lenght arguments
       5. Multiple Inheritance: A class can inherit from multiple parant classes;
       6. Polymorphism allows methods in different classes to have the same name but 
          different implementations;
       7. Bundling data(attributes) and methods (functions) together
       8. Method Overriding: a subclass redefines a method from the parent class;
       9. self is a reference to the current instance of the class;
       10. f-string (f"string") in Python
       11. older string formatting % or str.format()
       12. __str()__(self) -> in class 
       13. The __init__ method initializes the construtor;
       14. sys modulde provides tools for interacting with the python interpreter,
           command-line arguments, system, paths and runtime behaviors
          
               if len(sys.argv) > 1:
                   print(f"Arguments: {sys.argv[1:]}")

       15. os -> Files, directories, Environment Varibles and process

      Example: 
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map( insert a function and parameter/s)

       References:
                  https://realpython.com/
                  https://realpython.com/working-with-files-in-python/
                  https://docs.python.org/3/library/filesys.html
                  https://docs.python.org/3/tutorial/inputoutput.html
                  https://devguide.python.org/documentation/start-documenting/
                  https://www.youtube.com/watch?v=IEEhzQoKtQU&ab_channel=CoreySchafer
                  https://www.youtube.com/watch?v=fKl2JW_qrso&ab_channel=CoreySchafer
                  https://www.youtube.com/watch?v=K8L6KVGG-7o&ab_channel=CoreySchafer
  


'''
import time
import os
import sys
import threading
import concurrent.futures


# 1. Example of the composition: 
class CPU:
    def __init__(self, brand):
        self.brand = brand
    # method specifies how the object is converted to a string
    def __str__(self):
        return self.brand                     # Return the size when the CPU is printed

class RAM:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return self.size                      # Return the size when the RAM is printed


class Computer: 
    def __init__(self, cpu_brand, ram_size):
        self.cpu = CPU(cpu_brand)             # Owns the CPU
        self.ram = RAM(ram_size)              # Owns the RAM
    def details(self):
        print(f"Details:\nCPU: {self.cpu}\nRAM: {self.ram}")
# End 1.

# 2. Example of the aggregation:

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car: 
    def __init__(self, make, model, engine): 
        self.make   = make
        self.model  = model
        self.engine = engine   # Car has an engine
    def details(self): 
        print("The car is new;")
# End 2.

# 3. Example of the Encapsulation (Access Modifiers: public, protected and private):
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance             # Private attribute
    def deposit(self, amount):
        self.__balance +=amount
    def get_balance(self):
        return self.__balance
# End 3.

# 4. Example of the inheritance:
class Vehicle: 
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def drive(self): 
        print(f"Driving at {self.speed} km/h.")

class CarNew(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type
    def drive(self):
        print(f"Driving a {self.fuel_type} car at {self.speed} km/h.")

# End 4.

class AddTwoNumbers:
    def __init__(self, a:int, b:int):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b


# Threading 

def do_something():
    print(f"Sleeping 1 second ...")
    time.sleep(1)
    print(f"Done sleeping")

def do_something1(seconds:int):
    print(f"Sleeping {seconds} second ...")
    time.sleep(seconds)
    print(f"Done sleeping")



def testTh1(): 
    # Create two threads:
    t1 = threading.Thread(target=do_something)
    t2 = threading.Thread(target=do_something)

    start = time.perf_counter();

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    finish = time.perf_counter();
    print(f"Finished in {round(finish-start,2)} seconds")

    return

def testTh2():
    threads = []                                                # For pool of the threads
    start = time.perf_counter();
    for _ in range(10):
        t = threading.Thread(target=do_something1, args=[2])
        t.start()
        threads.append(t)
 
    for thread in threads:
        thread.join()
    
    finish = time.perf_counter();
    print(f"Finished in {round(finish-start,2)} seconds")  
    return


# Main function:
def main():
    print("  -- Main function;")
    
    # Composition
    computer = Computer(cpu_brand="Intel Core i7", ram_size="16GB")
    computer.details()

    # Aggregation
    engine = Engine(300)
    car = Car("Toyota", "Supra", engine)
    car.details()

    # Encapsulation: 
    account = BankAccount(100)
    account.deposit(50)
    print("My cash is " + str(account.get_balance()))

    # Inheritance

    vehicle = Vehicle("Generic", 50)
    car = CarNew("Fiat", 50, "petrol")
    vehicle.drive()
    car.drive()

    # 
    test = AddTwoNumbers(10,10)
    print(f"The result is {test.add()}")

    print(" -- Thread exercises;")
    testTh2()
    
  
    print("  -- End;")


if __name__ == "__main__":
    main()
