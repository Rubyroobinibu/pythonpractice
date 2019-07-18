import csv
from datetime import datetime

path="C:\\Users\\Trainee\Desktop\\python\\googlesheet.csv"
file=open(path, newline='')
reader=csv.reader(file)
header=next(reader)
data=[row for row in reader]

returnpath="C:\\Users\\Trainee\\Desktop\\python\\resultsheet.csv"
file=open(returnpath,'w',newline='')

writer=csv.writer(file)
writer.writerow(["date","cost"])

for i in range(len(data)):
    row=i
    d=row[0]
    dateobj = datetime.strptime(d, '%m/%d/%Y').date()
    # date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y)
    cost=row[1]
    if float(cost)>700.00:
        writer.writerow([dateobj,float(cost)])
        print([datetime.strptime(d, '%m/%d/%Y'),float(cost)])
        

file.close()