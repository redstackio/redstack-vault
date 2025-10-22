---
id: 05083415-cbda-4f8e-8473-b79f648fa709
name: Add registry key and value for persisting cmd.exe with calc.exe on current user
  run
type: command
executor: bash
data: SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun"
  -v "Test Stuff" -m add
output: null
created_at: '2023-04-06T03:56:27.769566+00:00'
updated_at: '2023-04-10T20:37:28.586667+00:00'
---

# Add registry key and value for persisting cmd.exe with calc.exe on current user run

```bash
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add
```
