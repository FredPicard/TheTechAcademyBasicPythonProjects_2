


import sqlite3

X = sqlite3.connect('fileList.db')





with X:
    cur = X.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_List( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Lname TEXT \
        )")
    X.commit()
X.close() 


    
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

print(fileList)

 
   
for file in fileList:
    if file.endswith(".txt"):
        print(file)




        X = sqlite3.connect('fileList.db')
        with X:
            cur = X.cursor()
            cur.execute("INSERT INTO tbl_List(col_Lname) VALUES (?)", (file,))
            X.commit
        X.close

