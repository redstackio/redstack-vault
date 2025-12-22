---
type: command
executor: powershell
data: >-
  $cred = New-Object System.Management.Automation.PSCredential('RetailAdmin',
  (ConvertTo-SecureString 'trs10' -AsPlainText -Force)); Enter-PSSession
  -ComputerName $_TARGET_SERVER -Credential $cred
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credential-access
  - remote-login
verified: true
validated: true
---

# login-with-retailadmin-credentials

## Command

```powershell
$cred = New-Object System.Management.Automation.PSCredential('RetailAdmin', (ConvertTo-SecureString 'trs10' -AsPlainText -Force)); Enter-PSSession -ComputerName $_TARGET_SERVER -Credential $cred
```

## Description

This command authenticates to a remote Windows server using the RetailAdmin credentials and establishes an interactive PowerShell session for further actions like data extraction. Use it after obtaining credentials to simulate retail system access in a controlled environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_SERVER | IP address or hostname of the target retail server | Yes |
| 'RetailAdmin' | Fixed username for the retail admin account | Yes (hardcoded) |
| 'trs10' | Fixed password for the account | Yes (hardcoded, change in production) |

## Examples

### Basic Usage

```powershell
$cred = New-Object System.Management.Automation.PSCredential('RetailAdmin', (ConvertTo-SecureString 'trs10' -AsPlainText -Force)); Enter-PSSession -ComputerName 192.168.1.100 -Credential $cred
```

### Advanced Usage

For non-interactive use, combine with Invoke-Command:

```powershell
$cred = New-Object System.Management.Automation.PSCredential('RetailAdmin', (ConvertTo-SecureString 'trs10' -AsPlainText -Force)); Invoke-Command -ComputerName 192.168.1.100 -Credential $cred -ScriptBlock { Get-Process }
```

## Expected Output

Successful execution prompts an interactive session:

```
[192.168.1.100]: PS C:\Users\RetailAdmin\Documents> 
```

If failed, errors like 'Access is denied' or 'Connecting to remote server failed' appear.

## Related

- [[procedures/windows-retail-credential-theft]]
