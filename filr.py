	
from tkinter import *
 
mainFrame = Tk()
mainFrame.geometry( "400x200" )
 
menubar = Menu( mainFrame )
mainFrame.config( menu = menubar )
 
item = Menu( menubar )
item2 = Menu( menubar )

menubar.add_cascade( label = "파일", menu = item )
menubar.add_cascade( label = "설정", menu = item2 )

def save() :
    print( "저장 버튼" )

def load() :
    print( "불러오기 버튼" )
 
item.add_command( label = "저장", command = save )
item.add_command( label = "불러오기", command = load )

item2.add_command( label = "edit", command = save )
item2.add_command( label = "power", command = load )


mainFrame.mainloop()