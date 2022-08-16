from tkinter import *
from PIL import ImageTk
import shutil
import os
import math

def createDirectory(directory):
    current_path = os.getcwd()
    try:
        os.mkdir(current_path +  "/image/" + directory)
    except OSError as e:
        print(e)
        pass

def movefile(i, new):
    current_path = os.getcwd()
    source = current_path + '/image/' + str(i) +'.jpg'
    destination = current_path + '/image/' + new + '/' + str(i) + '.jpg'
    shutil.move(source,destination)

num = 0

def skip_image():
    try:
        global num
        num = num + 1
        canvas.itemconfig(shapes, image=img_path[num])    
    except:
        print("끝")
        app.destroy()

def next_image():
    name=ent.get()
    if name:
        createDirectory(name)
        movefile(num+1, name)
        skip_image()
    else:
        pass

def next_image_by_enter(event):
    name=ent.get()
    if name:
        createDirectory(name)
        movefile(num+1, name)
        skip_image()
    else:
        pass


width=300
height=300

app = Tk()

app.bind('<Return>', next_image_by_enter)

canvas = Canvas(app, width=300, bg="red")
canvas.pack(side = "top", padx=10, pady=10)

panedwindow=PanedWindow(relief="raised",orient="vertical", bd=2)
panedwindow.pack(side = "bottom", fill="x")

w1=PanedWindow(panedwindow, orient="horizontal", bd=3)
panedwindow.add(w1)

q = Label(panedwindow, text="입력하세요")
w1.add(q)

ent = Entry(app, width=25, font=('Arial 10'))    
w1.add(ent)

w2=PanedWindow(panedwindow, orient="horizontal", bd=3)
panedwindow.add(w2)

btn_s = Button(app, text="skip", command=skip_image)
btn_s.config(width = 8)
w2.add(btn_s, padx=20)

btn_n = Button(app, text="next", command=next_image)
btn_n.config(width = 8)
w2.add(btn_n, padx=20)

img_path = []
for i in range(1, 51):
    try:
        img_path.append(ImageTk.PhotoImage(file="../Project/image/"+ str(i) + ".jpg"))
    except:
        pass

for i, img in enumerate(img_path):  
    r = (img.width() / width)
    if r < 1:
        img = img._PhotoImage__photo.zoom(math.ceil(width/img.width()), math.ceil(width/img.width()))
    else:
        img = img._PhotoImage__photo.subsample(math.ceil(img.width() / width), math.ceil(img.width() / width))
    img_path[i] = img 

shapes = canvas.create_image(width / 2, height / 2, image = img_path[0])

app.title("이미지 띄우기")
# app.geometry("1000x500")
app.mainloop()



