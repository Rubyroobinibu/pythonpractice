import csv

path="C:\\Users\\Trainee\\Desktop\\python\\birthday.csv"

'''
lines=[line for line in open(path)]
print(lines[0])
print(lines[1])

lines[0].strip()

dataset=[line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1])
print(dataset[2])
print(dataset[3])

'''
file=open(path, newline='')
reader=csv.reader(file)
header=next(reader)
data=[row for row in reader]
if data[0][2]=='1995' or data[0][1]=='aug':
  print(data[0])

newlist=[]
for row in data:
    date=row[0]
    month=row[1]
    year=int(row[2])
    newlist.append([date,month,year])

print(newlist)

returnpath="C:\\Users\\Trainee\\Desktop\\python\\returncsv.csv"
file=open(returnpath,'w',newline='')

writer=csv.writer(file)
writer.writerow(["date","month"])

for i in range(len(data)):
    row=data[i]
    date=row[0]
    month=row[1]
    writer.writerow([date,month])

file.close()





