###Youtube Video Downloader



from pytube import YouTube
import time, datetime


#change path here
path = ''
#change filename here:  'name.mp4'
filename = ''



#input url
link = input("Enter URL: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()  #default 720p??

#download and time
time_start = time.time()
stream.download(path,filename)
time_end = time.time() - time_start

#end of programm and output time
print("Download completed: ", datetime.timedelta(seconds=time_end))

