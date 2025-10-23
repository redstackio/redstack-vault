---
id: 9166419a-47b7-42d4-830d-d2f13b4dd967
name: Add a new hourly schtask persistence using SharPersist
type: command
executor: bash
data: SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Task" -m add -o hourly
output: null
created_at: '2023-04-06T03:56:16.649875+00:00'
updated_at: '2023-04-10T20:36:23.644724+00:00'
---

# Add a new hourly schtask persistence using SharPersist

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```


