import csv
import isbn_parsing
import viaf_parsing

books = open('books.csv')
reader = csv.reader(books)
outfile = open('books_additional.csv', 'w')
writer = csv.writer(outfile)

seen = {} # memoization, author : gender
for row in reader:
    title = row[3]
    book_data = isbn_parsing.find(title)
    author = isbn_parsing.author_names(book_data)
    print("found author:", author)

    if author:
        row[4] = ''.join(author)

    if author and len(author) == 1:
        author = author[0]
        if author in seen:
            gender = seen[author]
        else:
            gender = viaf_parsing.author_gender(
                    viaf_parsing.find_author(author[0]))
            seen[author] = gender
    else:
        gender = "Multiple Authors"

    row.append(gender)
    writer.writerow(row)
