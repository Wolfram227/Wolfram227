#imports
import random
import time

#main function
def main():
    #creating the start of the game
    passthrough = True
    print('Hello, Welcome to the number guessing game!')
    
    #create main loop
    while passthrough == True:
        print('Select your difficulty,')
        difficulty = input("easy, medium, hard, expert, ELITEGAMER: ")
        
        if difficulty == "easy":
            game(10, 3)
        
        if difficulty == "medium":
            game(25, 3)
       
        if difficulty =="hard":
            game(50, 4)
        
        if difficulty =="expert":
            game(75, 5)
        
        if difficulty =="ELITEGAMER":
            print('GET READY GAMERR')
            time.sleep(1)
            
            print('BETTER HAVE YOUR GAMER CHAIR READY!')
            time.sleep(1)
            
            print('GO!')

            game(150, 7)
    
#Game fundamentals function
def game(number, countlimit):
    count = 0
    num = str(number) 
    isGameActive = True
    theNumber = random.randint(1, number +1)
    while isGameActive == True:
        guess = int(input('Guess the number from 1 to ' + num + ': '))
        count = count + 1
        if guess == theNumber:
            print('Congrats! You found the number!\nTotal number of guesses:', count, 'The number:', theNumber)
            isGameActive = False
        elif guess < theNumber:
            print("Your guess is smaller than the number.")
        else:
            print("your guess is larger than the number.")

        if count == countlimit:
            print('You have guessed more than',count,'times. The number was:', theNumber, '\nGame Over')
            isGameActive = False

#run the main function
main()
