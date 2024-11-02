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
lbl1 = Label(root , text = "Welcome to Weather App!")
lbl1.grid(row = 0)

lbl2 = Label(root , text = "Enter a City: ")
lbl2.grid(row = 1)

lbl3 = Label(root , text = "")
lbl3.grid(row = 4)

lbl4 = Label(root , text = "")
lbl4.grid(row = 5)

lbl5 = Label(root , text = "")
lbl5.grid(row = 6)

lbl6 = Label(root , text = "")
lbl6.grid(row = 7)

lbl7 = Label(root , text = "")
lbl7.grid(row = 8)

#Entry  
ent = Entry(root , width = 10)
ent.grid(row = 2)

#Function   
def clicked():
    city = ent.get()
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html , 'html.parser')

    #Get tempereature   
    temp = soup.find('div' ,  attrs = {'class' : 'BNeawe iBp4i AP7Wnd'}).text

    #Get sky description    
    str = soup.find('div' , attrs = {'class' : 'BNeawe tAd8D AP7Wnd'}).text

    #Get other data 
    listdiv = soup.find_all('div' , attrs = {'class' : 'BNeawe s3v9rd AP7Wnd'})

    #Particular list with required data 
    strd = listdiv[5].text

    #Formatting the string  
    pos = strd.find('Wind')
    other_data = strd[pos:]

    #Format sky description data    
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    lbl3text = "City Data of " + city
    lbl4text = "Temperature : " + temp
    lbl5text = "Time : " + time
    lbl6text = "Sky Description : " + sky
    lbl7text = "Other Data : " + other_data
    lbl3.configure(text = lbl3text)
    lbl4.configure(text = lbl4text)
    lbl5.configure(text = lbl5text)
    lbl6.configure(text = lbl6text)
    lbl7.configure(text = lbl7text)

#Button 
btn = Button(root , text= "Get Weather" , command = clicked)
btn.grid(row = 3)

#Execute    
root.mainloop()