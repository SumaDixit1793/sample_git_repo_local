import csv
def file_read_csv(file_path = '/mnt/c/Users/dsuma/Documents/Python_Practise/sample.csv'):
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(" Row = ",row);
            line_count += 1
        print(f'Processed {line_count} lines.')