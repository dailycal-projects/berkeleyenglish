import csv
import requests
from bs4 import BeautifulSoup

url = 'https://english.berkeley.edu/course_semesters/38/printable_show/all'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
class_line = soup.find_all('hr')

list_of_rows = []

for c in class_line:
    try:
        course_name_element = c.find_next_sibling()
        course_logistics_element = course_name_element.find_next_sibling()
        course_number_element = course_logistics_element.find('h4')

        book_list_header = course_logistics_element.find_next_sibling().get_text()
        if book_list_header != 'Book List':
            continue

        book_list_element = course_logistics_element.find_next_sibling().find_next_sibling()
        book_list = book_list_element.get_text().split(';')

        for author_book in book_list:
            book_info_row = [] # each row includes course name, number, then book and author
            book_info_row.extend([course_name_element.get_text().strip(), course_number_element.get_text().strip()]) 

            try: 
                if 'Recommended' in author_book:
                    continue
                author, book = author_book.split(':', 1)
                book_info_row.append(book.strip())
                book_info_row.append(author.strip())
                
                list_of_rows.append(book_info_row)
            except:
                # jank debugging
                # print("error:", author_book)
                continue
    except:
        continue

outfile = open("books.csv", "w")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
