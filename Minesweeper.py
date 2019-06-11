import pickle
import os
from tkinter import *
from pathlib import Path
import random

minWidth = 5
maxWidth = 30
minHeight = 5
maxHeight = 30
difficulty = 10


class Window():
	def createWindow(self):
		self.window = Tk()
		self.window.title(self.title)
		self.window.configure(background = "white")
	def vertical_label_create(self,Text):
		Label(self.window, text = Text, bg = "white").grid(row=self.row,column=0,sticky=W)
		self.row += 1

class minesweeper(Window):

	def __init__(self):
		super()
		self.title = " "
		self.row = 0

	def setup_submit(self):
		try:
			self.width_value = int(self.width.get())
			self.height_value = int(self.height.get())
			difficulty = int(self.difficulty.get())
			failed = False
		except:
			failed = True
		if failed == False:
			failed = True
			if minHeight <= self.height_value <= maxHeight:
				failed = False
			if minWidth <= self.width_value <= maxWidth:
				failed = False
		if difficulty < 2:
			failed = True
		if failed == True:
			Label(self.window, text = "Please check", bg = "red", fg = "yellow").grid(row=self.row,column=0,sticky=W)
			Label(self.window, text = "your inputs", bg = "red", fg = "yellow").grid(row=self.row+1,column=0,sticky=W)
		else:
			self.window.destroy()


	def setup(self):
		maxWidthLabel = "Width (" + str(minWidth) + " - " + str(maxWidth) + "):"
		maxHeightLabel = "Width (" + str(minHeight) + " - " + str(maxHeight) + "):"
		self.title = "Minesweeper Setup"
		self.createWindow()

		self.vertical_label_create(maxWidthLabel)

		self.width = Entry(self.window, bg = "white")
		self.width.grid(row=self.row,column=0,sticky=W)
		self.row += 1

		self.vertical_label_create(maxHeightLabel)
		self.height = Entry(self.window, bg = "white")
		self.height.grid(row=self.row,column=0,sticky=W)
		self.row += 1

		self.vertical_label_create("Difficulty (2+)")
		self.difficulty = Entry(self.window, bg = "white")
		self.difficulty.grid(row=self.row,column=0,sticky=W)
		self.row += 1

		Button(self.window, text="Submit",command = self.setup_submit).grid(row=self.row,column=0,sticky=W)
		self.row += 1
		self.window.mainloop()
		self.game()

	def button(self,pos):
		print(pos)
		f = Frame(self.window,width=20,height=20)
		b = Label(f,text = self.board[pos[0]][pos[1]])
		f.rowconfigure(0, weight = 1)
		f.columnconfigure(0, weight = 1)
		f.grid_propagate(0)
		f.grid(row = pos[1], column = pos[0])
		b.grid(sticky = "NWSE")
		#insert ant program

	def game(self):
		self.board = []
		column = 0
		x = 0
		y = 0
		temp = []
		while y < self.width_value:
			a = random.randint(0, difficulty)
			if a == difficulty:
				temp = temp + ["X"]
			else:
				temp = temp + [' ']
			x += 1
			if x == self.height_value:
				self.board += [temp]
				temp = []
				y += 1
				x = 0
		x = 0
		y = 0
		while y < self.width_value:
			num = 0
			if self.board[x][y]!='X':
				if x > 0 and y > 0:
					if self.board[x-1][y-1] == 'X':
						num += 1
				if y > 0:
					if self.board[x][y-1] == 'X':
						num += 1
				if y > 0 and x < (self.width_value - 1):
					if self.board[x+1][y-1] == 'X':
						num += 1
				if x < (self.width_value - 1):
					if self.board[x+1][y] == 'X':
						num += 1
				if x < (self.width_value - 1) and y < (self.height_value - 1):
					if self.board[x+1][y+1] == 'X':
						num+=1
				if y < (self.height_value - 1):
					if self.board[x][y+1] == 'X':
						num+=1
				if x > 0 and y < (self.height_value - 1):
					if self.board[x-1][y+1] == 'X':
						num+=1
				if x > 0:
					if self.board[x-1][y] == 'X':
						num += 1
			if num != 0:
				self.board[x][y] = str(num)
			x+=1
			if x == self.height_value:
				y += 1
				x = 0
		win = False
		while win == False:
			self.window = Tk()
			x = 0
			y = 0
			while y < self.width_value:
				f = Frame(self.window,width=20,height=20)
				b = Button(f,command=lambda m=[x,y]: self.button(m))
				f.rowconfigure(0, weight = 1)
				f.columnconfigure(0, weight = 1)
				f.grid_propagate(0)
				f.grid(row = y, column = x)
				b.grid(sticky = "NWSE")

				
				
				x += 1
				if x == self.height_value:
					y += 1
					x = 0
			self.window.mainloop()
Minesweeper = minesweeper()
Minesweeper.setup()

