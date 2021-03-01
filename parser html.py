from urllib.request import urlopen
from bs4 import BeautifulSoup

base_URL = "http://olympus.realpython.org"
address = base_URL + "/profiles"
htmlPage = urlopen(address)
htmlText = htmlPage.read().decode("utf-8")

soup = BeautifulSoup(htmlText, "html.parser")

for anchor in soup.find_all("a"):
    linkAdd = base_URL + anchor['href']
    print(f"--- fetching {linkAdd}: ")

    linkPage = urlopen(linkAdd)
    linkText = linkPage.read().decode('utf-8')
    linkSoup = BeautifulSoup(linkText, 'html.parser')
    print(linkSoup.getText())