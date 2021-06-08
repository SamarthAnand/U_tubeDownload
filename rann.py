from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from pytube import *
from pytube import YouTube
import validators
import requests
import xml.etree.ElementTree as ET

win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x500")
win.title('YTVD')
win.config(bg= "blue")
win.resizable(False,False)


'''
response_xml_as_string = "xml response string from API"
responseXml = ET.fromstring(response_xml_as_string)
Id = responseXml.find('data').find('ID')
video_link = responseXml.find('data').find('VideoUrl')
# print Id.text
'''
direct =""
def open_path():
    Download_out.config(text="Downloading...",font=('Helvetica 20'))
    Download_name.config(text="")
    Download_size.config(text="")
    Download_loc.config(text="")
    global direct
    direct = filedialog.askdirectory()   #saves the selected path to save the video/audio
    path_txt.config(text= direct)
    
    '''
    Download method downloads the video if called.
    '''
def Download():  
        url = link_ent.get()
        selected = types.get()
        if( len(url) < 1):   
            link_error.config(text="Enter a valid URL. ") #incase of error in link of the youtube video
        if( len(direct) < 1):
            path_error.config(text="Enter a valid path. ")  #incase of wrong path input
        else:
            link_error.config(text="")
            path_error.config(text="")
            try:
                Yt= Youtube(url)
                try:
                    if (selected == option[0]):
                        typ = Yt.streams.get_highest_resolution()   # high quality video is downloaded
                    elif (selected == option[1]):
                        typ = Yt.streams.filter(progressive= True,file_extension="mp4").first() # low quality video is downloaded
                    elif (selected == option[2]):
                        typ = Yt.streams.filter(only_audio=True).first()  # audio of the video is downloaded
                    try:
                        typ.download(direct)
                        link_ent.delete(0,"end")
                        path_txt.config(text="\t\t\t\t\    ")
                        Download_out.config(text="Downloaded",font=(12))
                        
                        name = Id
                        size = typ.filesize/1024000
                        size = round(size,1)
                        
                        Download_name.config(text="Name : "+name)
                        Download_size.config(text="Size : "+str(size)+" MB")
                        Download_loc.config(text="Path : "+direct)
                    except:
                           Download_out.config(text="Download failed",font=(12))
                except:
                        Download_out.config(text="Download failed",font=(12))
            except:
                path_error.config(text="Enter a valid path here",font=(12))
                    
heading = Label(win, text="Download videos from Youtube", font=('Century 20 bold'))
heading.pack(pady=10)

link = Label(win, text="URL", font=('Helvetica 20'), foreground="black")
link.pack(anchor="nw",padx=100 ,pady=50)
#entry box is the text box

'''
Here we have to create a variable to copy the url from the xml and assignit to entry_url
'''
entry_url = StringVar()
link_ent = Entry(win, width = 52, textvariable = link_ent)
link_ent.place(x= 180,y=100)

link_error = Label(win,font=('Helvetica 10'), background="blue",foreground="black" )
link_error.place(x= 340,y = 130)

path = Label(win,text="path",font=('Helvetica 20'), foreground="black" )
path.pack(anchor="nw",padx=100 ,pady=2)

path_txt = Label(win,text="\t\t\t\t     ",font=('Helvetica 20'), background="white" )
path_txt.place(x = 180 , y = 170)

path_style = ttk.Style()
path_style.configure("PT.TButton",background="green", foreground = "black",font=('Courier 15 bold'))

path_btn = Button(win,width = 15, text = "Select Path",style = "PT.TButton",command = open_path)  #on click select path button open_path method runs
path_btn.place(x=450,y =165)

path_error = Label(win,font=('Helvetica 10'),background="blue",foreground="red")
path_error.place(x= 340,y = 190)

Download_type = Label(win,text="Download Type",font=('Helvetica 20'), foreground="black" )
Download_type.pack(anchor="w",padx=100 ,pady=50)

option =["High Quality","Low quality","Audio"]
types = ttk.Combobox(win, value=option, width=35, height=35)
types.current(0)
types.place(x= 250, y = 230)

Download_style = ttk.Style()
Download_style.configure("DO.TButton", background ="darkorange1", foreground = "black",font=('Courier 25 bold'))

Download_btn = Button(win,width= 30, text="Download now",style="PT.TButton",command = Download)  # on click Download now the Download method runs
Download_btn.pack(anchor="center",padx = 30)

Download_out = Label(win,text="Wait for download to complete",font=('Helvetica 10'), background="blue")
Download_out.pack(anchor="center",pady=10)


Download_name = Label(win,font=('Helvetica 10'), background="blue",foreground="white" )
Download_name.pack(anchor="w",padx=100 ,pady=10)
Download_size = Label(win,font=('Helvetica 10'), background="blue",foreground="white" )
Download_size.pack(anchor="nw",padx=100 ,pady=10)
Download_loc = Label(win,font=('Helvetica 10'), background="blue",foreground="white" )
Download_loc.pack(anchor="nw",padx=100 ,pady=5)



win.mainloop()
