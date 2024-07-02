import pytube 
from moviepy.editor import *

def getYoutubeMP4Highest(link, output):
    video = pytube.YouTube(link)
    streams = video.streams

    # find the mp4 audio streams
    audio = []
    for i in range(len(streams)):
        if streams[i].type == 'audio' and streams[i].mime_type == "audio/mp4":
            audio.append(streams[i])

    # get highest sampling rate
    # sort the audio
    for i in range(len(audio)):
        if i == 0:
            audio_highest = audio[i]
        # check which is higher
        abr_highest = ''.join(c for c in audio_highest.abr if c.isdigit())
        abr_curr = ''.join(c for c in audio[i].abr if c.isdigit())
        # update the highest
        if int(abr_curr) > int(abr_highest):
            audio_highest = audio[i]

    video_final = video.streams.get_by_itag(audio_highest.itag)
    pathout = video_final.download(output_path=output)
    return pathout

def convertMP4toMP3(mp4_path, mp3_path):
    FILETOCONVERT = AudioFileClip(mp4_path)
    FILETOCONVERT.write_audiofile(mp3_path)
    FILETOCONVERT.close()

