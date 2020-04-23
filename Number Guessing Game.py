import random
print('Welcome to the Number Guessing Game')
level = input('\n Choose a level: easy, medium or hard \n')

if level.lower() == "easy":
	sought = random.randint(1,10)
	number_of_tries = 1
	guess = int(input('Please choose a number between 1 and 10 as your guess: '))
	while sought != guess:
		print (f"That was wrong. You have {6-number_of_tries} attempts left.")
		if number_of_tries == 6:
			break
		guess = int(input('Please try again: '))
		number_of_tries += 1
	if sought == guess:
		print('You were right! Well done.')
	else:
		print("Game over!!!")
		print("The number you were to guess was", sought)

elif level.lower() == "medium":
	sought = random.randint(1,20)
	number_of_tries = 1
	guess = int(input('Please choose a number between 1 and 20 as your guess: '))
	while sought != guess:
		print (f"That was wrong. You have {4-number_of_tries} attempts left.")
		if number_of_tries == 4:
			break
		guess = int(input('Please try again: '))
		number_of_tries += 1
	if sought == guess:
		print('You were right! Well done.')
	else:
		print("Game over!!!")
		print("The number you were to guess was", sought)

elif level.lower() == "hard":
	sought = random.randint(1,50)
	number_of_tries = 1
	guess = int(input('Please choose a number between 1 and 50 as your guess: '))
	while sought != guess:
		print (f"That was wrong. You have {3-number_of_tries} attempts left.")
		if number_of_tries == 3:
			break
		guess = int(input('Please try again: '))
		number_of_tries += 1
	if sought == guess:
		print('You were right! Well done.')
	else:
		print("Game over!!!")
		print("The number you were to guess was", sought)

else:
	print('\n Please start again and check your input very well this time around.')






