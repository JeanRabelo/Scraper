Function Sobrou_depois_do_IOF(d_i As Integer)
    
    Dim Wsf As Object
    
    Set Wsf = Application.WorksheetFunction
    
    Sobrou_depois_do_IOF = (4 / 100) * d_i - (1 / 100) * (Wsf.Quotient(d_i, 3) * 2 + Wsf.GeStep((d_i - 1) Mod 3, 3) * Wsf.GeStep(d_i Mod 3, 3))

End Function