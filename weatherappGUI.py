#Import Tkinter modules 
from tkinter import *

import requests
from bs4 import BeautifulSoup

#Root window    
root = Tk()

#Specify root window attributes 
root.title("Weather App")
root.geometry('300x400')

#Widgets    

#Label
lbl1 = Label(root , text = "Enter a City: ")
lbl1.grid(row = 0)

lbl2 = Label(root , text = "")
lbl2.grid(row = 3)

#Entry  
ent = Entry(root , width = 10)
ent.grid(row = 1)

#Function   
def clicked():
    city = ent.get()
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html , 'html.parser')

    #Get tempereature   
    temp = soup.find('div' ,  attrs = {'class' : 'BNeawe iBp4i AP7Wnd'}).text
    print("Temperature is " , temp)
    #print(res.text)

    lbl2text = "Temperature of city " + city + " is " + temp
    lbl2.configure(text = lbl2text)

#Button 
btn = Button(root , text= "Get Weather" , command = clicked)
btn.grid(row = 2)

#Execute    
root.mainloop()