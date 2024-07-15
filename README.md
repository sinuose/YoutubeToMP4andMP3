**Youtube Audio Downloader**

This project is a personal tool I use to scrape audio from youtube videos. This is an application for my mp3 player.

This simply downloads the highest stream of an mp4 file, and seperately converts it to an mp3 using PyTube.

**Usage**
1. Type in the path to save. This will create two subfolders: ../mp4 and ../mp3
2. Paste in youtube link. This will save the audio in both formats under the previously made folders.
3. once finished with all the videos you'd like to downloader, type in either '' or 'quit' into the terminal for the program to swifly exit.

July 15 2024:
There is an update to Youtube's backend.

in cipher.py of Pytube, change line 264 to:
------------------------------------------------------------------------------------------------
function_patterns = [
    # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
    # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
    # var Bpa = [iha];
    # ...
    # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
    # Bpa.length || iha("")) }};
    # In the above case, `iha` is the relevant function name
    r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
]
------------------------------------------------------------------------------------------------

Happy Downloading!
