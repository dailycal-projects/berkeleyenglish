import csv
import cache

books = open('books_additional_copy.csv', errors = 'ignore')
reader = csv.reader(books)
outfile = open('books_additional_with_sections.csv', 'w')
writer = csv.writer(outfile)

sect_num_instr_cache = cache.get_section_num_and_instructor_cache()

index = 0
for row in reader:
    try:
        book_name = row[3]
        index_max = 0
        passed = True
        while sect_num_instr_cache[index][0] != book_name and index_max < 10: # [book_name, section_num, instructor]
            index += 1
            if index_max == 9:
                index -= 10
                passed = False
            index_max += 1
        if passed:
            section_num = sect_num_instr_cache[index][1]
            instructor = sect_num_instr_cache[index][2]
        else:
            section_num = 'FIX ME'
            instructor = 'FIX ME'
        row.append(section_num)
        row.append(instructor)
    except:
        continue
    writer.writerow(row)




"""
for key in cache.keys():
    for class_info in cache[key]:
        print(class_info, ': ', cache[key][class_info])

"""
