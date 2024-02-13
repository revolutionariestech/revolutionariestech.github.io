# found here : https://www.youtube.com/watch?v=A1s1aGHoODs

from bs4 import BeautifulSoup
import requests

website = "https://gwu.campuslabs.com/engage/organization/revtech/roster"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content,"lxml")
print(soup.prettify())