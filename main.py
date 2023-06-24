import csv

with open('covid-data.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    count = 0
    dates_Aze = []
    new_Cases_Aze = []


    for row in csvreader:
        country = row[2]
        new_Cases = row[5]
        date = row[3]
        
        if country=="Azerbaijan":
            dates_Aze.append(date)
            new_Cases_Aze.append(int(round(float(new_Cases))))
