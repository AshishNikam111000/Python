import pandas as pd
import requests ,urllib,os
from bs4 import BeautifulSoup

os.system('cls')

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
response = requests.get(url)  

soup = BeautifulSoup(response.text,'html.parser') 

table = list(soup.findAll('span',{'class':'u-hide-phablet'}))
teamlist = []

n = len(table)
for i in range(n-1):
    #print(i+1,table[i].text)
    teamlist.append([i+1,table[i].text])
#print(teamlist)

dataframe = pd.DataFrame(teamlist,columns=['Rank','Team_Name'])
#print(dataframe)

dataframe.to_csv('Sample CSV file.csv')

