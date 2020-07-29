from tkinter import *


root = Tk()
root.title("Calculator")
root.geometry("600x900")
root.resizable(0,0)

def click(event):                                                                        
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)                                                       

        sc.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
#scvalue.set("")
screen = Entry(root, textvar = scvalue, bg = "black",fg="white", font = "scriptmt 35 bold", bd = 18, relief = GROOVE)
screen.pack(fill = X, pady = 10, padx = 10)

f = Frame(root, bg = "black")

b = Button(f, text = "9", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd= 12, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "8", height = 1, width= 2,  bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "7", height = 1, width = 2,  bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "+", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, text = "6", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "5", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "4", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "-", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, text = "3", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "2", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "1", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "*", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()
#f = Frame(root, bg = "white")

#b = Button(f, text = "0", padx = 20, pady = 20, font = "scriptmt 35 bold")
#b.pack(side = LEFT, padx = 5, pady = 5)
#b.bind("<Button-1>", click)

#b = Button(f, text = "-", padx = 20, pady = 20, font = "scriptmt 35 bold")
#b.pack(side = LEFT, padx = 5, pady = 5)
#b.bind("<Button-1>", click)

#b = Button(f, text = "*", padx = 20, pady = 20, font = "scriptmt 35 bold")
#b.pack(side = LEFT, padx = 5, pady = 5)
#b.bind("<Button-1>", click)

#f.pack()

f = Frame(root, bg = "black")

b = Button(f, text = "0", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text = "c", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "=", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "/", height = 1, width = 2, bg = "white",fg="black", padx = 10, pady = 10, font = "scriptmt 35 bold", bd = 11, relief = GROOVE)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()

#f = Frame(root, bg = "white")

#b = Button(f, text = "c", height = 1, width = 5, padx = 20, pady = 20, font = "scriptmt 30 bold")
#b.pack(side = LEFT, padx = 5, pady = 5)
#b.bind("<Button-1>", click)

#b = Button(f, text = ".", height = 1, width = 5, padx = 20, pady = 20, font = "scriptmt 30 bold")
#b.pack(side = LEFT, padx = 5, pady = 5)
#b.bind("<Button-1>", click)

#b = Button(f, text = "00", height = 1, width = 5, padx = 20, pady = 20, font = "scriptmt 30 bold")
#b.pack(side = LEFT, padx = 5, pady = 5)
#b.bind("<Button-1>", click)

#f.pack()



root.mainloop()