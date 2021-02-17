import requests ,urllib,os
from bs4 import BeautifulSoup

os.system('cls')

url = 'https://en.wikipedia.org/wiki/Google'
response = requests.get(url)  #response contains the response of the request

soup = BeautifulSoup(response.text,'html.parser')  #soup will contain page source(all html document)  / it will contain every html content shows us in inspect

#to get a tag with soup: soup: <html tag name>, ex. soup.p (para tag)
#but soup.p will return string including <p> tags, so to remove/avoid that use: soup.p.text

ptag = list(soup.findAll('p'))  #findAll('<html tag to find>')   

for i in range(len(ptag)):
    print(ptag[i].text)