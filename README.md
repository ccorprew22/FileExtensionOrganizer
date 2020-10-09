# FileExtensionOrganizer

+ Python script that takes three inputs: The file path to be organized, the file path to put the new directories, and how long you want the script to run in seconds. The program takes each file within the orignal path, uses regex to find see if it has an extension, then places that file in a folder of other files sharing the same extensions. Control+C to stop program.

+ NOTE: If you want the new directories to be put in the same path then just put the same path in both inputs. Also the time will keep the program running actively on the desired path until time expires, so when the path is ever modified, files will be sorted automatically.

# Modules used:
+ re
+ os
+ time
+ watchdog
+ random
+ string
+ tkinter
