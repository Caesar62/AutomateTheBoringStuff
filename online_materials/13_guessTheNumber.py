import random
print('I am thinking of a number between 1 and 20')

secretnumber = random.randint(1,20)
print(secretnumber)

# Ask the player to guess 6 times.
for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretnumber:
        print('The number is too low')
    elif guess > secretnumber:
        print('The number is too high')
    else:
        break # This condition es the correct guess!!

if guess == secretnumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
        