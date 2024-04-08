from pytube import YouTube 

# where to save 
SAVE_PATH = "C:/Users/*UserName*/Downloads" #Change path to your location (windows)
#SAVE_PATH = "/Users/yourusername/Folder/To/Download/To"  # Update this path (MAC)


# link of the video to be downloaded 
link = "YOUTUBE_LINK_HERE" #Add youtube video link here

try: 
    print("Download started...")
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# get the video with the highest resolution
d_video = yt.streams.get_highest_resolution()

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")