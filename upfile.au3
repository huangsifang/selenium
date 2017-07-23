WinActivate("打开");

;ControlFocus("title","text",controlID) Edit1 = Edit instance 1
ControlFocus("请选择要加载的文件", "", "Edit1")

;wait 10 seconds for the Upload window tp appear
WinWait("[CLASS:#32770]","",10)

;Set the File name text on the Edit field
ControlSetText("请选择要加载的文件", "", "Edit1", "E:\downloads\2.zip")
Sleep(2000)

;Click on the Open button
ControlClick("请选择要加载的文件", "", "Button1");