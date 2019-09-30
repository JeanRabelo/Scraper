Function Correl_Spearman(range1 As Range, range2 As Range)
    'Check
    If range1.Count <> range2.Count Then
        Correl_Spearman = "Ranges de tamanhos diferentes"
    End If
    
    Dim n, i As Integer
    
    n = range1.Count
    
    ReDim rank1(n - 1) As Integer
    ReDim rank2(n - 1) As Integer
    ReDim diff_quad(n - 1) As Integer
    
    'Definir Ranks
    For i = 0 To n - 1
        rank1(i) = Application.WorksheetFunction.Rank(range1(i + 1).Value, range1)
        rank2(i) = Application.WorksheetFunction.Rank(range2(i + 1).Value, range2)
    Next i
    
    'Definir diff_quadrada
    For i = 0 To n - 1
        diff_quad(i) = (rank1(i) - rank2(i)) ^ 2
    Next i
    
    Correl_Spearman = 1 - 6 * Application.WorksheetFunction.Sum(diff_quad) / (n * (n ^ 2 - 1))
    
End Function