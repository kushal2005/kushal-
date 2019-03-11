import random

while True:
    d=input("\npress r to roll\n press q to quit!\n")
    if d=="r":
    	print("You got:",random.randint(1,6))
    if d=="q":
       print("Bye!!")
       exit()



