###Youtube Video Downloader



from pytube import YouTube
import time, datetime
from hurry.filesize import size


#change path here
path = ''
#change filename here
filename = ''



#input url
link = input("Enter URL: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()  #default 720p??

#filename
if filename == '':
    filename = video.title + '.mp4'
else:
    filename = filename + '.mp4'

#details of download
print("Video Title:     ", video.title)
print("Video Length:    ", datetime.timedelta(seconds=video.length))
print("Video Size:      ", size(stream.filesize), "Bytes")

#download and time
print("##### Start download")
time_start = time.time()
stream.download(path,filename)
time_end = time.time() - time_start

#end of programm and output time
print("##### Download completed: ", datetime.timedelta(seconds=time_end))

