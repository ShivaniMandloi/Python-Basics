# Functions + Module = Standard Library
# These are some standard Library examples

# 1. os provides a platform-independent way to interact with your underlying operating system
from os import getcwd()
xyz = getcwd()                                                                         # this is called invoking the function and will give current working directory


#sys module exists to help you learn more about your interpreter’s system
>>> import sys
>>> sys.platform 
'win32'
>>> print(sys.version)
3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]

import os
>>> os.environ                                                                          # gives you all system environment variables
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\dell\\AppData\\Roam

>>> os.getenv('HOME')                                                                   # You can also access specific variable using getenv function
'C:\\Users\\dell'
         
# Another important module we usually need is datetime module
import datetime
>>> datetime.date.today()                                                                # gives current date
datetime.date(2023, 8, 19)
>>> datetime.date.today().day                                                            # This is simply extracting component of the above output
19
>>> datetime.date.today().month

>>> datetime.date.isoformat(datetime.date.today())                                       # if you need date in string format usually we need this whenever we  need any datestamp to store any file
'2023-08-19'

Below is the short example how it is used as a timestamp

import datetime

# Get the current date and time
current_date = datetime.datetime.now()

# Format the date as a string
date_stamp = current_date.strftime("%Y-%m-%d_%H-%M-%S")

# Create a sample content to write into the file
file_content = "This is some content for the file."

# Define the file name using the date stamp
file_name = f"file_{date_stamp}.txt"

# Write the content to the file
with open(file_name, "w") as file:
    file.write(file_content)

print(f"File '{file_name}' with current date stamp created.")




