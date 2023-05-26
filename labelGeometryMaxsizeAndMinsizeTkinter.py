from tkinter import *

izhar_root = Tk()
izhar_root.geometry("455x233")
izhar_root.title("Izhar's GUI")
izhar_root.config(background="grey")
width = izhar_root.winfo_screenwidth()
height = izhar_root.winfo_screenheight()
print(f"{width}x{height}")
# width, height 
izhar_root.minsize(200, 100)
izhar_root.maxsize(1200, 988)
Button(text="Close", command=izhar_root.destroy).pack()
izhar = Label(text="Izhar is a good boy!!!").pack()
# izhar.pack()
izhar_root.mainloop()
