---
id: 687ee0a7-7358-42bf-9a53-58da76f37759
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.514528+00:00'
updated_at: '2023-04-10T20:37:50.960310+00:00'
---

# Code Snippet 687ee0a7

**Language**: Powershell

```powershell
C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
```
