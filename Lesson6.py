"""Errors in Python These can also be called exceptions, 
and they occur when something goes wrong in your code."""

"""Examples in errors in python could be anything and
   we will have many of them in the future, but here are 
   some common examples of errors in Python:
   1. SyntaxError: This error occurs when there is a syntax error in the code, 
   such as a missing parenthesis or a misspelled keyword.

   2. NameError: This error occurs when a variable or function is not defined 
   or is out of scope.

   3. TypeError: This error occurs when an operation is performed on an 
   object of an inappropriate type, such as trying to add a string and an 
   integer.

   4. ValueError: This error occurs when a function receives an argument 

   of the correct type but an inappropriate value, such as trying to convert 
   a string that cannot be converted to an integer.

   5. IndexError: This error occurs when trying to access an index that is
     out of range in a list or other sequence.

   6. KeyError: This error occurs when trying to access a key that does not
     exist in a dictionary.

   7. AttributeError: This error occurs when trying to access an attribute 
   that does not exist on an object.

   8. ZeroDivisionError: This error occurs when trying to divide a number 
   by zero.

   9. ImportError: This error occurs when trying to import a module that 
   cannot be found or has an error in its code.

   10. FileNotFoundError: This error occurs when trying to open a file 
   that does not exist.

   11. IndentationError: This error occurs when there is an issue with the
    indentation of the code, such as mixing tabs and spaces or having 
    inconsistent indentation levels.

   12. RuntimeError: This error occurs when an error is detected that does not
    fall into any of the other categories, such as an error in a generator
    or an error in a thread.

   13. MemoryError: This error occurs when the program runs out of memory,
    such as when trying to create a very large list or when there is a 
    memory leak in the code.

   14. OverflowError: This error occurs when a calculation exceeds the maximum
    limit for a numeric type, such as when trying to calculate a very large
    factorial or when trying to raise a number to a very large power.

   15. RecursionError: This error occurs when a function calls itself too many
    times, such as when there is a bug in a recursive function that causes it
    to call itself indefinitely.

   16. AssertionError: This error occurs when an assert statement fails, such as
    when a condition that is expected to be true is actually false.

   17. KeyboardInterrupt: This error occurs when the user interrupts the program
    by pressing Ctrl+C or another interrupt signal.

   These are just a few examples of the many types of errors that can 
   occur in Python. It is important to understand how to handle these 
   errors using try-except blocks and other error-handling techniques 
   to ensure that your code runs smoothly and does not crash unexpectedly."""


"""Thats why we need error handling in Python, 
to catch and handle these errors gracefully, instead of letting them crash the program.
Error handling allows us to write code that can recover from errors, log them, or provide useful feedback to the user, rather than just crashing with an error message.
This is typically done using try-except blocks, where you can specify the code that may raise an error in the try block, and then handle the error in the except block. This way, you can prevent your program from crashing and provide a better user experience.
For example, if you have a function that divides two numbers, you can use error handling to catch the ZeroDivisionError that may occur when the second number is zero:
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None"
In this example, if the user tries to divide by zero, the program will catch 
the ZeroDivisionError and print an error message instead of crashing. 
This allows the program to continue running and provides a better user 
experience.
In summary, error handling is essential in Python to ensure that your 
code can handle unexpected situations gracefully
and provide a better user experience, rather than crashing with an 
error message."""
