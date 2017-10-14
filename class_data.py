import csv
from pathlib import Path

### COMPILING CLASS DATA BY SECTION FROM GRADING SPREADSHEET
files = ['class_data/grades_f' + str(y) + '.csv' for y in range(2012, 2017)]
files.extend(['class_data/grades_s' + str(y) + '.csv' for y in range(2012, 2018)])

combined = csv.writer(open('all_enrollment_numbers.csv', 'w'))
combined.writerow(['Semester', 'Course', 'Section', 'Enrollment'])

count = {} # dictionary of {'Fall/SpringYear_ English Course_Sec#': # enrolled }
for f in files:
    year = 'Fall ' + f[-8:-4] if f[-9] == 'f' else 'Spring ' + f[-8:-4]
    print(year)
    f = csv.reader(open(f, 'r'))
    
    firstline = True

    for row in f:
        # skip header row
        if firstline:
            firstline = False
            continue
        # Each row corresponds to a different grade for a given course.
        # 1: num of people receiving grade, 7: 'English', 8: Course number, 9: section number
        # Using these files instead of other, because specification by course number
        key = year + '_' + row[7] + ' ' + row[8] + '_' + str(int(row[9])) # removing leading 0s
        if key not in count:
            count[key] = 0
        count[key] += int(row[1])

for k in count.keys():
    combined.writerow(k.split('_') + [count[k]])


### ADDING TO BOOKS_ADDITIONAL.CSV
reader = csv.reader(open('books_additional.csv', 'r', errors='ignore'))
writer = csv.writer(open('new_books_additional.csv', 'w'))

# title row
writer.writerow(['Semester', 'Class', 'Class Number', 'Section Number', 'Title', 'Author(s)', 'Gender', 'Number Students'])

for row in reader:
    key = row[0] + '_' + row[2] + '_'+ row[3]
    try:
        row.append(count[key])
    except KeyError:
        pass
    writer.writerow(row)


        
