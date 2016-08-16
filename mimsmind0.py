import sys
from random import randint 

if len(sys.argv) > 1: 
	number_digits = int(sys.argv[1]) 
else:
	number_digits = 1 
print("Lets play the MIMSMIND game")

print("Guess a " + str(number_digits) + "-digit number :" )
x = randint(10**(number_digits-1), 10**number_digits - 1)

print(x)

won = False

count = 0
while won == False:
	guess = int(input())
	count = count + 1
	if guess == x:
		print ("Congratulations you guessed the correct number in "+ str(count)+" tries!")
		won = True
	else:
		if guess < x:
			print ('Try again. Guess a higher number: ')

		else:
			print('Try again. Guess a lower number: ')	
	

