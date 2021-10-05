#!/usr/bin/env python

# In this module is the numerical conversion
import num_conv

# It has to import either python 3 or 2 version
try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk


# Star the main class
class HexConv(object):
	def __init__(self):
		super().__init__()
		
	
	# Main function
	def main(self):
		self.root = tk.Tk()
		self.root.geometry('600x800')
		self.root.title("From Decimal to Hexadecimal converter")
		self.index = 0
		
		self.number = tk.IntVar()
		self.display_number = tk.Entry (self.root, textvariable=self.number, state= 'normal', font = ('Arial 11'))
		self.display_number.grid(row=0, column=0, columnspan=2, rowspan=2, pady=20, padx=10)
		
		self.createButton('Copy', 0, 2). config(bg='yellow')
		self.createButton(9, 2, 0).config(command=lambda:self.input_number(9))
		self.createButton(8, 2, 1).config(command=lambda:self.input_number(8))
		self.createButton(7, 2, 2).config(command=lambda:self.input_number(7))
		self.createButton(6, 3, 0).config(command=lambda:self.input_number(6))
		self.createButton(5, 3, 1).config(command=lambda:self.input_number(5))
		self.createButton(4, 3, 2).config(command=lambda:self.input_number(4))
		self.createButton(3, 4, 0).config(command=lambda:self.input_number(3))
		self.createButton(2, 4, 1).config(command=lambda:self.input_number(2))
		self.createButton(1, 4, 2).config(command=lambda:self.input_number(1))
		self.createButton('Clear', 5, 0).config(bg= 'blue', command=self.clear_screen)
		btnButton = self.createButton(0, 5, 1).config(command=lambda:self.input_number(0))
			
		self.createButton('=', 5, 2).config(bg= 'green', command=self.convert)
		
		self.root.mainloop()

		
	def convert (self):
		self.n = self.number.get()
		self.message = num_conv.hex_upper(self.n)
		self.display_number.delete(0, tk.END)
		self.display_number.insert(0, self.message)
		
		self.index=0
		
	# This function creates a button and displays it in a grid with x and y position given
	def createButton(self, value, posx, posy):
		boton = tk.Button(self.root, text = str(value), font = ('Arial 11'))
		boton.grid(row= posx, column= posy, pady=10, padx=5)
		return boton
	
	# This function clear the display number screen
	def clear_screen(self):
		self.display_number.delete(0, tk.END)
		self.index = 0
	
	# This function writes the numbers into the Entry	
	def input_number(self, value):
		self.display_number.insert(self.index, value)
		self.index += 1
		
if __name__ == '__main__':
	conv = HexConv()
	conv.main()
	