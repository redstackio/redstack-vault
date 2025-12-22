---
id: d4d775af-3a3a-4024-b56c-8d2bb58cae21
name: powershell-disable-smb-signing-client
type: command
executor: powershell
data: >-
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name
  RequireSecuritySignature -Value 0; Restart-Service LanmanWorkstation -Force
output: null
created_at: '2023-04-06T03:56:05.363229+00:00'
updated_at: '2023-04-10T20:26:21.879066+00:00'
platforms:
  - Windows
tags:
  - smb
  - configuration
verified: true
validated: true
---

# powershell-disable-smb-signing-client

## Command

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name RequireSecuritySignature -Value 0
Restart-Service LanmanWorkstation -Force
```

## Description

This PowerShell command disables SMB signing on the client side by setting the registry value to 0 and restarting the Workstation service. Required for SMB relay attacks where clients must accept unsigned authentications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Set-ItemProperty | Modifies registry value | Yes |
| -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" | Registry path | Yes |
| -Name RequireSecuritySignature | Key to modify | Yes |
| -Value 0 | Disables signing | Yes |
| Restart-Service | Restarts service for changes | Yes |
| LanmanWorkstation | Service name | Yes |
| -Force | Forces restart without prompt | No |

## Examples

### Basic Usage

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name RequireSecuritySignature -Value 0
```

### With Service Restart

```powershell
Restart-Service LanmanWorkstation -Force
```

## Expected Output

No output on success; verify with [[commands/powershell-check-smb-signing-enabled]]. Service restart confirmation: The operation completed successfully.

## Related

- [[procedures/SMB-Relay-Attack-via-Disabled-SMB-Signing]]
