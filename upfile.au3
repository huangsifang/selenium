WinActivate("��");

;ControlFocus("title","text",controlID) Edit1 = Edit instance 1
ControlFocus("��ѡ��Ҫ���ص��ļ�", "", "Edit1")

;wait 10 seconds for the Upload window tp appear
WinWait("[CLASS:#32770]","",10)

;Set the File name text on the Edit field
ControlSetText("��ѡ��Ҫ���ص��ļ�", "", "Edit1", "E:\downloads\2.zip")
Sleep(2000)

;Click on the Open button
ControlClick("��ѡ��Ҫ���ص��ļ�", "", "Button1");