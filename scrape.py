import requests
from bs4 import BeautifulSoup

url = 'https://english.berkeley.edu/course_semesters/38/printable_show/all'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
heading = soup.find('h5')
print('hello')
print(soup.prettify())
