import csv
lists=[]
maps={}
with open("person.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    if row[0] not in lists:
        lists.append(row[0])
    if row[1] not in lists:
        lists.append(row[1])
i=1
c=''
for j in lists[2:]:
  c=c+str(i)+','+j+'\n'
  i=i+1




filez=open('mappings.csv','w')
filez.write(c)
filez.close()
