Function CPF_S_to_C(CPF As String)
    Dim Part_1, Part_2, Part_3, Part_4, Part_5  As String
    Dim n As Integer
    
    n = Len(CPF)
    
    Part_4 = Right(CPF, 2)
    Part_3 = Left(Right(CPF, 5), 3)
    Part_2 = Left(Right(CPF, 8), 3)
    
    If n = 11 Then
        Part_1 = Left(CPF, 3)
    ElseIf n = 10 Then
        Part_1 = "0" & Left(CPF, 2)
    ElseIf n = 9 Then
        Part_1 = "00" & Left(CPF, 1)
    ElseIf n = 8 Then
        Part_1 = "000"
    Else
        Part_1 = "Error"
    End If
    
    If Part_1 = "Error" Then
        CPF_S_to_C = Part_1
    Else
        CPF_S_to_C = Part_1 & "." & Part_2 & "." & Part_3 & "-" & Part_4
    End If
    
End Function
