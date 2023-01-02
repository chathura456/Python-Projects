print('Welcome to Quiz Game')

playing = input('Do you want to play this game(Y/N)? ')

if playing.lower() != 'y':
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does CPU mean? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU mean? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM mean? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM mean? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU mean? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSD mean? ")
if answer.lower() == "solid state disk":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " Questions correct!")
print("You got " + str(round(((score / 6) * 100), 2)) + "%")
