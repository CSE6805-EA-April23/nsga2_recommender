import os

folder='data\\friends'
files=os.listdir(folder)
total=[]
filess=''
file12 = open('myfile.csv', 'w')

for file in files:
    main_person=''
    file1 = open(folder+'\\'+file, 'r')
    Lines = file1.readlines()
    friends=[]
    for line in Lines:
        if not ('https://www.facebook.com/friends/' in line or 'https://www.facebook.com/watch/?ref=tab'  in line or 'https://www.facebook.com/marketplace/?ref=app_tab' in line  or 'https://www.facebook.com/groups/'  in line or 'https://www.facebook.com/bookmarks/' in line  or  'https://www.facebook.com/notifications/' in line  or 'https://www.facebook.com/photo/'  in line  or 'https://www.facebook.com/photo.php'  in line or 'https://www.facebook.com/gaming/'  in line or '/watch/' in line or '/reel/' in line or '/events/' in line or '/messages/' in line or '/posts/' in line or '/probanglahacks/' in line or 'substring filter' in line or line=='https://www.facebook.com/\n' or '/pages/' in line) :

            if line[len(line)-9:len(line)]=='/friends\n' or '&sk=friends' in line:
                if line[len(line)-9:len(line)]=='/friends\n':
                    line=line.replace("https://www.facebook.com/",'')
                    line=line.replace('/friends\n','')
                if '&sk=friends' in line :
                    line=line.replace('https://www.facebook.com/profile.php?id=','')
                    line=line[0:line.index('&')]
                line=line.replace('httpswww.facebook.comprofile.phpid=','')
                line=line.replace('\n','')
                main_person=line
            else:
                line=line.replace('https://www.facebook.com/profile.php?id=','')
                line=line.replace("https://www.facebook.com/",'')
                line=line.replace('\n','')
                if '/' not in line:
                    friends.append(line)

            if main_person in friends:friends.remove(main_person)


    for ij in friends:
        if main_person=='': continue
        if ij=='': continue
        file12.write(ij+","+main_person+"\n")


file12.close()



