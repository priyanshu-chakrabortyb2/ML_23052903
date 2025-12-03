import csv

with open(r"C:\Users\KIIT0001\Downloads\annual-enterprise-survey-2024-financial-year-provisional.csv", "r") as rcsv:
    csv_reader=csv.reader(rcsv)
    field=next(csv_reader)
    print(field)
    for lines in csv_reader:
        print(lines)