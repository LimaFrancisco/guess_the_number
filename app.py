from random import randint
number = randint(0,100)

while True:    

    guess_number = int(input("I'm thinking of a number! Try to guess the number I'm thinking of: "))

    while guess_number != number:
        if guess_number > number:
            guess_number = int(input("Too high! Guess again: "))

        elif guess_number < number:
            guess_number = int(input("Too low! Guess again: "))

    response = input("That's it! Would you like to play again? (yes/no) ")

    if response == 'no':
        print("Thanks for playing!")
        exit()
    elif response == 'yes':
        number = randint(0,100)
        continue
    else:
        print("invalid response")
        exit()