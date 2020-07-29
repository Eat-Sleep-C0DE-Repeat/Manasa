from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import tkinter.messagebox as mb

def word(texts):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

def subscribe():
    with open('Subscribers.txt', 'a') as f:
        f.write(f"{userName.get(), userEmail.get()}\n")
        mb.showinfo("Done","Thankyou for Subscribing us")

root = Tk()
root.title("TIMES NOW")
root.geometry("650x400")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(word(text))

        image = Image.open(f"{i+1}.jpg")
        image = image.resize((105,100 ), Image.ANTIALIAS)
        photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=100, height=70)
Label(f0, text="TIMES NOW", font="times 38 bold").pack()

Label(f0, text="July 29, 2020", font="scriptmt 14 bold").pack()
f0.pack()

f1 = Frame(root, width=100, height=70)
Label(f1, text=texts[0], padx=50, pady=22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

f2 = Frame(root, width=100, height=70, pady=14, padx= 22)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")

f3 = Frame(root, width=100, height=70, pady=14)
Label(f3, text=texts[2], padx=22, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")

Label(root, text='SUBSCRIBE FOR MORE UPDATES', font=("Times 15 bold")).pack()

f_frame = Frame(root)
f_frame.pack()

userName = StringVar()
userEmail = StringVar()

Label(f_frame, text='Name: ', padx=3, pady=3).grid(row=1, column=1)
Label(f_frame, text='Email: ', padx=3, pady=3).grid(row=2, column=1)

name=Entry(f_frame, textvariable=userName).grid(row=1, column=2)
email=Entry(f_frame, textvariable=userEmail).grid(row=2, column=2)

Button(f_frame, text='Subscribe', command=lambda: subscribe()).grid(row=4, column=1, padx=10, pady=10)


def star():
    mb.showinfo("Succesfull.","Thankyou for rating us!")

def rate():
    a = mb.askokcancel("Rate", "Would you please take a moment and rate us?")
    print(a)
    if a==True:
        mb.showinfo("Rated", "Thank you for rating us.")
    else:
        mb.showinfo("Not Rated", "Sorry\nWe are looking forward to serve in much better way.\nThank You!")

def help():
    mb.showinfo("Help","We will soon resolve your issue. Kindly wait\nThank You")

myMenuBar = Menu(root)

m1 = Menu(myMenuBar, tearoff=0)
m1.add_command(label='Rate', command=rate)
m1.add_command(label='Help', command=help)

myMenuBar.add_cascade(label='Options', menu=m1)
myMenuBar.add_command(label='Exit', command=quit)
root.config(menu=myMenuBar)

myslider = Scale(root, from_ = 0, to = 5, orient = HORIZONTAL)
Label(root,text="RATE US").pack()
myslider.pack()
myslider.set(1)
Button(root, text="Submit",command=star).pack()



root.mainloop()