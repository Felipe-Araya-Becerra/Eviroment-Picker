from dotenv import load_dotenv

import os
import subprocess
import tkinter as tk
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk

load_dotenv()
class MyApp:
	def __init__(self, root):
		self.root = root
		self.root.title("My App")
		self.root.geometry("1280x720+350+200")
		self.root.configure(bg="#0F1940")  # Set window background color to black
		
		# Background colors for each column
		left_color = "#1C2A50"  # Light blue
		right_color = "#1C2A50"  # Light pink
		
		# Padding between the window and the columns
		window_padding = 30
		# Padding between the columns
		column_padding = 10
		
		# Create styles for the frames and labels
		s = ttk.Style()
		s.configure('Left.TFrame', background=left_color)
		s.configure('Right.TFrame', background=right_color)
		s.configure('Right.TLabel', background=right_color, font=('Consolas', 26,'bold italic'), foreground="#C6C6C6")
		
		s.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10)
		s.configure('Custom.TButton', background='#000000', foreground='#000000', font=('Helvetica', 12, 'bold'), padding=10)
		
		# Create two frames to represent the columns
		self.left_frame = ttk.Frame(root, style='Left.TFrame')
		self.left_frame.pack(side="left", padx = window_padding,  pady=window_padding)
		
		self.right_frame = ttk.Frame(root, style='Right.TFrame')
		self.right_frame.pack(side="right", fill="both", expand=True, padx=(1, window_padding), pady=window_padding )
		
		#Add image
		self.add_image("./src/EnviromentPicker.png")
		
		self.text_frame = ttk.Frame(self.right_frame, style='Right.TFrame', width=232, height=84)
		self.text_frame.pack(pady=38)
		self.text_frame.pack_propagate(False)
		
		# Add the text "Choose Your Environment" to the right column using ttk.Label with custom style
		ttk.Label(self.text_frame, text="Choose Your Environment", style='Right.TLabel', anchor='center', wraplength=400).pack()
		
		self.add_button(self.right_frame, "Program", 424, 88, command=self.programming_enviroment)
		self.add_button(self.right_frame, "Play", 424, 88, command="")
	
	def add_image(self, path):
		image = Image.open(path)
		image = image.resize((570,660))
		photo = ImageTk.PhotoImage(image)
		
		image_label = tk.Label(self.left_frame, image=photo, bg="#1C2A50")
		image_label.image = photo
		image_label.pack()
	
	def add_button(self,parent,text,width,height, command=None):
		button_frame = tk.Frame(parent, width=width, height=height, bg="#4CAF50")  # Green background
		button_frame.pack_propagate(False)
		button_frame.pack(pady=51)
		
		button = tk.Button(button_frame, text=text, font=('Helvetica', 12, 'bold'), bg="#0F1940", fg="#ffffff", bd=0, command=command)
		button.pack(fill="both", expand=True)
	
	def programming_enviroment(self):

		# Abrir pestañas de chrome
		chrome_path = os.getenv("CHROME_PATH")
		urls = ["https://www.google.com", "https://www.stackoverflow.com"]
		for url in urls:
			webbrowser.get(chrome_path).open_new_tab(url)
		
		# Abrir vscode
		directory = os.getenv("PROJECTS_PATH")
		if os.path.exists(directory):
			subprocess.Popen(['code', directory])
		else:
			print(f"el directorio {directory} no existe")
def main():
	root = tk.Tk()
	app = MyApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()
