import sys
import os
from PIL import Image
import tkinter as tk
from tkinter import messagebox

def convert_to_favicon(image_path):
    try:
        img = Image.open(image_path)
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        directory = os.path.dirname(image_path)
        output_path = os.path.join(directory, 'favicon.ico')
        img.save(output_path, format='ICO', sizes=sizes)
        tk.Tk().withdraw()
        messagebox.showinfo('Success', 'Favicon created successfully')
    except Exception as e:
        tk.Tk().withdraw()
        messagebox.showerror('Error', str(e))

def main():
    if len(sys.argv) != 2:
        tk.Tk().withdraw()
        messagebox.showerror('Usage', 'Usage: python favpycon.py <image_path> or drag an image to this executable')
        return
    
    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        tk.Tk().withdraw()
        messagebox.showerror('Error', 'Image path does not exist')
        return

    convert_to_favicon(image_path)

if __name__ == '__main__':
    main()
