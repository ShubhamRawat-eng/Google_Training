# This is Guess the number game
import random
playagain = 'y'
while playagain == "Y" or playagain == 'y':
	secret_number = random.randint(1,20)
	print('\nI am thinking of a number between 1 to 20.')

	# Ask the player to guess 6 times.
	for guesses_taken in range(1,7):
		guess = int(input('Take a guess:'))

		if guess < secret_number:
			print('Your number is too low.')

		elif guess > secret_number:
			print('Your number is too High.')
		else:
			break

	if guess == secret_number:
		print(f'Good job! You got it in {guesses_taken} guess!')
	else:
		print(f"Nope. The number was {secret_number} ")
	
	playagain = input('Would u like to play again(Y/N): ')