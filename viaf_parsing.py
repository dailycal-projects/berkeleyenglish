import requests
from bs4 import BeautifulSoup

def find_author(author_name):
    try:
        url = 'http://www.viaf.org/viaf/search?query=local.personalNames+=+"' + author_name+ '"&maximumRecords=1&sortKeys=holdingscount&httpAccept=application/json'
        response = requests.get(url)

        data = response.json()['searchRetrieveResponse']['records']
        author_url = data[0]['record']['recordData']['Document']["@about"]
        return author_url

    except Exception:
        return None

def author_gender(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.content, "html.parser")
    personal_info = soup.find(id='personalinfo')
    text = personal_info.find('h4').get_text().lower().split()
    if 'female' in text:
        return 'female'
    elif 'male' in text:
        return 'male'
    else:
        return 'unknown'

