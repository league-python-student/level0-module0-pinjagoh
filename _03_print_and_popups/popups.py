from tkinter import messagebox, simpledialog, Tk

window = Tk()

window.withdraw()

print("hello")

messagebox.showinfo(None, message="hello")


name = simpledialog.askstring(None, prompt="what is your name?")

messagebox.showerror(title="error", message="this is a message," + name)

print(name + " is your name")

window.mainloop()