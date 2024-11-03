#Import Tkinter modules 
import tkinter as tk

import requests
from bs4 import BeautifulSoup

#Root window    
root = tk.Tk()

#Specify root window attributes 
root.title("Weather App")
root.geometry('300x400')

#Widgets    

#Labels

lbl1 = tk.Label(root , text = "Welcome to Weather App!")
lbl2 = tk.Label(root , text = "Enter a City: ")
lbl3 = tk.Label(root , text = "")
lbl4 = tk.Label(root , text = "")
lbl5 = tk.Label(root , text = "")
lbl6 = tk.Label(root , text = "")
lbl7 = tk.Label(root , text = "" )
lbl8 = tk.Label(root , text = "" , wraplength = 200)

#Entry  
ent = tk.Entry(root , width = 10)

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
    lbl7text = "Other Data : "
    lbl8text = other_data
    lbl3.configure(text = lbl3text)
    lbl4.configure(text = lbl4text)
    lbl5.configure(text = lbl5text)
    lbl6.configure(text = lbl6text)
    lbl7.configure(text = lbl7text)
    lbl8.configure(text = lbl8text)

#Button 
btn = tk.Button(root , text= "Get Weather" , command = clicked)

lbl1.pack()
lbl2.pack()
ent.pack()
btn.pack()
lbl3.pack()
lbl4.pack()
lbl5.pack()
lbl6.pack()
lbl7.pack()
lbl8.pack()

#Execute    
root.mainloop()