import csv


lines = open(path)

print(lines[0])


import csv
file = open("Salary_Data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()