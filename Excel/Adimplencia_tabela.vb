Function Adimplencia_tabela(INICIO As Date, i As Integer, tx30e As Double, tx30c As Double, FERIADOS As Range)
    Dim d_i, d_i_less_1 As Integer
    
    d_i = Application.WorksheetFunction.WorkDay(Application.WorksheetFunction.EDate(INICIO, i) - 1, 1, FERIADOS) - INICIO
    
    If i = 1 Then
        Adimplencia_tabela = ((1 + tx30e) / (1 + tx30c)) ^ (d_i / 30)
    ElseIf i > 1 Then
        d_i_less_1 = Application.WorksheetFunction.WorkDay(Application.WorksheetFunction.EDate(INICIO, i - 1) - 1, 1, FERIADOS) - INICIO
        Adimplencia_tabela = 1 + ((1 + tx30e) / (1 + tx30c)) ^ (d_i / 30) - ((1 + tx30e) / (1 + tx30c)) ^ (d_i_less_1 / 30)
    Else
        Adimplencia_tabela = "Erro! i < 1"
    End If
End Function
