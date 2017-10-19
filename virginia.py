import csv

books = open('books_additional.csv', 'r')
reader = csv.reader(books)

new = open('books_additional_new.csv', 'w')
writer = csv.writer(new)

for row in reader:
    if row[5] == "['Virginia Woolf']":
        row[6] = 'female'
    elif row[5] == "['Virgina Woolf']":
        row[5] = ['Virginia Woolf']
        row[6] = 'female'
    writer.writerow(row)



