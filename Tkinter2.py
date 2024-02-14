from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
 
mainFrame = Tk()
mainFrame.geometry( '400x300' )

	
lbl1 = Label( mainFrame )
lbl2 = Label( mainFrame )
lbl1["text"] = "예"
lbl2["text"] = "아니오"


def inputBox() :
    name = tkinter.simpledialog.askstring( "질문", "이름을 입력하세요" )
    age = tkinter.simpledialog.askstring( "질문", "나이를 입력하세요" )
 
    lbl1["text"] = name
    lbl2["text"] = age

    	
btn1 = Button( mainFrame, text = "클릭", command = inputBox )
 
lbl1.pack()
lbl2.pack()
btn1.pack()
 
mainFrame.mainloop()