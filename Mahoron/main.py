import os
import sys
import io
import eel
import pygame
import tkinter
import subprocess
import pyglet
import tkinter.filedialog
import time
from mutagen.mp3 import MP3
from pydub import AudioSegment
pyglet.have_avbin=False



@eel.expose
def StartUp2():
    eel.rename2(playlist[j])
    eel.sstomm2(sstomm(timely2()))

# Start up the application by loading the files
def StartUp():
    # Create a list to store the names of the mp3 files
    global maxi
    global playlist
    global playlist2
    global var4
    var4 = int(1000)

    # Get all the files in the directory
    userfolder = os.path.expanduser('~')
    userfolder = userfolder + "/Music/4K YouTube to MP3"
    folderpyg = 'C:/Users/John/Music/4K YouTube to MP3/'
    playlist = os.listdir(userfolder)

    global filepath
    filepath = userfolder + "\\"
    folderpyglet = folderpyg + "/"


    # Create a variable to store the state of the player and initialize it to false
    global playing
    global playing2
    # Create a variable to store the index of the song currently playing (starts at 0)
    global i
    i = 0
    global j
    j = 1
    # Remove files which are not mp3
    for item in playlist:
        if not item.endswith(".mp3"):
            playlist.remove(item)



    playlist2 = playlist
    # Prints the playlist to the terminal
    print(playlist)

    # Initialize the pygame mixer
    pygame.mixer.init()

    # Load the first mp3 file, that is playlist[0], to pygame mixer and play it
    pygame.mixer.music.load(filepath + playlist[i])
    pygame.mixer.music.play()
    
    # Set playing variable to true
    playing = True
    playing2 = False
    global musicp
    global load
    
    
    
    musicp = pyglet.media.Player()
    load = pyglet.media.load(str(filepath + playlist2[j]),streaming=False)
    musicp.queue(load)
    eel.sstomm(sstomm(timely()))



# Implements the play/pause button activity
@eel.expose
def PlayPause():
    global playing
    if playing == True:
        print("Pausing")
        playing = False
        pygame.mixer.music.pause()
    else:
        print("Playing")
        pygame.mixer.music.unpause()
        playing = True


# Implements the next button activity and plays the next song when current song finishes
@eel.expose
def nextTrack():    
    global i
    i += 1
    pygame.mixer.music.load(str(filepath + playlist[i]))
    eel.rename(playlist[i])
    pygame.mixer.music.play()
    print("Playing next")
    eel.sstomm(sstomm(timely()))
    eel.tozero()


# Implements the previous button activity
@eel.expose
def previousTrack():
    global i
    if i > 0:
        i = i - 1
        pygame.mixer.music.load(str(filepath + playlist[i]))
        pygame.mixer.music.play()
        eel.rename(playlist[i])
        print("Playing previous")
        eel.sstomm(sstomm(timely()))
        eel.tozero()
    else:
        pygame.mixer.music.load(str(filepath + playlist[i]))
        pygame.mixer.music.play()
        eel.rename(playlist[i])
        print("Playing previous")
        eel.sstomm(sstomm(timely()))


@eel.expose
def timely():
    song = MP3(str(filepath + playlist[i]))
    songLength = song.info.length
    eel.updatemaxdur(songLength)
    eel.updatemaxdur1(songLength)
    return songLength


@eel.expose
def sstomm(dur):
    return time.strftime('%M:%S', time.gmtime(dur))

# @eel.expose
# def slidevalue():
#     return (pygame.mixer.music.get_pos())


@eel.expose
def setpos(dur):
    dur=float(dur)
    global dur2
    dur2 = dur
    print(dur)
    pygame.mixer.music.set_pos(dur)
    


@eel.expose
def cropwrap():
    try:
        thevariable
    except NameError:
        dur2 = 0.0
        print("well, it WASN'T defined after all!")

    print("start ",dur2)
    cropaudio(filepath,playlist[i],(dur2+50),timely())
    


