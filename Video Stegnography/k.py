from tkinter import filedialog
from tkinter import *

import cv2


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename) #returns file path
a=cv2.imread(root.filename)
cv2.imshow("a",a)

print(type(a))
print(a.shape)
li=[]
for i in a:
    for j in i:
        for k in j:
            li+=k

print(len(li))
cv2.waitKey(0)