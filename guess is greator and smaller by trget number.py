n=18
guess=1
print("number is guess is limited to only 9 times")
while guess<=9:
    guess_number=int(input("guess the number\n"))
    if guess_number<18:
        print("you enter less number please enter greater number\n")
    elif guess_number>18:
        print("you enter greater number please enter less number\n")
    else:
        print("you won")
        print(guess,"number of guesses he/she took\n")
        break
    print(9-guess,"numer of guesses is left")
    guess=guess+1
if guess>9:
    print('game over')
