import random # Step 1: bring the random tool
secret_number = random.randint(1, 10) # secret_Number is a variable which will store the secret number choosen by computer between 1 and 10
guess = 0 # we tok 0 as a dummy value to enter a loop, cant be entering a loop empty 
while guess!= secret_number:
     guess = int(input("Guess the number between 1 and 10: "))  # keep looping until it is equal to secret number 

     if guess == secret_number:  
          print("🎉 Correct! You guessed the number!")  
     else:
          print("❌ Wrong guess, try again!")
        
