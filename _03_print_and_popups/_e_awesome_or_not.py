from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
        
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    randomValue = random.randint(0, 3)
    # 2. Print your variable to the console
    print(randomValue)
    # 3. Get the user to enter something that they think is awesome
    awesomeResponse = simpledialog.askstring(title="Something awesome...", prompt="Please enter something you think is awesome!")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if randomValue == 0:
        messagebox.showinfo(title="Awesome!", message=awesomeResponse + " is awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    elif randomValue == 1:
        messagebox.showinfo(title="Awesome!", message=awesomeResponse + " is okay...")    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    elif randomValue == 2:
        messagebox.showinfo(title="Awesome!", message=awesomeResponse + " is boring.")    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    elif randomValue == 3:
        messagebox.showinfo(title="Awesome!", message="I don't have much of an opinion on " + awesomeResponse)            
    # Run the window's .mainloop() method
    window.mainloop()
