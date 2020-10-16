import subprocess,sys
def install(package):
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])

install("bs4")
install("requests")

from bs4 import BeautifulSoup

import requests
page = requests.get("https://www.scorespro.com/rss2/live-cricket.xml")
soup = BeautifulSoup(page.content, 'html.parser')
p=soup.find_all('title')[2].get_text()
#print(page)
#print(page.content)
#print(soup.prettify())
print(p)
