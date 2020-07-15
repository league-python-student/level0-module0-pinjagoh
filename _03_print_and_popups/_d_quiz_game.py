from tkinter import messagebox, simpledialog, Tk
import random
from _ast import If

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    answer = simpledialog.askstring("Are you a human?", prompt="(yes/no)")
    #      // 2.  Ask the user a question 
    if answer == "yes":
    #      // 3.  Use an if statement to check if their answer is correct
        score = score + 1
    #      // 4.  if the user's answer was correct, add one to their score 
        messagebox.showinfo("Correct!", "Correct! \nYour score is " + str(score))
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    elif answer == "no":
        score = score - 1
        messagebox.showinfo("I think you are lying...", message="I think you are lying... \nYour score is " + str(score))
    else:
        score = score - 10
        messagebox.showinfo("You didn't answer properly!", message="You didn't answer properly! \nYour score is " + str(score))
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    answer = simpledialog.askstring("Are you a robot?", prompt="(yes/no)")
    
    if answer == "yes":
        score = score - 1
        messagebox.showinfo("I think you are lying...", "I think you are lying... \nYour score is " + str(score))
            
    elif answer == "no":
        score = score + 1
        messagebox.showinfo("Correct!", message="Correct! \nYour score is " + str(score))
            
    else:
        score = score - 10
        messagebox.showinfo("You didn't answer properly!", message="You didn't answer properly! \nYour score is " + str(score))
    
   
     
        
    answer = simpledialog.askstring("What is your favorite color?", prompt="Please enter your favorite color")
    preference = random.randint(0,3)
    
    if preference == 0:
        score = score - 10
        messagebox.showinfo(title="I don't like that color", message="I don't like " + answer +". \nYour score is " + str(score))
    
    elif preference == 1:
        messagebox.showinfo(title="That's a decent color", message=answer + " is a decent color. \nYour score remains " +str(score))
    
    elif preference == 2:
        score = score + 1
        messagebox.showinfo(title="Nice choice!", message=answer + "! You have very good taste in colors! \nYour score is " + str(score))
    else:
        score = score + 30
        messagebox.showinfo(title="Wow! An amazing answer!", message="Wow! " + answer + " is a fantastic color! \nYour score is " + str(score))
        
    
    answer = simpledialog.askinteger("What is your favorite integer value?", "What is your favorite integer value?")    
    preference = random.randint(0,1)
    
    if preference == 0:
        messagebox.showinfo(title="Wow!", message="I like that number too. \nYour score is now " + str(score) + " + " + str(answer) + " = " + str(score + answer))
        score = score + answer
        
    else:
        messagebox.showinfo(title="Oh...", message="I don't like that number very much. \nYour score is now " + str(score) + " - " + str(answer) + " = " + str(score - answer))        
        score = score - answer
    
        
        
        
    if score > 0:
        messagebox.showinfo(title="Final score:", message="Congrats! You won! \nYour final score is " + str(score))
    
    else:
        messagebox.showinfo(title="Final score:", message="Better luck next time... \nYour final score is " + str(score))
    window.mainloop()
    # Run the window's .mainloop() method
