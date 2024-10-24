#Import requests module 
import requests

#Send request to get IP location info   
resIpinfo = requests.get('https://ipinfo.io/')
#Receive response in JSON format    
data = resIpinfo.json()

#Extract city from the data 
#print(data)
citydata = data['city']
print("Current city is " , citydata)

#Passing the city name to URL to get city weather data  
url = 'https://wttr.in/{}'.format(citydata)
resWeather = requests.get(url)

print(resWeather.text)