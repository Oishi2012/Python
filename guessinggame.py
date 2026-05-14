import random
def guessinggame():
    print("Welcome to the Guessing Game!")
    name=input("What is your name? ")
    wanna_play=input("Do you want to play? (yes/no) ")
    if wanna_play=="no":
       print("Okay, maybe next time!")

    secret_num=random.randint(1,100)
    attempts=0
    max_attempts=3
    print('You only have 3 attempts to guess the number between 1 to 100.')
    while attempts<max_attempts:
        guess=int(input("Enter your guess: "))
        attempts=attempts+1

        if guess==secret_num:
            print("Well done! You have guessed the right number!")
            break
        elif guess<secret_num:
            print("Try a bigger number.")
        else:
            print("Try a smaller number.")

        print("Attempts left:", max_attempts-attempts)
    else:
        print("You lost. The correct number was",secret_num)
    print("Thank you for playing")
guessinggame()

  
        

    


    