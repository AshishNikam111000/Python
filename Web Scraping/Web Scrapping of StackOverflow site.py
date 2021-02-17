import requests ,urllib.request, os
from bs4 import BeautifulSoup

os.system('cls')
#print(os.getcwd())

url = 'https://stackoverflow.com/questions/604802/python-finding-an-element-in-a-list'
response = requests.get(url)  
#print(response)

soup = BeautifulSoup(response.text,'html.parser') 

#soup.prettify(): this method will give us the Indented page source, so the page source is readable. And the we can print it.

answers = soup.findAll('div',{'class':'answer'})
#print(answers)

for ans in answers:
    vote = ans.find('div',{'class':'js-vote-count'}).text
    solution = ans.find('div',{'class':'post-text'}).text
    if (int(vote)>15):
        print(vote ,solution)