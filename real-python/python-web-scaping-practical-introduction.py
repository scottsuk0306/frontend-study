from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Extract all the text from the document and automatically remove any HTML tags.
print(soup.get_text())

# Extract the URL of the image.
print(soup.find_all("img"))

# Extract the title of the page.
print(soup.title)

# Exercise: Parse HTML with Beautiful Soup
url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all("a"):
    link_url = link["href"]
    print(link_url)
    
# Interact with HTML forms
import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url)
print(page)
print(page.soup)

# Submit the form with mechanical soup
import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)