from youtube_search import YoutubeSearch
import music_tag
import os
import wget

music=[]


def download():
    thumbnailurl='https://img.youtube.com/vi/8BiZpA9YEwQ/maxresdefault.jpg'
    print ("Downloading Thumbnail...")
    thumbnail = wget.download(thumbnailurl,out='jp.jpg')


def search(sr):
    results = YoutubeSearch(sr, max_results=2).to_dict()
    print(results)
    return results[0]['thumbnails'][1]


def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                #yield os.path.join(root, filename)
                yield filename
                music.append(filename)

for mp3file in mp3gen():
    pass
    #print (mp3file)

print(music[3])

f=music_tag.load_file(music[0])
fa=str(f['artist'])

if(fa==''):
    print("yes")


print(f['artist'])
print("hello")

search
#input()
