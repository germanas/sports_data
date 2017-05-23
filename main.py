import requests
from bs4 import BeautifulSoup

url = "https://rugby.statbunker.com/alltimestats/AllTimeTryScorers?comp_code=8217249&club_id=54"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

column_names = (soup.find_all('tr'))[2:]
for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    #print ((tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text))

print (tds)