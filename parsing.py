import csv
import xlrd
import xlwt
import numpy as np
from datascience import Table
from helper_functions import * 
from wikiapi import WikiApi # https://github.com/richardasaurus/wiki-apie

"""
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

"""

workbook = xlrd.open_workbook('demo.xls', on_demand = True) # reading books
# currently set to demo.xls because books is huge, change later.
books_sheet = workbook.sheets()[0]

semesters = [c.value for c in books_sheet.col(0)]
section = [c.value for c in books_sheet.col(1)]
class_name = [c.value for c in books_sheet.col(2)]
book_names = [c.value for c in books_sheet.col(3)]
full_names = [c.value for c in books_sheet.col(4)]

new_full_names = [] # from last,first to first,last
for name in full_names:
    if ',' in name:
        first_name = name.split(',')[1].strip()
        last_name = name.split(',')[0].strip()
        new_full_names.append(first_name + " " + last_name)
    else:
        new_full_names.append(name)

# compile into a table
books = Table().with_columns("SEMESTER", semesters,
                                    "SECTIONS", section,
                                    "CLASS NAME", class_name,
                                    "BOOK TITLES", book_names,
                                    "AUTHOR", new_full_names)

grouped = books.group(["SEMESTER", "AUTHOR"])

# "calculate" genders from Wikipedia articles
gender = []
seen = {} # memoization: author -> gender
wiki = WikiApi()
for author in grouped.column("AUTHOR"):
    if author.lower() in seen:
        gender.append(seen[author])
        continue
    try:
        results = wiki.find(author)
        wikipedia_page = wiki.get_article(results[0]).url
        # wikipedia_page = google_search(author + ' site: en.wikipedia.org', num=1).link
        g = find_gender(wikipedia_page)
        gender.append(g)
        seen[author.lower()] = g
        print(author)
    except:
        gender.append("Cannot find wikipedia page, or some other error")

# add genders column to table
grouped = grouped.with_column('GENDER', gender)

print(grouped)

"""
for name in full_names:
    if '&' in name:
        name = name.split('&')
    if 'and' in name:
        name = name.split('and')

last_names = [c.value.split(',')[0].strip() for c in books_sheet.col(4)]
#first_names = [c.value.split(',')[1].strip() for c in column]
author_names = Table().with_columns("LAST NAMES", last_names,
                                    "FULL NAMES", full_names)
last_name_count = author_names.group(0).sort(1, descending=True).relabel('count', 'COUNT')
print(last_name_count)
# find the last name
# find the first name (could be just an intial or nothing )
"""

#print(workbook.sheet_by_index(0).cell(0, 0).value)
