#!/usr/bin/env python

import num_conv
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
title = tkinter.Label (root, text='From Decimal to Hexadecimal converter')
number = tkinter.IntVar()
decimal = tkinter.Entry (root, textvariable=number)

def convert ():
	n = number.get()
	
	message = num_conv.hex_upper(n)
	
	messagebox.showinfo('Hexadecinal number', message)	
button = tkinter.Button(root, text='Enter', command= convert)

def createDigit(value):
	button = tkinter.Button(root, text=str (value))
	button.grid(row=2, column=1)
	
title.grid(row=0, column=0, columnspan=2)
decimal.grid(row=1, column=0)
button.grid(row=1, column=1)

createDigit (0)

root.mainloop()
