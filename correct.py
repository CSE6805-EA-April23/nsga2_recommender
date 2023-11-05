import csv
lists=[]
maps={}
with open("myfile.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    lists.append(row[1])

#     if row[0] not in maps:
#       maps[row[0]]=1
#     else:
#       maps[row[0]]=maps[row[0]]+1
#
#     if row[1] not in maps:
#       maps[row[1]]=1
#     else:
#       maps[row[1]]=maps[row[1]]+1
#
# for j in maps:
#   if maps[j]>1:
#     lists.append(j)

c=''
with open("myfile.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    if row[0] in lists :
      c=c+row[0]+','+row[1]+'\n'



filez=open('check.csv','w')

filez.write(c)
filez.close()




