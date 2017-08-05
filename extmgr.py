import Tkinter
import os
import tkMessageBox
import tkFileDialog
import shutil

top = Tkinter.Tk()
path=""

def takepathname():
	global path
	path=E.get()
	if os.path.exists(path):
		makefolders(path)
	else:
		tkMessageBox.showinfo("Oops!","Incorrect path. Try again")
		

def makefolders(path):
	if not os.path.exists(path+"/Photos"):
		os.mkdir(path+"/Photos",0777)
	if not os.path.exists(path+"/Music"):
		os.mkdir(path+"/Music",0777)
	if not os.path.exists(path+"/Videos"):
		os.mkdir(path+"/Videos",0777)
	if not os.path.exists(path+"/Documents"):
		os.mkdir(path+"/Documents",0777)
	if not os.path.exists(path+"/Other"):
		os.mkdir(path+"/Other",0777)
	transferfiles(path)

def transferfiles(path):
	filelist=os.listdir(path)
	for file in filelist:
		if file.endswith(".txt") or file.endswith(".doc") or file.endswith(".pdf") or file.endswith(".rtx"):
			shutil.move(path+'/'+file,path+"/Documents/")
		elif file.endswith(".wav") or file.endswith(".au") or file.endswith(".mp3") or file.endswith(".wma") or file.endswith(".aiff"):
            		shutil.move(path+'/'+file,path+"/Music/")
		elif file.endswith(".jpg") or file.endswith(".xpm") or file.endswith(".gif") or file.endswith(".png"):
            		shutil.move(path+'/'+file,path+"/Photos/")
		elif file.endswith(".avi") or file.endswith(".flv") or file.endswith(".wmv") or file.endswith(".mov") or file.endswith(".mp4"):
            		shutil.move(path+'/'+file,path+"/Videos/")
        	elif '.' in file:
        		shutil.move(path+'/'+file,path+"/Other/")
	tkMessageBox.showinfo("Yay!","Success")

def browse():
	global E
	E.insert(0, tkFileDialog.askdirectory(initialdir="/home"))



E=Tkinter.Entry(top)
Br=Tkinter.Button(top,text="Browse",command=browse)
B=Tkinter.Button(top, text="Organise",command=takepathname)
L=Tkinter.Label(top, text="Enter path:")
L.pack()
Br.pack()
E.pack()
B.pack()
top.mainloop()