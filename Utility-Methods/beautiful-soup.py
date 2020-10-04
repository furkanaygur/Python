import requests
from bs4 import BeautifulSoup

site_url = "https://furkanaygur.netlify.app"
response = requests.get(site_url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

# ****************************************************************************
result = soup.prettify()
print(result)
# ****************************************************************************
result = soup.title.string
print(result)
# ****************************************************************************
result = soup.h1
print(result)
# ****************************************************************************
result = soup.find_all('header')[0].ul.find_all('li')
for menu in result:
    print(menu)
# ****************************************************************************
result = soup.div.findChildren()
print(result)
# ****************************************************************************
result = soup.header.find_next_sibling().find_next_sibling()
print(result)
# ****************************************************************************
result = soup.header.find_next_sibling().find_previous_sibling()
print(result)
# ****************************************************************************
result = soup.div.find_all('a')
for link in result:
    print(link.get('href'))
