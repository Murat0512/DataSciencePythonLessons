"""Lambda Expressions"""


"""Lambda expressions, also known as anonymous functions, 
are a way to create small, one-line functions in Python. They are 
defined using the lambda keyword,
followed by a list of parameters, a colon, and an expression 
that is evaluated and returned when the function is called.
Lambda expressions are often used in situations where a small function 
is needed for a short period of time
and it is not necessary to give it a name. They are commonly used 
in conjunction with higher-order functions like map(), filter(), and reduce() 
to create more concise and readable code.
The syntax for a lambda expression is as follows:
lambda arguments: expression
For example, the following lambda expression takes two arguments 
and returns their sum:
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
Lambda expressions can also be used to create more complex functions, 
such as those that use conditional statements
or multiple lines of code. However, it is generally recommended to 
keep lambda expressions simple and concise, as they can become difficult 
to read and understand if they are too complex.
Lambda expressions are a powerful tool in Python that can help you write 
more concise and readable code, especially when working with higher-order 
functions. However, it is important to use them judiciously and avoid
creating overly complex lambda expressions that can be difficult to 
understand.
"""

my_list = [1,2,3,4,5]

print(list(map(lambda item:item*2 ,my_list)))
print(my_list)

"""---- lambda item:item*2 ---- is the function, it is used only ones then 
it is fogotten, and it is not stored in any variable.
"""


my_list2 = [ 2,4,5,6,7,8,10]

print(list(map(lambda item:item **2 , my_list2)))


#List sorting, We want to sort a given tuple list 
# based on the second element of each tuple.

a = [(1,3), (4,3), (9,9), (10,-1)]

"""We can use the sorted() function with a lambda expression as the key argument
to sort the list based on the second element of each tuple."""

sorted_a = sorted(a, key = lambda x: x[1])
print(sorted_a)

"""Explain the code above:
1. We have a list of tuples called 'a', where each tuple contains two elements.
2. We want to sort this list based on the second element of each tuple.
3. We use the sorted() function, which takes an iterable and returns a new sorted list.
4. We pass the list 'a' as the first argument to sorted().
5. We use the 'key' parameter of the sorted() function to specify a 
function that
   will be called on each element of the list to determine the value 
   to sort by.
6. We provide a lambda function as the key, which takes a tuple 'x' as 
input and
    returns the second element of the tuple (x[1]).
7. The sorted() function uses the values returned by the lambda function 
to sort the list.
8. Finally, we print the sorted list 'sorted_a', which will be sorted 
based on the second element of each tuple.
Output:
[(10, -1), (1, 3), (4, 3), (9, 9)]
"""