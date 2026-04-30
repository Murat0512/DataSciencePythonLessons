"""Decorators are a powerful tool in Python that allow you to 
modify the behavior of functions or classes without changing 
their source code. They are often used to add functionality, 
such as logging, timing, or access control, to existing functions.
A decorator is a function that takes another function as an 
argument and returns a new function that typically extends 
the behavior of the original function. The syntax for using a 
decorator is as follows:

@decorator

def function_to_decorate():
    # function body
When a function is decorated, the decorator function is called with the 
original function as an argument, and it returns a new function that replaces 
the original function. This allows you to add functionality to the original 
function without modifying its code.
For example, let's say we want to create a decorator that logs the 
execution time of a function. We can define the decorator as follows:

import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

Now we can use this decorator to log the execution time of any function. 
For example:

    @log_execution_time
    def my_function():# function body
        # some code to execute
        time.sleep(2)  # Simulating a time-consuming operation

When we call my_function(), it will now log the execution time of 
the function without us having to modify the original function's code.
Decorators can also be used to add functionality to classes. 
For example, we can create a decorator that adds a method to a class:

    def add_method(cls):
        def new_method(self):
        print("This is a new method added by the decorator.")
        cls.new_method = new_method
        return cls
Now we can use this decorator to add a new method to any class. For example:

        @add_method
            
            class MyClass:
                pass
                
                my_instance = MyClass()
                my_instance.new_method()  # Output: This is a new method 
                added by the decorator.    
In summary, decorators are a powerful tool in Python that allow 
you to modify the behavior of functions or classes without changing 
their source code. They can be used to add functionality, such as logging, 
timing, or access control, to existing functions or classes, making your 
code more flexible and reusable.
"""

"""THIS IS AN IMPORTANT TOPIC WHICH REQUIRES SOME TIME TO STUDY AND EXERCISE, 
DO IT LATER ON AND UNDERSTAND IT FULLY, 
FEEL COMFORTABLE READING AND PRUPOSE OF THE DECORATORSWHERE USED"""