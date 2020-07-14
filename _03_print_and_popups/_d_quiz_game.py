from tkinter import messagebox, simpledialog, Tk

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
        messagebox.showinfo("Correct!", "Your score is " + str(score))
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    else:
        score = score - 1
        messagebox.showinfo("I think you are lying", message="Your score is " + str(score))
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    window.mainloop()
    # Run the window's .mainloop() method
