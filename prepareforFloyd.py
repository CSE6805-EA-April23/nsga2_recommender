import csv
import math

persons={}
max_val=0
minitime=1
with open("corrected_mappings.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in  csvreader:
        persons[row[1]]=(row[0],row[2])
        if float(row[2])>max_val:
            max_val=float(row[2])

cs=''
with open("person.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        cs=cs+persons[row[0]][0]+' '+persons[row[1]][0]+ ' '+str(math.floor(max_val-float(persons[row[0]][1]))+minitime)+'\n'
        cs=cs+persons[row[1]][0]+' '+persons[row[0]][0]+ ' '+str(math.floor(max_val-float(persons[row[1]][1]))+minitime)+'\n'

f=open('floyd.txt','w')
f.write(cs)
f.close()
