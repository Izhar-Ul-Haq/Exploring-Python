from tkinter import *
izhar_root = Tk()
izhar_root.geometry("455x233")
izhar_root.title("Izhar's GUI")
izhar_root.config(background="grey")
width = izhar_root.winfo_screenwidth()
height = izhar_root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="Close", command=izhar_root.destroy).pack()

