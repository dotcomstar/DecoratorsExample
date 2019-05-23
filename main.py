#!/usr/bin/env python
import os
import sys
import decorators as d

def main():
    print("Starting main()\n")
    say_whee()
    say_oink()
    say_hi_to_Jawad()
    print("\nFinishing main()")

# ~~~~ Function definitions ~~~~

@d.simple_decorator  # This is the same as writing say_whee = d.simple_decorator(say_whee)
def say_whee():
    print("WHEE")

@d.print_function_names
def say_oink():
    print("OINK")

def say_hi_to_Jawad():
    print("Hi Jawad")

# ~~~~ Don't worry about this for now ~~~~
if __name__ == "__main__":
    main()
