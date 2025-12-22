---
id: a57b7ff5-3ed0-4526-a454-b1514a7b9456
name: set-powershell-execution-policy-unrestricted
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
created_at: '2020-03-10T21:52:48.532165+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powershell
  - configuration
verified: true
validated: true
---

# set-powershell-execution-policy-unrestricted

## Command

```powershell
Set-ExecutionPolicy Unrestricted
```

## Description

This command sets the PowerShell execution policy to 'Unrestricted', allowing all scripts to run without restrictions or prompts. It is commonly used during setup of pentesting environments like Commando VM to enable running unsigned scripts. Use with caution as it reduces security protections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Unrestricted | Sets the policy to allow all scripts (no parameters needed beyond the policy name) | Yes |

Note: No additional flags are required, but the command prompts for confirmation to prevent accidental changes.

## Examples

### Basic Usage

Run as Administrator to change the policy for the current user or machine:

```powershell
Set-ExecutionPolicy Unrestricted
```

Respond with 'A' (Yes to All) when prompted.

### Advanced Usage

To apply to the local machine scope (requires admin):

```powershell
Set-ExecutionPolicy Unrestricted -Scope LocalMachine
```

## Expected Output

```
PS C:\Windows\system32> Set-ExecutionPolicy Unrestricted

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https://go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): A
PS C:\Windows\system32>
```

The prompt appears, and after confirming, the policy is updated. Verify with `Get-ExecutionPolicy`.

## Related

- [[tools/commando-vm]] (Used during installation)

*Last updated: 2023-05-29T16:48:52.884824+00:00*
