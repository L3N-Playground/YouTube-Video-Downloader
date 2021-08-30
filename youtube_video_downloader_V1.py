###Youtube Video Downloader V1



from pytube import YouTube

#input url
link = input("Enter URL: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()  #default 720p??

stream.download()


