from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
 
mainFrame = Tk()
mainFrame.geometry( '400x300' )
 
lbl1 = Label( mainFrame )
lbl2 = Label( mainFrame )
lbl1["text"] = "바보"
lbl2["text"] = "천재"
 
def onClick() :
    choice = tkinter.messagebox.askyesno( "질문", "선택해주세요" )
    if choice :
        lbl1["background"] = "blue"
    else :
        lbl2["background"] = "red"
        
btn1 = Button( mainFrame, text = "버튼", command = onClick )
 
lbl1.pack()
lbl2.pack()
btn1.pack()
 
mainFrame.mainloop()