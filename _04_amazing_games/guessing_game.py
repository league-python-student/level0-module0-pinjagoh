from tkinter import simpledialog, messagebox, Tk
import random

if __name__ == '__main__':
    
    #Initializing window
    window = Tk()
    window.withdraw()
    
    #Turn counter
    counter = 0
    #Target number
    targetNum = random.randint(1,100)
    #Variable dictates whether the game is ongoing or not
    gameEnd = 0
    
    
    while gameEnd == 0:
        
        if counter > 10:
            gameEnd = 2
            break
        #Prompts user to guess a number and increases turn counter
        guess = simpledialog.askinteger("Guessing Game", "Please enter an integer from 1 to 100")
    
        counter += 1
        
        if guess == targetNum:
            gameEnd = 1
        
        else:
            if targetNum > guess:
                messagebox.showinfo("Not quite...", "The target number is greater than " + str(guess) + ".")
            else:
                messagebox.showinfo("Not quite...", "The target number is less than " + str(guess) + ".")
    
    if gameEnd == 1:   
        messagebox.showinfo("Congratulations!", "The target number was " + str(targetNum) + "!")
        messagebox.showinfo("Congratulations!", "You guessed " + str(counter) + " times.") 
  
    else:
        messagebox.showinfo("Better luck next time...", "You guessed too many times! The target number was " + str(targetNum) + ".")
        
    window.mainloop()