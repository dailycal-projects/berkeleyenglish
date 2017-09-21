import requests
from bs4 import BeautifulSoup

url = 'https://english.berkeley.edu/course_semesters/38/printable_show/all'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
class_line = soup.find_all('hr')

list_of_rows = []

for c in class_line:
    course_name_element = c.find_next_sibling()
    course_logistics_element = course_name_element.find_next_sibling()
    course_number_element = course_logistics_element.find('h4')


    book_list_element = course_logistics_element.find_next_sibling().find_next_sibling()
    book_list = book_list_element.get_text().split(';')

    for book_author in book_list:
        book_info_row = [] # each row includes course name, number, then book and author
        print(course_number_element)
        book_info_row.extend([course_name_element.get_text(), course_number_element]) 

        try: 
            book, author = book_author.split(':', 1)
            # print(book, author)
            book_info_row.append(book)
            book_info_row.append(author)
            
            list_of_rows.append(book_info_row)
        except:
            # jank debugging
            # print("error:", book_author)
            1 + 1

print(list_of_rows)
