# we need to install the package pyshorteners and pyperclip

import pyshorteners

url = input("Enter the long url: ")

def shorturl(url):
    short = pyshorteners.Shortener()
    print("Your shortened url is: ",short.tinyurl.short(url))

shorturl(url)