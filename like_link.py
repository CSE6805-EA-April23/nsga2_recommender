import csv
import os

folder='myfile.csv'

list_names=[]
with open(folder, 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:

    if row[1] not in list_names:
        list_names.append(row[1])
f = open("links.txt", "w")



flag=2
link=''
for i in list_names:
    flag=2

    for j in i:
        if not ( '1' in j or '2' in j   or '3' in j   or '4' in j   or '5'  in j  or '6'  in j  or '7'  in j  or '8'   in j or '9' in j   or  '0'  in j ):
            flag=4

    if flag==4:
        link='https://www.facebook.com/'+i+'/likes'
        link='<a href="'+link+'">'+link+'</a><br>'
    if flag==2:
        link='https://www.facebook.com/profile.php?id='+i+'&sk=likes'
        link='<a href="'+link+'">'+link+'</a><br>'
    print(link)
    f.write(link+'\n')
f.close()
