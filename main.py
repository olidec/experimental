from bs4 import BeautifulSoup 
from requests import get 

url="https://xkcd.com/archive/"
res=get(url)
soup=BeautifulSoup(res.content, "html.parser")
hrefs=[elem['href'] for elem in soup.select(r"a[title]")] 
print(hrefs)