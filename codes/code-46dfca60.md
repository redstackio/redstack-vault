---
id: 46dfca60-8ee2-4872-9f02-fcaf3632dbc2
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.769525+00:00'
updated_at: '2023-04-10T20:37:28.590627+00:00'
---

# Code Snippet 46dfca60

**Language**: Powershell

```powershell
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add -o env
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "logonscript" -m add
```
