import random  # Allow the program to use random numbers

while True:
    print()  # Prints a blank line
    usersQuestion = input('Ask the Magic 8-Ball a question (press enter to quit): ')

    if usersQuestion == "":
        break  # Exit the loop if the user presses Enter

    randomAnswer = random.randrange(0, 8)  # Pick a random number

    if randomAnswer == 0:
        print('It is certain.')
    elif randomAnswer == 1:
        print('Absolutely!')
    elif randomAnswer == 2:
        print('You may rely on it.')
    elif randomAnswer == 3:
        print('Answer is foggy, ask again later.')
    elif randomAnswer == 4:
        print('Concentrate and ask again.')
    elif randomAnswer == 5:
        print('Unsure at this point, try again.')
    elif randomAnswer == 6:
        print('No way, dude!')
    elif randomAnswer == 7:
        print('No, no, no, no, no.')