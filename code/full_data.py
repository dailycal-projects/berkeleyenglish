import csv
import cache

books = open('books_additional_with_sections.csv', errors = 'ignore')
reader = csv.reader(books)
outfile = open('books_additional_with_everything.csv', 'w')
writer = csv.writer(outfile)

students_num_cache = cache.get_students_num_cache()
# cache - 'f2012': seen{}
# seens{} - (Course Number, Section Nbr, Semester, Year): num_student

for key in students_num_cache.keys():
    for class_info in students_num_cache[key]:
        print(class_info, ': ', students_num_cache[key][class_info])
print('--------------------------')
for row in reader:
    season, year = row[0].split()
    semester_tag = (season.lower())[0]
    english, course_num = row[2].split()
    section_num = int(row[6])
    year_sem_tag = semester_tag + year
    year = int(year)
    tag = (course_num, section_num, semester_tag, year)
    print(tag)
    #print(tag)
    #print(students_num_cache[year_sem_tag][tag])
    try:
        num_student = students_num_cache[year_sem_tag][tag]
    except:
        num_student = 'FIX ME'
    row.append(num_student)
    writer.writerow(row)
