import csv

with open('data01.csv', newline='', encoding='UTF-8') as csvfile:
    readFile = csv.reader(csvfile)
    for row in readFile:
        print(row)