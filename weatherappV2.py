import requests

city = input('Enter your city: ')

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

print(res.text)