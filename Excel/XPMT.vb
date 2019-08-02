Function XPMT(value As Double, tx360 As Double, dates As Range)
    
    Dim i, j, n, m As Integer
    Dim tx1 As Double
    
    tx1 = (1 + tx360) ^ (1 / 360) - 1
    n = dates.Count
    m = 0
    For i = 1 To n
        If IsDate(dates(i).value) Then
            m = m + 1
        End If
    Next i
    
    'Agora m é a quantidade de dias válidos
    
    ReDim truedates(m - 1) As Date
    
    j = 0
    For i = 1 To n
        If IsDate(dates(i).value) Then
            truedates(j) = dates(i).value
            j = j + 1
        End If
    Next i
    
    ReDim dias(m - 1) As Integer
    ReDim mult(m - 1) As Double
    
    For i = 0 To m - 1
        dias(i) = truedates(i) - truedates(0)
        mult(i) = 1 / (1 + tx1) ^ (dias(i))
    Next i
    
    sum_factors = Application.WorksheetFunction.Sum(mult) - 1
    
    XPMT = -value / sum_factors
    
End Function
