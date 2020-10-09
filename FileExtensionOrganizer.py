import re
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import random
import string
import tkinter as tk

class MyHandler(FileSystemEventHandler):
    def __init__(self, file_origin, file_destination):
        self.file_origin = file_origin
        self.file_destination = file_destination
    def dispatch(self, event):
        for filename in os.listdir(self.file_origin):
            #print(filename)
            try:
                ext = re.search(r"\.[^\.]+$", filename).group()
                ext = ext[1:] #extenstion          
                if os.path.isdir(self.file_destination+"/"+ext) == False:
                    #print('here')
                    os.mkdir(self.file_destination + "/" + ext) #makes folder if doesnt exist            
                src = self.file_origin+"/"+filename
                new_destination = self.file_destination+"/"+ext+"/"+filename
                os.rename(src, new_destination)
            except AttributeError:
                continue
       

root = tk.Tk()
tk.Label(root, text="Origin").grid(row=0)
tk.Label(root, text="Destination").grid(row=1)
tk.Label(root, text="Time To Run").grid(row=2)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

folder_to_track = None
folder_destination = None
t = 10
def getFiles():
    global folder_to_track
    global folder_destination
    global t
    folder_to_track = entry1.get()
    folder_destination = entry2.get()
    t = entry3.get()
    t = int(t)
    root.destroy()

button = tk.Button(root, text="Quit", command=root.destroy).grid(row=3)
button = tk.Button(root, text="Enter", command=getFiles).grid(row=3, column=1)

root.mainloop()

event_handler = MyHandler(folder_to_track, folder_destination)
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

throwaway =  "".join(random.choice(string.ascii_lowercase) for i in range(10))
os.mkdir(folder_to_track + "/" + throwaway) #to start function
os.rmdir(folder_to_track + "/" + throwaway) #get rid of folder

try:
    while True:
        time.sleep(t)
        observer.stop()
        break
except KeyboardInterrupt:
    observer.stop()
observer.join()

