Sub RegisterUDF()
    Dim s As String
    
    s = "Pega a quantidade de dias e coloca o que sobrou dps do IOF"
    
    Application.MacroOptions Macro:="Sobrou_depois_do_IOF", Description:=s, Category:=14
    
End Sub