import csv
import os

files=os.listdir('data/FB\\')
mappings={}
for jh in files:
    files_read=open('data\\FB\\'+jh).read()
    i=0
    sp=[]
    ipj=files_read.index('Snapshot-Content-Location: ')
    ipjk=files_read.index('\n',ipj)
    namelink=files_read[ipj:ipjk]
    namelink=namelink[namelink.rindex('/')+1:]
    if '=' in namelink:
        namelink=namelink[namelink.index('=')+1:]
    print(namelink)


    try:
        jp=1

        while(True):
            jp=jp+1
            j=files_read.index("role=3D\"article\"",i)
            i=j+1

            spans=[]
            try:
                s=files_read.index("role=3D\"article\"",i)
                post=files_read[i:s]

                k=0
                while(True):

                    try:
                        n=post.index("<span>",k)
                        o=post.index('</span>',n)
                        f=post[n+6:o]
                        k=n+1
                        if '<' in f or '>' in f or '/' in f:
                            continue
                        else:

                            spans.append(f.replace('=\n',''))
                    except:
                        break



            except:
                s= len(files_read)-1
                post=files_read[i:s]
                k=0
                while(True):
                    try:
                        n=post.index("<span>",k)
                        o=post.index('</span>',n)
                        f=post[n+6:o]
                        k=n+1
                        if '<' in f or '>' in f or '/' in f:
                            continue
                        else:

                            spans.append(f.replace('=\n',''))
                    except:
                        break


            sp.append(spans)

    except:
        pass
    points=0
    counts=0
    for ipc in sp:

        if counts==10:break


        for jpc in ipc:


            if 'January' in jpc or  'February' in jpc or 'March' in jpc or 'April' in jpc or 'May' in jpc or 'June' in jpc or 'July' in jpc or 'August' in jpc or 'September' in jpc or 'October' in jpc or 'November' in jpc or 'December' :
                point=16
                counts=counts+1
                if '2022' in jpc:
                    point=8
                if '2021' in jpc:
                    point=4
                if '2020' in jpc:
                    point=2
                if '2019' in jpc:
                    point=1
                if '2018' in jpc:
                    point=0.5
                if '2017' in jpc:
                    point=0.25
                if '2016' in jpc:
                    point=0.125
                if '2015' in jpc:
                    point=0.05
                if '2014' in jpc:
                    point=0.001
                if '2013' in jpc:
                    point=0.001
                if '2012' in jpc:
                    point=0.001

                if '2011' in jpc or '2010' in jpc:
                    point=0.001
                if '200' in jpc:
                    point=0.0001
                points=points+point
                break
    print(points)
    mappings[namelink]=points
avg=0
n=0
for i in mappings:
    avg=mappings[i]+avg
    n=n+1
avg=avg/n


cv=''
with open("mappings.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    if row[1] not in mappings:
        cv=cv+row[0]+','+row[1]+','+str(avg)+'\n'
    if row[1] in mappings:
        cv=cv+row[0]+','+row[1]+','+str(mappings[row[1]])+'\n'

f=open('corrected_mappings.csv','w')
f.write(cv)
f.close()

