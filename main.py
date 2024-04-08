from pytube import YouTube 
import os
import math

# Function to handle the progress
def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = math.floor((bytes_downloaded / total_size) * 100)
    print(f'Downloading: {percentage_of_completion}%', end='\r')

# where to save 
#SAVE_PATH = DriveFolderPathToWhereYouWantToStoreVideos #Change path to your location (windows)
SAVE_PATH = "/Users/yourusername/Folder/To/Download/To"  # Update this path (MAC)


# link of the video to be downloaded
link = "YOUTUBE_VIDEO_LINK_HERE"  # Add youtube video link here

try:
    # object creation using YouTube
    yt = YouTube(link, on_progress_callback=progress_function)
except:
    # to handle exception
    print("Connection Error")

# Get the video with the highest resolution
d_video = yt.streams.get_highest_resolution()

try:
    # downloading the video
    print("Downloading...")
    d_video.download(output_path=SAVE_PATH)
    print('\nVideo downloaded successfully!')
except Exception as e:
    print("Some Error:", e)