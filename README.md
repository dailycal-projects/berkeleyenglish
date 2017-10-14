# berkeleyenglish

### Files:

**scrape.py** - Scrapes data off UC Berkeley's English Department website, which contains a list of required readings for each semester's English classes. Puts data in books.csv

**isbn_parsing.py** - Uses Google Books api to search book title and retrieve author information, including correct spelling of author's name.

**viaf_parsing.py** - Uses VIAF api to find author's gender from the profile associated with their name

**main.py** - Ties together isbn_parsing.py and viaf_parsing.py to record information associated with class and author from books.csv into additional_books.csv

**class_data.py** - Uses class_data files to create enrollment per class section in all_enrollment_numbers.csv, then adds to books_additional.csv

**books.csv** - Initial data scraped from Berkeley's English department website

**books_additional.csv** - books.csv fleshed out with correct author spelling and gender, section number, and enrollment

**all_enrollment_numbers.csv** - Number enrolled in each class by section number, class, semester

**class_data** - Data on class enrollment in Berkeley

**archive** - Old code, data that is no longer needed
