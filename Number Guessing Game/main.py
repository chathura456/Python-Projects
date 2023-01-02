import random

range_high = input("Type a number range: 0 to > ")

if range_high.isdigit():
    range_high = int(range_high)

    if range_high < 0:
        print("Please type a Number greater than 0")
        quit()
else:
    print("Please type a Number Next Time")
    quit()

random_number = random.randint(0, range_high)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a Number Next Time")
        continue

    if user_guess == random_number:
        print("Congratulations, You got it!!")
        break
    elif user_guess > random_number:
        print("Your were above the number!")
    else:
        print("Your were below the number!")

print("You got it in", guess_count, "guesses")
