---
type: command
executor: powershell
data: >-
  $cred = Get-Credential; Enter-PSSession -ComputerName $_TARGET_HOSTNAME
  -Credential $cred -Authentication Basic
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - session
  - powershell
verified: true
validated: true
---

# enter-pssession-basic-auth

## Command

```powershell
$cred = Get-Credential; Enter-PSSession -ComputerName $_TARGET_HOSTNAME -Credential $cred -Authentication Basic
```

## Description

Opens an interactive remote PowerShell session using WinRM with Basic authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOSTNAME | Target hostname or IP | Yes |
| $cred | Credential object from Get-Credential | Yes |
| -Authentication Basic | Use Basic auth | Yes |

## Examples

### Basic Usage

```powershell
$cred = Get-Credential
Enter-PSSession -ComputerName winserver1 -Credential $cred -Authentication Basic
```

### Direct Credentials (Insecure)

```powershell
Enter-PSSession -ComputerName winserver1 -Credential (New-Object System.Management.Automation.PSCredential('admin', (ConvertTo-SecureString 'Pass123' -AsPlainText -Force))) -Authentication Basic
```

## Expected Output

[winserver1]: PS C:\Users\admin\Documents> 

(Type commands here; use Exit to close)

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-identify-basic]]
