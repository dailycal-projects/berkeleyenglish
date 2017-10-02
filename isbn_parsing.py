import csv
import requests
from bs4 import BeautifulSoup

list_of_rows = []

def find(book_name):
    try:
        book_name = book_name.lower().replace(' ', '+')
        url = 'https://www.googleapis.com/books/v1/volumes?q=' + book_name
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        data = response.json()
        items = data.get('items')
        book_dict = items[0].get('volumeInfo')
        return book_dict

    except Exception:
        return {'authors': None, 'categories': None, 
                'pageCount': None, 'averageRating': None,
                'description': None, 'publishedDate': None}

def author_names(book_info):
    return book_info.get('authors')

def book_categories(book_info):
    return book_info.get('categories')

def book_pages(book_info):
    return book_info.get('pageCount')

def book_average_rating(book_info):
    return book_info.get('averageRating')

def book_description(book_info):
    return book_info.get('description')

def book_publish_date(book_info):
    return book_info.get('publishedDate')

book = find('Do Androids Dream of Electric Sheep?')
print('Author:', author_names(book))
print('Categories:', book_categories(book))
print('Pages:', book_pages(book))
print('Average Rating:', book_average_rating(book))
print('Published Data:', book_publish_date(book))
print('Description:', book_description(book))
