import os
import time


path = 'C:\\Users\\Student\\Documents\\GitHub\\The-Tech-Academy-Basic-Python-Projects\\python_Drill_Step100'


file_List = os.listdir(path)


for file in file_List:
    if file.endswith("txt"):
        abPath = os.path.join(path, file)
        print(file)

        

modification_time = os.path.getmtime(abPath)

local_time = time.ctime(modification_time) 
print("Last modification time(Local time):", local_time)

