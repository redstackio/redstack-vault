---
id: 34e2be3c-87f7-458f-bdcf-70bd78f569bd
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.662133+00:00'
updated_at: '2023-04-10T20:37:46.214076+00:00'
---

# Code Snippet 34e2be3c

**Language**: Powershell

```powershell
wmic service get name,displayname,pathname,startmode |findstr /i "Auto" |findstr /i /v "C:\Windows\\" |findstr /i /v """

wmic service get name,displayname,startmode,pathname | findstr /i /v "C:\Windows\\" |findstr /i /v """

gwmi -class Win32_Service -Property Name, DisplayName, PathName, StartMode | Where {$_.StartMode -eq "Auto" -and $_.PathName -notlike "C:\Windows*" -and $_.PathName -notlike '"*'} | select PathName,DisplayName,Name
```


