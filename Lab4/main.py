# Joseph Sepe
# Spring 2021 Lab 4 dictionaries and CSV files

import csv

def main():
    # lists of data
    Lnumbers = ["L00312", "L00526", "L00497", "L00274", "L00456", "L00963"]
    Names = ["Bob", "Sue", "Mary", "Bill", "Ann", "Fred"]
    GPA = [3.4, 3.9, 4.1, 3.8, 3.5, 2.6]

    # dynamically create dictionary from lists
    students = {}
    for idx, x in enumerate(Lnumbers):
        students[idx] = {'Lnumber': Lnumbers[idx], 'Name': Names[idx],'GPA': GPA[idx]}

    # open or create the file
    with open('students.csv', mode='w', newline='') as students_file:
        fieldnames = ['Lnumber', 'Name', 'GPA']

        # reference https://docs.python.org/3/library/csv.html#csv.DictWriter
        writer = csv.DictWriter(students_file, fieldnames=fieldnames)

        writer.writeheader()
        # write row for each item in students
        for id, student in students.items():
            writer.writerow(students[id])
        
        # close the file
        students_file.close()


if __name__ == '__main__':
    main()
