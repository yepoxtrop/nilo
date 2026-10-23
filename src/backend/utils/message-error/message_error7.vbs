Dim primerParametro
If WScript.Arguments.Count > 0 Then
    primerParametro = WScript.Arguments.Item(0)
Else
    primerParametro = "the application"
End If

x=msgbox("We found problems to open some system applications, review " & primerParametro, 0+16, "FATAL CRITICAL ERROR")
