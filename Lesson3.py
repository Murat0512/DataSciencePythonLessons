
from functools import reduce


"""map() function is used to apply a function, and return a map object 
(which is an iterator). It is a built in function in Python that takes 
a function and an iterable as arguments, and applies the function 
to each item of the iterable, returning a map object that can be 
converted to a list or other iterable type. 
The map() function is often used to apply a transformation to each item
 in a list or other iterable, without having to write a loop."""

def multiply_By2(item):
     return item * 2 

print(list(map(multiply_By2, [1,2,3])))

"""To be able to print the outcome we need to create a list out of 
the map object.
The map function is a pure function because it does not have 
any side effects and it always produces"""




""" 
filter() function is used to filter items out of an iterable based on a 
function that returns a boolean value
"""

def only_even(item):
     return item %2 == 0 
print(list(filter(only_even, [1,2,3,4,5,6,7,8,9,10])))


"""
zip() function is used to combine two or more iterables 
(like lists, tuples etc.)to all the items in an iterable 
(like list, tuple etc.) 
"""
my_list = [10,20,30]
your_list = [40,50,60]

print(list(zip(my_list, your_list))) 
# It will zip the items together and create a list of tuples. 
# Each tuple will contain one item from each of the input lists.
#result is [(10, 40), (20, 50), (30, 60)]

users = ["user1", "user2", "user3"]
passwords = ["pass1", "pass2", "pass3"]

print(list(zip(users, passwords))) 
# See how useful it cna be to zip two lists together.

movies= ["movie1", "movie2", "movie3"]  
ratings = [5, 4, 3]

total_result = list(zip(movies,ratings))
print(total_result)


"""
reduce() function is used to apply a function cumulatively to 
the items of an iterable, from left to right, so as to reduce 
the iterable to a single value.Reduce does not come as built
 in python function but it is part of the functools module, 
 so you need to import it before using it.
"""

my_lists = [1,2,3,4,5]

def accumulator(acc, item):
    print(acc,item)
    return acc + item

print(reduce(accumulator, my_lists, 0 ))

"""
The result will be
3 3
6 4
10 5
15
The reduce function takes the first two items of the list and applies 
the accumulator function to them, which returns 3. 
Then it takes the result (3) and the
next item (4) and applies the accumulator function again, 
which returns 6. This process continues until all items 
in the list have been processed, resulting in a final value of 15.
"""



