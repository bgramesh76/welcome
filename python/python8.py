#! /usr/bin/python

def ram():
    x=0
    while(x<4):
        print(x)
        x=x+1

if __name__ == "__main__":
    ram()

print("=================================================================")

def kumar():
    months = ["Jan", "feb", "Mar"]
    for m in months:
        print(m)

if __name__ == "__main__":
    kumar()

print("================================================================")

def ram():
    for x in range(10,20):
       # if (x == 15):
        #    break
        if (x % 5 == 0):
            continue
        print x
if __name__ == "__main__":
    ram()

print("===============================================================")

# How to use "While Loop"
#Example file for working with loops
#
def main():
	x=0
	#define a while loop
	while(x <4):
		print x
		x = x+1

if __name__ == "__main__":
    main()

#How to use "For Loop"
#Example file for working with loops
#
def main():
	x=0
	#define a while loop
#	while(x <4):
#		print x
#		x = x+1


#Define a for loop
for x in range(2,7):
		print x


if __name__ == "__main__":
    main()

#How to use For Loop for String
def main():
	#use a for loop over a collection
	Months = ["Jan","Feb","Mar","April","May","June"]
	for m in Months:
		print m

if __name__ == "__main__":
	main()

#How to use break statements in For Loop
def main():
	#use a for loop over a collection
	#Months = ["Jan","Feb","Mar","April","May","June"]
	#for m in Months:
		#print m

# use the break and continue statements
		for x in range (10,20):
			if (x == 15): break
			#if (x % 2 == 0) : continue
			print x

if __name__ == "__main__":
	main()

#How to use "continue statement" in For Loop
def main():
	#use a for loop over a collection
	#Months = ["Jan","Feb","Mar","April","May","June"]
	#for m in Months:
		#print m

# use the break and continue statements
		for x in range (10,20):
			#if (x == 15): break
			if (x % 5 == 0) : continue
			print x

if __name__ == "__main__":
	main()

#How to use "enumerate" function for "For Loop"
def main():
	#use a for loop over a collection
	Months = ["Jan","Feb","Mar","April","May","June"]
	for i, m in enumerate (Months):
		print i,m

# use the break and continue statements
		#for x in range (10,20):
		#if (x == 15): break
		#if (x % 5 == 0) : continue
		#print x

if __name__ == "__main__":
	main()
