import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

from remover import BackgroundRemover

cwd = os.getcwd()

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.master = master
		self.grid()

		self.BGRemover = BackgroundRemover()

		self.draw_frames()
		self.draw_widgets()

	def draw_frames(self):
		self.uframe = tk.Frame(self, width=450, height=250, bg='green')
		self.uframe.grid(row=0, column=0)
		self.uframe.grid_propagate(False)

		self.bframe = tk.Frame(self, width=450, height=250, bg='red')
		self.bframe.grid(row=1, column=0)
		self.bframe.grid_propagate(False)

		self.rframe = tk.Frame(self, width=150, height=500, bg='blue')
		self.rframe.grid(row=0, column=1, rowspan=2)
		self.rframe.grid_propagate(False)

	def draw_widgets(self):
		self.ucanvas = tk.Canvas(self.uframe, width=450, height=250, bg='#252525')
		self.ucanvas.grid(row=0, column=0)

		self.bcanvas = tk.Canvas(self.bframe, width=450, height=250, bg='#252525')
		self.bcanvas.grid(row=0, column=0)

		self.load_btn = ttk.Button(self.rframe, text='Load Image', width=20, 
						command=self.load_image)
		self.load_btn.grid(row=0, column=0, pady=(20,0), padx=10)

		self.rb_btn = ttk.Button(self.rframe, text='Remove background', width=20,
						command=self.remove_bg)
		self.rb_btn.grid(row=1, column=0, pady=(20,0), padx=10)

		self.save_btn = ttk.Button(self.rframe, text='Save Image', width=20)
		self.save_btn.grid(row=2, column=0, pady=(20,0), padx=10)

	def load_image(self):
		filepath = filedialog.askopenfilename(initialdir = cwd)
		if filepath:
			self.filepath = filepath
			self.image = self.BGRemover.load_image(filepath, (450,250))
			self.ucanvas.create_image(0,0, anchor=tk.NW, image=self.image)
			self.update()

	def remove_bg(self):
		pass



if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('600x500+350+100')
	root.title('Word 2 PDF')
	root.resizable(0,0)

	app = Application(master=root)
	app.mainloop()