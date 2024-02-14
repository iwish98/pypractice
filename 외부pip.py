import wx
		
app = wx.App()	
frame = wx.Frame( None, pos = (100, 0), title = "좌", size = ( 500, 400 ), name = "frameName", id = wx.ID_ANY)

lbl = wx.StaticText( frame, label = "라벨에 입력된 텍스트" )
	
def onClick( event ) :
	
    print( "Clicked" )

btn = wx.Button( frame, label = "클릭" )
btn.Bind( wx.EVT_BUTTON, onClick )
btn.SetPosition( wx.Point( 150, 100 ) )

frame.Show( True )	
app.MainLoop()