import music_tag
import os
import re
import hdis
import pyfiglet

hdis.runame()
print('Enjoy a Repulserator Creation')

music=[]



def ice(name):
    e=''
    tlist2=name.split('\\')
    name=tlist2[1]
    tlist=name.split(" - ")
    if len(tlist) > 1:
        
        #print(tlist)
        tl=tlist[0]
        tr=tlist[1]
        #lyr=re.compile('(lyrics)',re.IGNORECASE)
        tr=re.sub("\(lyrics\)",'',tr,flags=re.IGNORECASE)
        tr=re.sub("\(official video\)",'',tr,flags=re.IGNORECASE)
        tr=re.sub("\(official audio\)",'',tr,flags=re.IGNORECASE)

        while(1):
            if re.search(" .mp3",tr):
                tr=re.sub(" .mp3",".mp3",tr)
            else:
                break
        
        tr=re.sub(".mp3",'',tr)
    
        tlist[1]=tr
        return tlist
    else:
        tlist[0]=tlist[0]
        tlist.append(e)
        return tlist

def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                jo= os.path.join(root, filename)
                yield filename
                music.append(jo)


os.chdir("D:\Music")

for k in mp3gen():
    pass

print("Scanning all songs")
for kk in music:
    #print(kk)
    f=music_tag.load_file(kk)
    fa=str(f['artist'])
    try:
        if(fa==''):
            tlist=ice(str(kk))
            f['title']=tlist[1]
            f['artist']=tlist[0]
            print('title ',f['title'])
            print('artist ',f['artist'])
            #os.rename(kk,tlist[1])
            f.save()
        elif(fa!=''):
            continue
    except:
        continue

print("Done")        

