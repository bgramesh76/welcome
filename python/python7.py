#! /usr/bin/python

def ram():
    print ("I am a good boy")

ram()

def ram(x):
    print(x*x)
print(ram(4))

print("===============================================================")

def kumar(x):
    return x*x
print(kumar(3))

def kumar(x):
    return x*x
print(kumar)

print("===============================================================")

def multiply(x, y):
    print(x*y)
multiply(3,6)

print("===============================================================")

def ram():
    x,y = 8,8

    if (x<y):
        st = "x is less than y"
    elif (x==y):
        st = "x is same as y"
    else:
        st = "x is greater than y"
    print(st)
if __name__ == "__main__":
    ram()

print("===============================================================")

def ram():
    x, y = 10, 8
    st = "x is less than y" if (x<y) else "x is greater than or equal to the y"
    print(st)

if __name__ == "__main__":
    ram()

print("============================================================================")

#Uncomment Line 2 in above code and comment Line 3 and run the code again 
total = 100
country = "US"
#country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
        print("Shipping Cost is $25")
elif total <= 150:
	    print("Shipping Costs $5")
else:
        print("FREE")
if country == "AU":
	  if total <= 50:
	    print("Shipping Cost is  $100")
else:
	    print("FREE")

print("==================================================================================")

# If Statement
#Example file for working with conditional statement
#
def main():
	x,y =2,8

	if(x < y):
		st= "x is less than y"
	print st

if __name__ == "__main__":
	main()



# How to use "else condition"
#Example file for working with conditional statement
#
def main():
	x,y =8,4

	if(x < y):
		st= "x is less than y"
	else:
		st= "x is greater than y"
	print st

if __name__ == "__main__":
	main()



# When "else condition" does not work
#Example file for working with conditional statement
#
def main():
	x,y =8,8

	if(x < y):
		st= "x is less than y"
	else:
		st= "x is greater than y"
	print st

if __name__ == "__main__":
	main()


# How to use "elif" condition
#Example file for working with conditional statement
#
def main():
	x,y =8,8

	if(x < y):
		st= "x is less than y"

	elif (x == y):
		st= "x is same as y"

	else:
		st="x is greater than y"
	print st

if __name__ == "__main__":
	main()


# How to execute conditional statement with minimal code
def main():
	x,y = 10,8
	st = "x is less than y" if (x < y) else "x is greater than or equal to y"
	print st

if __name__ == "__main__":
	main()


# Nested IF Statement
total = 100
#country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print "Shipping Cost is  $50"
elif total <= 100:
        print "Shipping Cost is $25"
elif total <= 150:
	    print "Shipping Costs $5"
else:
        print "FREE"
if country == "AU":
	  if total <= 50:
	    print "Shipping Cost is  $100"
else:
	    print "FREE"


#Switch Statement
def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print SwitchExample(argument)
