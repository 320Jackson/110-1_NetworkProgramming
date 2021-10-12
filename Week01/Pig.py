import csv
with open('pig.csv', encoding='Big5') as csvfile:
    readFile = csv.reader(csvfile)
    flag = 0
    Num = 0
    Total = 0
    TotalPrice = 0
    Highest = 0
    Lowest = 2147483647.0
    for row in readFile:
        if flag != 0:
            Num += float(row[3]) + float(row[6])
            Total += int(row[0])
            TotalPrice += float(row[0]) * float(row[2])
            if int(row[0]) != 0 and Lowest > float(row[2]):
                Lowest = float(row[2])
            if(Highest < float(row[1])):
                Highest = float(row[1])
        flag += 1
    
    print(Num)
    print(Highest)
    print(Lowest)
    print(Total)
    print(TotalPrice)
    print(TotalPrice / Total)