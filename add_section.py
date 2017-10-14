""" Adds section number from books.csv to
books_additional.csv by checking the titles
to ensure that we are staying in sync between
both files (for some reason, the number of lines
don't match up... this could due to cleanup of 
error-y lines. 
"""

import csv

books = open('books.csv', errors='ignore')
additional = open('books_additional.csv', errors='ignore')
outfile = open('new_books_additional.csv', 'w')

books = csv.reader(books)
additional = csv.reader(additional)
writer = csv.writer(outfile)

b_all = list(books)
a_all = list(additional)

b_i, a_i = 0, 0

try:
    while True:
        b_row, a_row = b_all[b_i], a_all[a_i]

        b_info = [b_row[0], b_row[1], b_row[2], b_row[4]]
        a_info = [a_row[0], a_row[1], a_row[2], a_row[3]]
    
        if b_info == a_info:
            a_info.insert(3, b_row[3])
            a_info.extend(a_row[4:])
            writer.writerow(a_info)
    
            b_i += 1
            a_i += 1
    
        else:
            next_b_row = b_all[b_i + 1]
            next_a_row = a_all[a_i + 1]
    
            next_b_info = next_b_row[0:3] + [next_b_row[4]]
            next_a_info = next_a_row[0:4]
    
            if next_b_info == a_info:
                b_i += 1
                print("advancing books")

            elif next_a_info == b_info:
                a_i += 1
                print("advancing additional")

            else:
                print("rows don't match up, increasing both by one")
                print(b_i, b_row)
                print(a_i, a_row)
                a_info.insert(3, b_row[3])
                a_info.extend(a_row[4:])
                a_info.append("check this")
                writer.writerow(a_info)
                
                a_i += 1
                b_i += 1

except IndexError:
    print("done")

