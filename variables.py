#Variables are containers for storing data values.
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

# Case-Sensitive
# Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:

# CAMEL Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# PASCAL Case
# Each word starts with a capital letter:

MyVariableName = "John"

# SNAKE Case
# Each word is separated by an underscore character:

my_variable_name = "John"

                                #ASSIGN MULTIPLE VSLUES

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

                            # One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

# Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

                        #Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits=["apple","banana","mango"]
x=y=z=fruits

print(x)
print(y)
print(z)

                        #Output Variables
# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:
# Example
x = "awesome"
print("Python is " + x)
print("python is:" + x)

# If you try to combine a string and a number, Python will give you an error:

# x = 5
# y = "John"
# print(x + y)

                                #PYTHON GLOBAL VARIABLES
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.

x = "global"

def myfunc():
  print("Python is " + x)

myfunc()


def test():
    print("python is " +  x)
test()

# If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. The global variable with the same name will remain as it was, 
# global and with the original value.

x = "handsome"

def myfunc():
  x = "awesome"
  print("Python is " + x)

myfunc()
#it will access global variable
print("Python is " + x)


                                                #THE GLOBAL KEYWORD

# Normally, when you create a variable inside a function, 
# that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
#If you use the global keyword, the variable belongs to the global scope:
def myfunc1():
  global x
  x = "fantastic"

myfunc1()

print("Python variable used as global " + x)

# use the global keyword if you want to change a global variable inside a function.

x = "random"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

                    # Global and Local Variables in Python  GEEKS FOR GEEKS

# Global variables are those which are not defined inside any function and have a global scope 
# whereas local variables are those which are defined inside a function and its scope is limited to that function only. 
# In other words, we can say that local variables are accessible only inside the function in which it was initialized
#  whereas the global variables are accessible throughout the program and inside every function. 

def f():
  # local variable
  s= "hello world"
  print(s)

f()
#if we try to use local variable outside thre dfunction
# print(s)

# Defining and accessing global variables

# This function uses global variable s
def f():
    print("Inside Function", s)
 
# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)


# what if there is a variable with the same name initialized inside a function as well as globally.
#  Now the question arises, will the local variable will have some effect on the global variable or vice versa, 
#  and what will happen if we change the value of variable inside of the function f()? 
# Will it affect the globals as well? We test it in the following piece of code: 

# This function has a variable with
# name same as s.
def f():
    s = "Me too."
    print(s)
 
# Global scope
s = "I love Geeksforgeeks"
f()
print(s)


# This function uses global variable s
# def f():

#   s = s +'GFG'
#   print("Inside Function", s)

# # Global scope
# s = "I love Geeksforgeeks"
# f()

                          # Global Keyword
# We only need to use the global keyword in a function if we want to do assignments or change the global variable.
#  global is not needed for printing and accessing. Python “assumes” that we want a local variable due to the assignment to s inside of f(), 
#  so the first statement throws the error message.
#   Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. 
#   To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example: 


# This function modifies the global variable 's'
def f():
    global s
    s += ' GFG'
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)
 
# Global Scope
s = "Python is great!"
f()
print(s)


# .....................................................

a = 1
 
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
 
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)
 
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)
 
 
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)