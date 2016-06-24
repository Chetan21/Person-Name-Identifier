import tkinter

def main():
    top = tkinter.Tk()
    top.wm_minsize(width=400, height=400)
    methodbutton1 = tkinter.Button(top, text="Method 1", command = setMethod1)
    methodbutton2 = tkinter.Button(top, text="Method 2", command = setMethod2)

    methodbutton1.pack()
    methodbutton2.pack()
    top.mainloop()

def setMethod1():
    print("method1")

def setMethod2():
    print("metho 2")

if __name__ == '__main__':
    main()