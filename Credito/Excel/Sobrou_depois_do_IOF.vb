Function Sobrou_depois_do_IOF(d_i As Integer)
    Dim Wsf As Object
    Dim Porcentagem As Double
    
    Set Wsf = Application.WorksheetFunction
    
    Porcentagem = (4 / 100) * d_i - (1 / 100) * (Wsf.Quotient(d_i, 3) * 2 + Wsf.GeStep(((d_i - 1) Mod 3), 1) * Wsf.GeStep((d_i Mod 3), 1))
    
    Sobrou_depois_do_IOF = Wsf.Min(Wsf.Max(Porcentagem, 0), 1)
    
End Function
