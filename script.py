import os
import json
import datetime
import dateutil
import urllib
import bs4


# script.py
filename = 'output.txt'
content = 'Hello, GitHub Actions! This file was created by a Python script. v0.5'

try:
    with open(filename, 'w') as f: # Open in write mode ('w') to create/overwrite
        f.write(content)
    print(f"Successfully wrote to {filename}")
except IOError as e:
    print(f"Error writing to file: {e}")
    exit(1)
