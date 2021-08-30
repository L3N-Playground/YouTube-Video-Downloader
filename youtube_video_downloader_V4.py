###Youtube Video Downloader V4



from pytube import YouTube
import time, datetime
from hurry.filesize import size


#change path here 
path = ''



print("##### YouTube Video Downloader #####")
print("")

#input url
link = input("Enter URL: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()  #default 720p??

#details of download
print("")
print("##### Details #####")
print("Video Title:     ", video.title)
print("Video Length:    ", datetime.timedelta(seconds=video.length))
print("Video Size:      ", size(stream.filesize), "Bytes")
print("")

#ask change video title
print("Want to change the video title?")
choose = ''
choosen = ['y', 'n']
while choose not in choosen:
    choose = input("[y/n] ")
print("")
#filename
if choose == 'y':
    filename = input("Name the video: ")
    filename = filename + '.mp4'
    print("")
else:
    filename = video.title + '.mp4'

#download and time
print("##### Download start #####")
time_start = time.time()
stream.download(path,filename)
time_end = time.time() - time_start

#end of programm and output time
print("##### Download completed ###")
print("Time:    ", datetime.timedelta(seconds=time_end))
print("mb/s:    ", round(stream.filesize*10**-6 / time_end, 2))


