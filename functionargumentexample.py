#!/usr/bin/env python
import os
import sys

# This file contains examples of functions as arguments.

# ~~~~ Function definitions ~~~~

def say_hello(name):
    return "Hello " + str(name)

def be_awesome(name):
    return "Yo " + str(name) + ", together we are the awesomest!"

def greet_bob(greeter_func):
    print(greeter_func("Bob"))  # Takes a function as an argument, then passes "Bob"
                                # into that function and prints the results.

# Python will run the following code.
print("Starting examples of functions as arguments:")
greet_bob(say_hello)
greet_bob(be_awesome)
print("Finished with example")
