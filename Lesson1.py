"""MRO Method Resolution Order"""

"""What is Method Resolution Order? MRO is the order in which Python looks 
for a method in a hierarchy of classes. When you call a method on an instance 
of a class, Python will first look for that method in the class of the 
instance. If it doesn't find it there, it will look in the parent classes, 
following the order of inheritance.
The MRO is determined by the C3 linearization algorithm, which ensures 
that the method resolution order is consistent and predictable. 
The MRO can be accessed using the __mro__ attribute of a class or by using
the mro() method. The MRO is important to understand when working with
multiple inheritance, as it determines which method will be called when 
there are multiple methods with the same name in different classes.
 """