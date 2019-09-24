import os
import time
import shutil
import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import filedialog



X = sqlite3.connect('DirList.db')

with X:
    cur = X.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_List( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_File TEXT, \
                col_Time TEXT \
                )")
    X.commit()
X.close()

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

        
       
        
        self.btn_1 = Button (self.master, text="Source...", width=20, height=1,command=self.open)
        self.btn_1.grid(row=5, column=1, padx=(20,10), pady=(70,0), sticky=NE)
        
        self.btn_2 = Button (self.master, text="Destination...", width=20, height=1,command=self.open_1)
        self.btn_2.grid(row=6, column=1, padx=(20,10), pady=(10,0), sticky=SE)
        
        self.btn_3 = Button (self.master, text="Check Files...", width=20, height=1,command=self.get_txt)
        self.btn_3.grid(row=7, column=1, padx=(20,10), pady=(10,0), sticky=SE)

        self.btn_4 = Button (self.master, text="Close Program", width=20, height=1, command=root.destroy)
        self.btn_4.grid(row=7, column=4, padx=(20,10), pady=(20,10), sticky=E)


    def open(self):
        source =  filedialog.askdirectory()
        file = self.varbtn_1.set(source)
   
              
           
    def open_1(self):
        destination = filedialog.askdirectory()
        file = self.varbtn_2.set(destination)

 

        
    def get_txt(self):
        source = self.varbtn_1.get()


        destination = self.varbtn_2.get()

        path = source
        file_List = os.listdir(path)

        #path = source
        #file_List = os.listdir(path)


        for file in file_List:
            if file.endswith(".txt"):
                print(file)


                abPath = os.path.join(path, file)
                modification_time = os.path.getmtime(abPath)
                local_time = time.ctime(modification_time)
                print("Last modification time(Local time):", local_time)


                X = sqlite3.connect('DirList.db')
                with X:
                    cur = X.cursor()
                    cur.execute("INSERT INTO tbl_List(col_File,col_Time) VALUES (?,?)",(file,local_time))
                    X.commit
                X.close
            


                     

                abPath = os.path.join(path, file)

                shutil.move(abPath, destination)                    


                     
    if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

