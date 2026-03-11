import tkinter as tk
from tkinter import Label, messagebox
from PIL import Image, ImageTk

class ASN4():
	def __init__(self):
		#Create the main application window and set the size to 400x300 pixels
		self.root = tk.Tk()
		self.root.title("Food Viewer")
		self.root.geometry("400x400")

		#-----------------------------------------------------------------------
		#Create two frames with packs
		self.img_frame = tk.Frame(self.root)
		self.img_frame.pack()

		self.rbdBtn_frame = tk.Frame(self.root)
		self.rbdBtn_frame.pack()

		#-----------------------------------------------------------------------
		#Create a label to display the image
		self.lbl = tk.Label(self.img_frame)
		self.lbl.pack()

		#----------------------------------------------------------------------
		#Path the images from the images folder and resize them to 400x300 pixels
		#chicken.jpg
		self.img1 = Image.open("chicken.jpg")
		self.img1 = self.img1.resize((400, 300))
		self.imgOne = ImageTk.PhotoImage(self.img1)

		#pie.jpg
		self.img2 = Image.open("pie.jpg")
		self.img2 = self.img2.resize((400, 300))
		self.imgTwo = ImageTk.PhotoImage(self.img2)
		
		#pizza.jpg
		self.img3 = Image.open("pizza.jpg")
		self.img3 = self.img3.resize((350, 300))
		self.imgThree = ImageTk.PhotoImage(self.img3)
		
		#steak.jpg
		self.img4 = Image.open("steak.jpg")
		self.img4 = self.img4.resize((300, 300))
		self.imgFour = ImageTk.PhotoImage(self.img4)
		
		#----------------------------------------------------------------------
		#Label (Inital Setup)
		self.lbl = tk.Label(self.img_frame, image=self.imgOne)
		self.lbl.pack()


		#-----------------------------------------------------------------------
		#Create a variable to hold the selected radio button value
		self.var = tk.IntVar()
		self.var.set(1)

		#-----------------------------------------------------------------------
		#Creatte Radiobuttons for each image and pack them
		self.radio_a = tk.Radiobutton(self.rbdBtn_frame, text="Chicken",  variable=self.var, value=1, command=self.on_radio_select)
		self.radio_b = tk.Radiobutton(self.rbdBtn_frame, text="Pie",  variable=self.var, value=2, command=self.on_radio_select)
		self.radio_c = tk.Radiobutton(self.rbdBtn_frame, text="Pizza", variable=self.var, value=3, command=self.on_radio_select)
		self.radio_d = tk.Radiobutton(self.rbdBtn_frame, text="Steak", variable=self.var, value=4, command=self.on_radio_select)
		
		self.radio_a.pack(side=tk.LEFT, padx=10)
		self.radio_b.pack(side=tk.LEFT, padx=10)
		self.radio_c.pack(side=tk.LEFT, padx=10)
		self.radio_d.pack(side=tk.LEFT, padx=10)

	#-----------------------------------------------------------------------
	#Define a method to update the displayed image based on the selected radio button
	def on_radio_select(self):
		choice = self.var.get()

		if choice == 1:
			self.lbl.config(image=self.imgOne)
		elif choice == 2:
			self.lbl.config(image=self.imgTwo)
		elif choice == 3:   
			self.lbl.config(image=self.imgThree)
		elif choice == 4:
			self.lbl.config(image=self.imgFour)

if __name__ == "__main__":
    app = ASN4()
    app.root.mainloop()