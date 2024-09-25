import sys
import os
from yt_scraper import *
from tqdm import tqdm
from pathlib import Path
from moviepy.editor import AudioFileClip
from mutagen.mp4 import MP4, MP4Cover
import eyed3

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_videos(txt_file, mp4_dir, m4a_dir, mp3_dir, artist, album, cover_image=None):
    # Read the txt file with YouTube links
    with open(txt_file, 'r') as f:
        links = f.readlines()

    # Download and convert each video
    for idx, link in enumerate(links):
        link = link.strip()  # Remove any extra whitespace/newlines
        if not link:
            continue
        
        print(f"Processing link {idx + 1}/{len(links)}: {link}")
        
        # Download video as MP4
        mp4_saved = getYoutubeMP4Highest(link, mp4_dir)
        
        # Generate filenames for M4A and MP3
        m4a_saved = mp4_saved.replace('mp4', 'm4a')
        mp3_saved = mp4_saved.replace('mp4', 'mp3')

        # Convert MP4 to M4A and MP3
        convertMP4toM4A(mp4_saved, m4a_saved)
        convertMP4toMP3(mp4_saved, mp3_saved)

        # Add metadata to M4A and MP3 files
        add_metadata_m4a(m4a_saved, artist, album, idx + 1, cover_image)
        add_metadata_mp3(mp3_saved, artist, album, idx + 1, cover_image)

def add_metadata_m4a(m4a_file, artist, album, track_num, cover_image=None):
    audiofile = MP4(m4a_file)
    
    # Set metadata fields
    audiofile['\xa9ART'] = artist  # Artist
    audiofile['\xa9alb'] = album   # Album
    title = os.path.basename(m4a_file).replace(".m4a", "")
    audiofile['\xa9nam'] = title   # Title

    # Convert the generator from glob to a list to count the number of M4A files
    m4a_files = list(Path(m4a_file).parent.glob("*.m4a"))
    audiofile['trkn'] = [(track_num, len(m4a_files))]  # Track number

    if cover_image:
        with open(cover_image, 'rb') as img_file:
            cover_data = img_file.read()
            audiofile.tags['covr'] = [MP4Cover(cover_data, imageformat=MP4Cover.FORMAT_JPEG)]

    audiofile.save()

def add_metadata_mp3(mp3_file, artist, album, track_num, cover_image=None):
    audiofile = eyed3.load(mp3_file)
    title = os.path.basename(mp3_file).replace(".mp3", "")

    if audiofile.tag is None:
        audiofile.initTag()

    audiofile.tag.artist = artist
    audiofile.tag.album = album
    audiofile.tag.title = title
    audiofile.tag.track_num = track_num

    if cover_image:
        with open(cover_image, 'rb') as img_file:
            cover_data = img_file.read()
            audiofile.tag.images.set(3, cover_data, 'image/jpeg')

    audiofile.tag.save()

if __name__ == '__main__':
    print('This will save as MP4, M4A, and MP3')

    # Input the path to the text file with YouTube links
    txt_file = input('Path to text file with YouTube links: ')

    # Get the directories ready
    output = input('Save Path: ')
    mp4_dir = os.path.join(output, 'mp4')
    m4a_dir = os.path.join(output, 'm4a')
    mp3_dir = os.path.join(output, 'mp3')
    ensure_dir(mp4_dir)
    ensure_dir(m4a_dir)
    ensure_dir(mp3_dir)

    # Input metadata details
    artist = input('Artist Name: ')
    album = input('Album Name: ')
    cover_image = input('Path to cover image (or press Enter to skip): ')
    cover_image = cover_image if cover_image.strip() else None

    # Process videos
    process_videos(txt_file, mp4_dir, m4a_dir, mp3_dir, artist, album, cover_image)

    print("\nAll videos processed successfully!")
