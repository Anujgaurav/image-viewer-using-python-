from turtle import color
from PIL import ImageTk
import PIL.Image 
from tkinter import*
from tkinter import filedialog
import os
class ImageView:
    def __init__(self, root):
        self.root = root
        self.root.title("IMAGE VIEWER")
        self.root.geometry('950x600') 
        self.root.resizable(0, 0)
        Label(root,text='IMAGE VIEWER IN PYTHON', font='fantesy 20 bold').pack(side=BOTTOM)
        self.i = 0
        self.Image_list = []
        self.path = ""
        self.extension = ['png','JPG','PNG','JPEG','jpg','jpeg']
        self.canvas = Canvas(self.root, bd=5, relief=RIDGE)
        self.root.bind('<Right>', self.next_image)
        self.root.bind('<Left>', self.previous_image)
        self.canvas.place(x=0, y=0, height=500, width=850)
        self.previous_button = Button(self.root, text="Previous", width=8, font=('arial', 10, 'bold'), command=self.previous_image)
        self.previous_button.place(x=235, y=500)

        self.next_button = Button(self.root, text="Next", width=5, font=('arial', 10, 'bold'), command=self.next_image)
        self.next_button.place(x=475, y=500)

        self.open_button = Button(self.root, text="OPEN FOLDER ", width=18, font=( 'arial', 10, 'bold'), command=self.open_file)
        self.open_button.place(x=316, y=500)
    def open_file(self):
        self.path = filedialog.askdirectory()
        if self.path:
            self.Image_list = []
            self.add_image()

    def add_image(self):
        for image in os.listdir(self.path):
            ext = image.split('.')[::-1][0].upper()
            if ext in self.extension:
                self.Image_list.append(image)

        self.resize(self.Image_list[0])
    def resize(self, image):
        if self.path:
            os.chdir(self.path)
            image_p = self.path + '\\' + str(image)
            img = PIL.Image.open(image)
            width, height = img.size
            if (int(width) > 850 and int(height) < 500):
                img = img.resize((850, height))
            elif (int(height) > 500 and int(width) < 850):
                img = img.resize((width, 500))
            elif (int(width) > 850 and int(height) > 500):
                img = img.resize((700, 500))

            storeobj = ImageTk.PhotoImage(img)
            self.canvas.delete(self.canvas.find_withtag("bacl"))
            w = self.canvas.winfo_width()
            h = self.canvas.winfo_height()
            self.canvas.image = storeobj
            self.canvas.create_image(
                w / 2, h / 2, image=storeobj, anchor=CENTER)
            self.root.title("Image Viewer ({})".format(image_p))

    def next_image(self, *args):
        self.i += 1
        try:
            self.image = self.Image_list[self.i]
            self.resize(self.image)
        except:
            pass
    def previous_image(self, *args):
        self.i -= 1
        try:
            self.image = self.Image_list[self.i]
            self.resize(self.image)
        except:
            self.i = 1
if __name__ == '__main__':
    root = Tk()
    img = ImageView(root)
    root.configure(background="pink")
    root.mainloop()

