---
id: 00e0d44d-6c49-4f11-b325-730be1c892d7
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.436806+00:00'
updated_at: '2023-04-10T20:37:37.001468+00:00'
---

# Code Snippet 00e0d44d

**Language**: Powershell

```powershell
$ for /f "tokens=2 delims='='" %a in ('wmic service list full^|find /i "pathname"^|find /i /v "system32"') do @echo %a >> c:\windows\temp\permissions.txt
$ for /f eol^=^"^ delims^=^" %a in (c:\windows\temp\permissions.txt) do cmd.exe /c icacls "%a"

$ sc query state=all | findstr "SERVICE_NAME:" >> Servicenames.txt
FOR /F %i in (Servicenames.txt) DO echo %i
type Servicenames.txt
FOR /F "tokens=2 delims= " %i in (Servicenames.txt) DO @echo %i >> services.txt
FOR /F %i in (services.txt) DO @sc qc %i | findstr "BINARY_PATH_NAME" >> path.txt
```
