---
id: f980fd6f-8c40-4220-8cf5-7443428e2815
name: 'JAWS Enumerate for Privilege Escalation '
type: command
executor: powershell
data: Import-Module .\jaws-enum.ps1 -OutputFileName $_OUTPUT.txt
output: "PS C:\\Users\\Bob\\Downloads> Import-Module .\\jaws-enum.ps1 -OutputFileName\
  \ Jaws-Enum.txt\n\nRunning J.A.W.S. Enumeration\n        - Gathering User Information\n\
  \        - Gathering Processes, Services and Scheduled Tasks\n        - Gathering\
  \ Installed Software\n        - Gathering File System Information\n        - Looking\
  \ for Simple Priv Esc Methods"
created_at: '2019-11-26T19:36:52.433603+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Scheduled Tasks]]'
- '[[ps]]'
---

# JAWS Enumerate for Privilege Escalation 

```powershell
Import-Module .\jaws-enum.ps1 -OutputFileName $_OUTPUT.txt
```

## Expected Output

```
PS C:\Users\Bob\Downloads> Import-Module .\jaws-enum.ps1 -OutputFileName Jaws-Enum.txt

Running J.A.W.S. Enumeration
        - Gathering User Information
        - Gathering Processes, Services and Scheduled Tasks
        - Gathering Installed Software
        - Gathering File System Information
        - Looking for Simple Priv Esc Methods
```


