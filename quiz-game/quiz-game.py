playing = input('Do you want to play a game? ')
if playing.lower() != 'yes':
    print('Ok, maybe next time!')
    quit()
print("Okay! Let's play a game!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'You got {score} question(s) correct!')
print(f'You got {score / 2 * 100}% correct!')
