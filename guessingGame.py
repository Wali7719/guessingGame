import random

def guessing_game():

    secret_number = random.randint(1, 9)
    

    for _ in range(5):

        user_guess = int(input("Guess the number between 1 and 9: "))
        
      
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        else:
            
            difference = abs(secret_number - user_guess)
            if difference <= 2:
                print("Close, but not quite there. Try again!")
            else:
                print("Far from the correct number. Try again!")

    
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")


guessing_game()
