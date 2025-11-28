import csv

with open(r"C:\Users\KIIT0001\Desktop\ML_35\ML\my_data.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
