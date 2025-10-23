---
id: e636d41a-b0b1-407e-bdc9-bb9eaf57a7ca
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.198237+00:00'
updated_at: '2023-04-10T20:36:49.329949+00:00'
---

# Code Snippet e636d41a

**Language**: ps1

```ps1
Generate CS Macro and save it to Windows as vba.txt
PS> New-Item blank.xlsm
PS> C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll hot-manchego.cs
PS> .\hot-manchego.exe .\blank.xlsm .\vba.txt
```


