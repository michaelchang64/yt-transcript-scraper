# yt-transcript-scraper

This program scrapes all the YouTube transcripts in a YouTube video playlist.

Using selenium for the browser automation, this routine opens a browser (Chrome) to your specified link to a YouTube playlist with 100+ videos. It then scrolls down to presumably the end of the playlist then scrapes basic video description and link information from said playlist.

Using the youtube_transcript_api module, the program takes all the video information then outputs one .txt file containing video title followed by full video transcript.

# Set-up

assuming user is running python 3.7+:

1. go to terminal
2. `python -m venv venv`
3. `pip install -r requirements`
4. `source venv/bin/activate` (this activates the virtual environment)
5. `python actual_transcript_scraper.py`

This will run for a while, but once it does, the user should find the output .txt within the same file directory

## TODO
1. cleanup files
2. comment for clarity
3. refactor
