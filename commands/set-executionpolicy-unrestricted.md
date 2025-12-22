---
type: command
executor: powershell
data: Set-ExecutionPolicy Unrestricted
output: >-
  PS C:\Windows\system32> Set-ExecutionPolicy Unrestricted


  Execution Policy Change

  The execution policy helps protect you from scripts that you do not trust.
  Changing the execution policy might expose

  you to the security risks described in the about_Execution_Policies help topic
  at

  https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the
  execution policy?

  [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default
  is "N"): A

  PS C:\Windows\system32>
platforms:
  - Windows
tags:
  - powershell
  - execution-policy
verified: true
validated: true
---

# Set-ExecutionPolicy Unrestricted

## Command

```powershell
Set-ExecutionPolicy Unrestricted
```

## Description

This command changes the PowerShell execution policy to Unrestricted, allowing all scripts to run without restrictions or prompts. It is commonly used during setup of security tools like Flare VM to enable running unsigned installation scripts. Use with caution as it reduces script security protections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Unrestricted` | Sets the policy to allow all scripts (no signing required) | Yes |
| `-Scope` (optional) | Specifies the scope (e.g., CurrentUser, LocalMachine); defaults to LocalMachine for admin sessions | No |
| `-Force` (optional) | Suppresses confirmation prompts | No |

## Examples

### Basic Usage

Run as Administrator to apply globally:

```powershell
Set-ExecutionPolicy Unrestricted
```

### Advanced Usage

Set for current user only without prompts:

```powershell
Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
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

The prompt requires confirmation (enter 'A' for Yes to All). Successful execution returns to the prompt without errors.

## Related

- [[tools/flare-vm]] (Used in Flare VM installation)
- [[Related Procedure]] (For full script execution workflows)
