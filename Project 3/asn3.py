import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("tkinter Form")
root.geometry("500x300")

# Create a label frame
lblFrPerson = tk.LabelFrame(root, text="Personal Information")
lblFrPerson.pack(padx=10, pady=10)

# Create first name label and entry
lblFirst = tk.Label(lblFrPerson, text="First Name:")
lblFirst.grid(row=0, column=0, padx=5, pady=5)
entFirst = tk.Entry(lblFrPerson)
entFirst.grid(row=0, column=1, padx=5, pady=5)

# Add blue background and white foreground to this label
lblFirst.config(bg="blue", fg="white")


# Create last name label and entry
lblLast = tk.Label(lblFrPerson, text= "Last Name:")
lblLast.grid(row=1, column=0, padx=5, pady=5)
entLast = tk.Entry(lblFrPerson)
entLast.grid(row=1, column=1, padx=5, pady=5)

# Add blue background and white foreground to this label
lblLast.config(bg="blue", fg="white")

# Create email label and entry
lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(row=2, column=0, padx=5, pady=5)
entEmail = tk.Entry(lblFrPerson)
entEmail.grid(row=2, column=1, padx=5, pady=5)

# Create phone number label and entry
lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(row=3, column=0, padx=5, pady=5)
entPhone = tk.Entry(lblFrPerson)
entPhone.grid(row=3, column=1, padx=5, pady=5)

# Create Frames for buttons
fraButtons = tk.Frame(root)
fraButtons.pack(padx=10, pady=10)

# Create submite button on the left side of the frame.
btnS = tk.Button(fraButtons, text="Submit")
btnS.pack(side=tk.LEFT, padx=5, pady=5)

# Create Reset Button to the right of the submit button
btnR = tk.Button(fraButtons, text="Reset")
btnR.pack(side=tk.LEFT, padx=5, pady=5)

# Create Quit Button to the right of the reset button
btnQ = tk.Button(fraButtons, text="Quit", command=root.quit)
btnQ.pack(side=tk.LEFT, padx=5, pady=5)

# Start the main event loop

# Add functionality to the submit button and displat the entered information in a message box
def submit():
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()
    greeting = f"Welcome to tkinter, {first}"
    msgb = f"First Name: {first}\nLast Name: {last}\nEmail: {email}\nPhone: {phone}"
    messagebox.showinfo(greeting, msgb)
btnS.config(command=submit)

# Add functionality to the rest button to clear all the entry fields
def reset():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)
btnR.config(command=reset)

# Add functionality to the quit button to close the application
btnQ.config(command=root.quit)

root.mainloop()