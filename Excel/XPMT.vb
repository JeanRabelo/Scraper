Function XPMT(value As Double, tx360 As Double, dates As Range)
    
    Dim i, n As Integer
    Dim tx1 As Double
    
    tx1 = (1 + tx360) ^ (1 / 360) - 1
    n = dates.Count
    
    ReDim dias(n - 1) As Integer
    ReDim mult(n - 1) As Double
    
    For i = 0 To n - 1
        dias(i) = dates(i + 1).value - dates(1).value
        mult(i) = 1 / (1 + tx1) ^ (dias(i))
    Next i
    
    sum_factors = Application.WorksheetFunction.Sum(mult) - 1
    
    XPMT = -value / sum_factors
    
End Function
