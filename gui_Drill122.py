# Python Ver:   3.5.1
#
# Author:       Fred Picard
#
# Purpose:      Drill on Tkinder module
#
# Tested OS:  This code was written and tested to work with Windows 10.



import tkinter as tk
from tkinter import *
import filelist




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master) 

        self.master = master
        self.master.minsize(500,500) #(Height, Width)
        self.master.maxsize(500,500)
        self.master.title("Check Directory")
        self.master.configure(bg="lightgrey")
        
        self.varbtn_1 = StringVar()
        self.varbtn_2 = StringVar()


        self.btn_1 = Button (self.master, text="Browse...", width=20, height=5,command=self.submit)
        self.btn_1.grid(row=20, column=1, padx=(20,10), pady=(70,0), sticky=NE) 


        self.entry_1 = Entry(self.master,text=self.varbtn_1, font=("Helvetica", 16), fg="black", bg="white", width="13",)
        self.entry_1.grid(row=17, column=1, padx=(1,1),pady=(10,0))

        self.lstList1 = Listbox(self.master,exportselection=0, width=40, height=20)
        self.lstList1.grid(row=15,column=10,rowspan=12,columnspan=8,padx=(40,0),pady=(40,0),sticky=N+E)


        
    def addToList(self):
        var_fname = self.txt_filePath.get()

       

    def submit(self):
        txt = self.varbtn_1.get()


      









        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() 
