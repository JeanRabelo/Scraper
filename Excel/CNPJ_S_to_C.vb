Function CNPJ_S_to_C(CNPJ As String)
    Dim Part_1, Part_2, Part_3, Part_4, Part_5  As String
    Dim n As Integer
    
    n = Len(CNPJ)
    
    Part_5 = Right(CNPJ, 2)
    Part_4 = Left(Right(CNPJ, 6), 4)
    Part_3 = Left(Right(CNPJ, 9), 3)
    Part_2 = Left(Right(CNPJ, 12), 3)
    
    If n = 14 Then
        Part_1 = Left(CNPJ, 2)
    ElseIf n = 13 Then
        Part_1 = "0" & Left(CNPJ, 1)
    ElseIf n = 12 Then
        Part_1 = "00"
    Else
        Part_1 = "Error"
    End If
    
    If Part_1 = "Error" Then
        CNPJ_S_to_C = Part_1
    Else
        CNPJ_S_to_C = Part_1 & "." & Part_2 & "." & Part_3 & "/" & Part_4 & "-" & Part_5
    End If
    
End Function