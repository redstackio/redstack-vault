---
id: a57b7ff5-3ed0-4526-a454-b1514a7b9456
name: Disable PowerShell Execution Policy Restrictions
type: command
executor: powershell
data: Set-ExecutionPolicy Unrestricted
output: 'PS C:\Windows\system32> Set-ExecutionPolicy Unrestricted


  Execution Policy Change

  The execution policy helps protect you from scripts that you do not trust. Changing
  the execution policy might expose

  you to the security risks described in the about_Execution_Policies help topic at

  https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution
  policy?

  [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is
  "N"): A

  PS C:\Windows\system32>'
created_at: '2020-03-10T21:52:48.532165+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
- '[[SET]]'
- '[[ps]]'
---

# Disable PowerShell Execution Policy Restrictions

```powershell
Set-ExecutionPolicy Unrestricted
```

## Expected Output

```
PS C:\Windows\system32> Set-ExecutionPolicy Unrestricted

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): A
PS C:\Windows\system32>
```


