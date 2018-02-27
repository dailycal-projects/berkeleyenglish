# For working with multiple authors.
import viaf_parsing
import csv
import ast

original = open('books_additional.csv', 'r')
new = open('books_additional_new.csv', 'w')

reader = csv.reader(original)
writer = csv.writer(new)

header = True

for row in reader:
    if header:
        header = False
        writer.writerow(row)
        continue

    if row[6] != 'Multiple Authors':
        writer.writerow(row)
        continue

    authors = ast.literal_eval(row[5])
    unknown = False
    male, female = 0, 0
    for author in authors:
        gender = viaf_parsing.author_gender(viaf_parsing.find_author(author))
        if gender == 'female':
            female += 1
        elif gender == 'male':
            male += 1
        else:
            unknown = True
            break

    if unknown:
        row[6] = "gender could not be found"
    elif female > 0 and male == 0:
        row[6] = "female"
    elif female == 0 and male > 0:
        row[6] = "male"
    else:
        row[6] = "varying genders"

    writer.writerow(row)
