import random
#----------------------------------
randomNumber = random.randint(1,100)
guess = 0
attempts = 0
#----------------------------------

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.\n")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

choice = int(input("\nEnter your choice: "))
if choice == 1:
    print("\nGreat! You have selected the Easy difficulty level.\nLet's start the game!\n")
    Valid = False
    while not Valid:
        counter = 10
    
        if attempts == counter:
            print("You have ran out of chances!")
            Valid = True

        elif guess == randomNumber:
            print(f"Congratulations! You guessed the correct number in {attempts+1} attempts.")
            Valid = True

        else:
            guess = int(input("Enter your guess: "))
            if guess > randomNumber:
                print(f"Incorrect! The number is less than {guess}\n")
                attempts += 1
                Valid = False
            
            elif guess < randomNumber:
                print(f"Incorrect! The number is greater than {guess}\n")
                attempts +=1
                Valid = False

elif choice == 2:
    print("\nGreat! You have selected the Medium difficulty level.\nLet's start the game!\n")
    Valid = False
    while not Valid:
        counter = 5
    
        if attempts == counter:
            print("You have ran out of chances!")
            Valid = True

        elif guess == randomNumber:
            print(f"Congratulations! You guessed the correct number in {attempts+1} attempts.")
            Valid = True

        else:
            guess = int(input("Enter your guess: "))
            if guess > randomNumber:
                print(f"Incorrect! The number is less than {guess}\n")
                attempts += 1
                Valid = False
            
            elif guess < randomNumber:
                print(f"Incorrect! The number is greater than {guess}\n")
                attempts +=1
                Valid = False

elif choice == 3:
    print("\nGreat! You have selected the Hard difficulty level.\nLet's start the game!\n")
    Valid = False
    while not Valid:
        counter = 3
    
        if attempts == counter:
            print("You have ran out of chances!")
            Valid = True

        elif guess == randomNumber:
            print(f"Congratulations! You guessed the correct number in {attempts+1} attempts.")
            Valid = True

        else:
            guess = int(input("Enter your guess: "))
            if guess > randomNumber:
                print(f"Incorrect! The number is less than {guess}\n")
                attempts += 1
                Valid = False
            
            elif guess < randomNumber:
                print(f"Incorrect! The number is greater than {guess}\n")
                attempts +=1
                Valid = False
