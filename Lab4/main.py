import csv

def main():
    # define the dictionary
    students = {
        1: {
            'Name': 'Bob', 
            'Lnumber': 'L00312', 
            'GPA': 3.4
        },
        2: {
            'Name': 'Sue', 
            'Lnumber': 'L00526', 
            'GPA': 3.9
        },
        3: {
            'Name': 'Mary', 
            'Lnumber': 'L00497', 
            'GPA': 4.1
        },
        4: {
            'Name': 'Bill', 
            'Lnumber': 'L00274', 
            'GPA': 3.8
        },
        5: {
            'Name': 'Ann', 
            'Lnumber': 'L00456', 
            'GPA': 3.5
        },
        6: {
            'Name': 'Fred', 
            'Lnumber': 'L00963', 
            'GPA': 2.6
        }
    }

    # open or create the file
    with open('students.csv', mode='w') as students_file:
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
