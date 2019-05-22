#!/usr/bin/env python
import os
import sys
import functools  # You need to this import to use decorators on functions with parameters.

"""
Note: Each decorator takes a function as an input. See the function/argument example file for
more information on this.

The syntax is as follows:

@decorator_name
def function_name():
    put_code_here

"""
# ~~~~ The Decorators ~~~~

def simple_decorator(func):
    def wrapper():
        print("Before the function squad")
        func()
        print("Finito, fam")
    return wrapper

# This decorator can be used on functions with parameters
def print_function_names(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):  # This allows the function's parameters to be passed along.
        print("\nStarted " + str(func.__name__) + "()")  # You can do whatever you want before the function.
        value = func(*args, **kwargs)  # Actually runs the function, and stores the output as a variable.
        print("Finished " + str(func.__name__) + "()\n")  # You can do whatever you want after the function.
        return value  # Ensures the return values are passed through.
    return wrapper_decorator
