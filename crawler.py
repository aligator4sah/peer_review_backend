from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)

title_index = html.find("<title>")
title_index

title = html[start_index:end_index]
title

###############
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
soup.find_all("img")