def cropaudio(files_path, file_name,startTime,endTime):

    # Time to miliseconds
    print(startTime,pygame.mixer.music.get_pos())
    startTime = (startTime*1000)
    endTime = endTime*1000
    print(startTime,endTime)
    # Opening file and extracting segment
    song = AudioSegment.from_mp3(files_path+file_name)
    extract = song[startTime:endTime]
    
    try:
        # Saving
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.asksaveasfile(parent=top,defaultextension=".mp3")
        top.destroy()
        extract.export(file_name.name,format="mp3")
    except:
        print("Bro please")


@eel.expose
def durends(var):
    global var0,var1,var2,var3,var4
    print("Accessed")
    var = var.split(",")
    print(var)
    var0 = int(var[0])
    var1 = int(var[1])
    var2 = round(int(var[2]))
    var3 = int(var[3])
    var4 = int(var[4])
    cropaudioprompt()
    

def cropaudioprompt():
    print("Crop begin")
    global var0,var1,var2,var3
    # Time to miliseconds
    st1 = var0*1000
    et1 = var1*1000
    st2 = var2*1000
    et2 = var3*1000
    print(st1,et1,st2,et2)
    # Opening file and extracting segment
    song = AudioSegment.from_mp3(str(filepath + playlist[i]))
    extract = song[st1:et1]
    extract.export("cut1.mp3",format="mp3")
    
    song2 = AudioSegment.from_mp3(filepath + playlist[j])
    extract = song2[st2:et2]
    extract.export("cut2.mp3",format="mp3")
    print("Done")



@eel.expose
def overlaylocal():
    global var4
    print("var4 is ",var4)
    eel.durend()
    print("Start dure")
    sound1 = AudioSegment.from_mp3("cut1.mp3")
    sound2 = AudioSegment.from_mp3("cut2.mp3")
    output = sound1.overlay(sound2, position=var4)   
    try:
        # Saving
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.asksaveasfile(parent=top,defaultextension=".mp3")
        top.destroy()
        output.export(file_name.name, format="mp3")
    except:
        print("Bro please")

    


    


@eel.expose
def PlayPause2():
    global playing2
    print("Play 2 access granted", playing2)
    if playing2 == True:
        print("Pausing 2")
        playing2 = False
        musicp.pause()

    else:
        print("Playing 2")
        musicp.play()
        playing2 = True


@eel.expose
def p2nextTrack():
    global j
    j += 1
    load = pyglet.media.load(str(filepath + playlist2[j]))
    musicp.queue(load)
    musicp.next_source()
    eel.rename2(playlist[j])
    print("Playing next")
    eel.sstomm2(sstomm(timely2()))
    
@eel.expose
def p2previousTrack():
    global j
    if j > 0:
        j =j - 1
        pygame.mixer.music.load(str(filepath + playlist[j]))
        pygame.mixer.music.play()
        eel.rename2(playlist[j])
        print("Playing previous")
        eel.sstomm2(sstomm(timely2()))


@eel.expose
def timely2():
    song = MP3(str(filepath + playlist2[j]))
    songLength = song.info.length
    eel.updatemaxdur2(songLength)
    return songLength

@eel.expose
def setpos2(dur):
    dur=float(dur)
    global dur1
    dur1 = dur
    print(dur)
    musicp.seek(dur)



@eel.expose
def initi():
    eel.sstomm2(sstomm(timely2()))
    
@eel.expose()
def convert2ogg():
     subprocess.call(['ffmpeg', '-i', str(filepath + playlist[i]),str(filepath)+'converted.ogg'])
    
@eel.expose()
def convert2flv():
    subprocess.call(['ffmpeg', '-i', str(filepath + playlist[i]),str(filepath)+'converted.flv'])

@eel.expose()
def convert2wav():
    subprocess.call(['ffmpeg', '-i', str(filepath + playlist[i]),str(filepath)+'converted.wav'])




if __name__ == '__main__':
    eel.init('web')
    # Calls the start functions
    StartUp()
    # Renders the window
    eel.start('index2.html', block=False)
    eel.rename(playlist[i])
    eel.sstomm(sstomm(timely()))
    PlayPause()




# Loop after loading the window

while True:
    # Detect if the mixer is not playing AND that it wasn't forced by the user, If both of these conditions are true then the current song must be over
    if not pygame.mixer.music.get_busy() and playing:
        nextTrack()
    eel.sleep(1)
