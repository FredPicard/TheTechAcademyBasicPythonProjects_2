#
# Python Ver:   3.5.1
#
# Author:       Fred Picard
#
# Purpose:      Drill on Tkinder module
#
# Tested OS:  This code was written and tested to work with Windows 10.



import tkinter as tk
from tkinter import *





class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master) 

        
        self.master = master
        self.master.minsize(800,250) #(Height, Width)
        self.master.maxsize(800,250)
        self.master.title("Check Files")
        self.master.configure(bg="lightgrey")
      

        self.varbtn_1 = StringVar()
        self.varbtn_2 = StringVar()
        self.varbtn_3 = StringVar()

        self.entry_1 = Entry(self.master,text=self.varbtn_1, font=("Helvetica", 16), fg="black", bg="white", width="48")
        self.entry_1.grid(row=5, column=4, padx=(10,10), pady=(70,0))

        self.entry_2 = Entry(self.master,text=self.varbtn_2, font=("Helvetica", 16), fg="black", bg="white", width="48" )
        self.entry_2.grid(row=6, column=4, padx=(10,10), pady=(10,0))

        
        self.btn_1 = Button (self.master, text="Browse...", width=20, height=1,command=self.submit)
        self.btn_1.grid(row=5, column=1, padx=(20,10), pady=(70,0), sticky=NE)
        
        self.btn_2 = Button (self.master, text="Browse...", width=20, height=1, command=self.submit)
        self.btn_2.grid(row=6, column=1, padx=(20,10), pady=(10,0), sticky=SE)


        self.btn_3 = Button (self.master, text="Check for files...", width=20, height=3, command=self.check)
        self.btn_3.grid(row=7, column=1, padx=(20,10), pady=(20,10), sticky=W)

        self.btn_4 = Button (self.master, text="Close Program", width=20, height=3, command=root.destroy)
        self.btn_4.grid(row=7, column=4, padx=(20,10), pady=(20,10), sticky=E)



    def submit(self):
        txt = self.varbtn_1.get()
        msg = ("Let me browse for you")
        print(msg)


    def check(self):
        txt = self.varbtn_3.get()
        msg = ("Checking my files")
        print(msg)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    
           
   
  
   

           

 
                     
             














