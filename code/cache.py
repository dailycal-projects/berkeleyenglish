import csv

#books = open('books_and_sections', errors = 'ignore')
#section_reader = csv.reader(books)

def get_students_num_cache():
    cache = {} # 'f2012': seen{}
    year = 2012 # s then f
    season = 's'
    spring = True
    combined = season + str(year)
    while combined != 'f2017':
        seen = {} # (Course Number, Section Nbr, Semester, Year): num_student
        file_name = 'grades_' + combined + '.csv'
        grades = open(file_name, errors = 'ignore')
        grades_reader = csv.reader(grades)
        i = 0
        for row in grades_reader:
            i += 1
            if i == 1:
                continue
            course_num = row[8]
            section_num = int(row[9])
            enrollment_count = int(row[1])
            class_info = (course_num, section_num, season, year)
            #print(class_info)
            if class_info in seen.keys():
                value = seen[class_info]
                #print('VALUE: ', value)
                seen[class_info] = value + enrollment_count
                #print('ENROLLMENT: ', seen[class_info])
            else:
                seen[class_info] = enrollment_count
        #print("THIS IS I: ", i)
        #print(seen)
        cache[combined] = seen
        if spring:
            season = 'f'
            spring = False
        else:
            season = 's'
            spring = True
            year += 1
        combined = season + str(year)
    return cache

def get_section_num_and_instructor_cache():
    cache = [] # [book_name, section_num, instructor]
    books = open('books_and_sections.csv', errors = 'ignore')
    reader = csv.reader(books)
    for row in reader:
        cache.append([row[5], row[3], row[4]])
    return cache
