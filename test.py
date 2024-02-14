	
from tkinter import *
 
mainFrame = Tk()
mainFrame.geometry( '400x300' )
 
lbl1 = Label( mainFrame )
lbl2 = Label( mainFrame )
lbl1["text"] = "크기"
lbl2["text"] = "색상"
 
def textSize() :
    lbl1["font"] = "Arial 40"

def textsize1():
    lbl1["font"] = "Arial 10"

def textColor() :
    lbl2["foreground"] = "blue"
 
btn1 = Button( mainFrame, text = "크기", command = textSize )
btn2 = Button( mainFrame, text = "색상", command = textColor )
btn3 = Button( mainFrame, text = "뷁", command = textsize1 )


lbl1.pack()
lbl2.pack()
btn1.pack()
btn2.pack()
btn3.pack(side = "left")
 
mainFrame.mainloop()