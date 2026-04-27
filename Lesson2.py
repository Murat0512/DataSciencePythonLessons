"""Functional Programming in Python"""

"""Functional programming is a programming paradigm that treats 
computation as the evaluation of mathematical functions and avoids 
changing state and mutable data. 
In functional programming, functions are first-class citizens, 
meaning they can be assigned to variables, passed as arguments to 
other functions, and returned as values from other functions.
Functional programming emphasizes the use of pure functions, which are 
functions that always produce the same output for the same input and have 
no side effects. This makes functional programming easier to reason about 
and test, as pure functions are deterministic and do not rely on external 
state.
Functional programming also encourages the use of higher-order functions, 
which are functions that take other functions as arguments or return 
functions as values. Higher-order functions can be used to create more 
abstract and reusable code, as they allow you to manipulate functions in 
a flexible way.
Some common functional programming concepts in Python include:  
- Lambda functions: Anonymous functions that can be defined in a single 
line of code.
- Map, filter, and reduce: Functions that allow you to apply a function to 
a sequence of data in a functional way.
- List comprehensions: A concise way to create lists based on existing lists.
- Recursion: A technique where a function calls itself in order to solve a 
problem.
Functional programming can lead to more concise and readable code, as well 
as improved performance in certain cases
due to the use of immutable data structures and the avoidance of side 
effects. However, it may not be suitable for all programming tasks, 
and it can take some time to get used to the functional programming 
style if you are accustomed to imperative programming.
"""

"""What is a pure function?
A pure function is a function that always produces the same output for the
same input and has no side effects. This means that a pure function does not
modify any external state or data, and it does not rely on any external
state or data to produce its output. Pure functions are deterministic, which
makes them easier to reason about and test, as they do not have any hidden
dependencies or side effects that can affect their behavior. Pure functions are
a fundamental concept in functional programming, and they are often used to
create more predictable and reusable code.
"""


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1, 2, 3]))


"""Everytime we put the same input 1,2,3 we have to get the same output 2,4,6
 and we are not changing the state of the list a. 
 So this is a pure function. there has to be no side effect 
 and no change in the state of the data.As you can see the function does not connect in anyway outside of
the function and it does not change the state of the data."""

"""The interraction with the outside of function can be shown in this example"""

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    print(new_list)
"""This print statement above interracts with outside function because we still dont know until the variable
 decleration what the values will be"""
print(multiply_by2([1, 2, 3]))

"""It is better readable and can be tested easier if we return the new list instead of printing it.
This way we can test the function by comparing the output with the expected output.
This is a pure function because it does not have any side effects and it always produces the same
output for the same input."""

"""Another exampe for having side effect can be defining 
new_list =[] being outside the function and then appending to it inside the function.
This will change the state of the data and it will not be a pure function anymore.
new_list = []
def multiply_by2(li):
    for item in li:
        new_list.append(item*2)
    return new_list
print(multiply_by2([1, 2, 3]))

"""



