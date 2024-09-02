from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import png

root = Tk()

def generateqr():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"    #creating a png file to store the QR
    url = pyqrcode.create(link)       # creating QR using pyqrcode module
    url.png(file_name, scale=4)       # saving the generated QR the above created png file
    # now we have create the QR and saved to a file
    # next we have to display the QR in the Tkinter window
    # to display the QR image, we need to open the image using ImageTK module
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(root, image=image)     # creating a label and passing the QR image
    image_label.pack()
    image_label.image = image
    canvas.create_window(200, 250, window=image_label)

#using canvas to create a window
canvas = Canvas(root, width=400, height=600)
canvas.pack()

#creating label and adding to canvas windows
app_label = Label(root, text="QR Generator", fg='blue', font=('Arial',30))  #create lable
canvas.create_window(200, 50, window=app_label)  #add to canvas window

name_label = Label(root, text="Link Name")           #create lable
canvas.create_window(200, 100, window=name_label)    #add to canvas window

name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)

link_label = Label(root, text="Link")                 #create lable
canvas.create_window(200, 160, window=link_label)     #add to canvas window

link_entry = Entry(root)
canvas.create_window(200, 180, window=link_entry) 

#create button
button = Button(root, text="Generate QR code", command=generateqr)
canvas.create_window(200, 240, window=button)












root.mainloop()