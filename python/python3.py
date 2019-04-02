#! /usr/bin/python

# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)


print("=================================================================")

f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
print(f)
f = "changing global variable"
someFunction()
print(f)

print("==================================================================")

f = 11;
print(f)
del f
print(f)


