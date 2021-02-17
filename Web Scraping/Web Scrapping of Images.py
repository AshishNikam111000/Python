import requests ,urllib.request, os
from bs4 import BeautifulSoup

os.system('cls')
#print(os.getcwd())

url = 'https://www.pdfdrive.com/'
response = requests.get(url)  
#print(response)

soup = BeautifulSoup(response.text,'html.parser') 

#soup.prettify(): this method will give us the Indented page source, so the page source is readable. And the we can print it.

frames = soup.findAll('div',{'class':'file-left'})  #we should take 1st class that is contaning the <img> tag.
#print(frames)

for frame in frames:
    photo_url = frame.img['src']
    print(photo_url)
    name = photo_url.split('/')
    name = name[-1]
    urllib.request.urlretrieve(photo_url,name)
