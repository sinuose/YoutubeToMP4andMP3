import pytube 
from moviepy.editor import *

def getYoutubeMP4Highest(link, output):
    video = pytube.YouTube(link)
    streams = video.streams

    # Find the mp4 audio streams
    audio = [s for s in streams if s.type == 'audio' and s.mime_type == "audio/mp4"]

    # Get highest sampling rate
    audio_highest = max(audio, key=lambda s: int(''.join(filter(str.isdigit, s.abr))))

    video_final = video.streams.get_by_itag(audio_highest.itag)
    pathout = video_final.download(output_path=output)
    return pathout

def convertMP4toM4A(mp4_path, m4a_path):
    audio_clip = AudioFileClip(mp4_path)
    audio_clip.write_audiofile(m4a_path, codec='aac')
    audio_clip.close()

def convertMP4toMP3(mp4_path, mp3_path):
    FILETOCONVERT = AudioFileClip(mp4_path)
    FILETOCONVERT.write_audiofile(mp3_path)
    FILETOCONVERT.close()

