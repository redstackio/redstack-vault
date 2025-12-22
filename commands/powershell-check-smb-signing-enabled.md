---
id: 38610624-0e9f-4a42-b6c4-44950eca6426
name: powershell-check-smb-signing-enabled
type: command
executor: powershell
data: >-
  Get-SmbServerConfiguration | Select-Object EnableSecuritySignature,
  RequireSecuritySignature; Get-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name
  RequireSecuritySignature
output: null
created_at: '2023-04-06T03:56:05.363134+00:00'
updated_at: '2023-04-10T20:26:21.879066+00:00'
platforms:
  - Windows
tags:
  - smb
  - configuration
verified: true
validated: true
---

# powershell-check-smb-signing-enabled

## Command

```powershell
Get-SmbServerConfiguration | Select-Object EnableSecuritySignature, RequireSecuritySignature
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name RequireSecuritySignature
```

## Description

This PowerShell command queries the SMB server configuration for signing settings and checks the client-side registry key for required security signatures. Use it to determine if SMB signing is enabled, which impacts relay attack feasibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Get-SmbServerConfiguration | Retrieves SMB server settings | Yes |
| Select-Object EnableSecuritySignature, RequireSecuritySignature | Filters for signing properties | Yes |
| Get-ItemProperty | Retrieves registry value | Yes |
| -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" | Registry path for client settings | Yes |
| -Name RequireSecuritySignature | Specific key to query | Yes |

## Examples

### Basic Usage

```powershell
Get-SmbServerConfiguration | Select-Object EnableSecuritySignature, RequireSecuritySignature
```

### Client-Side Check

```powershell
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name RequireSecuritySignature
```

## Expected Output

EnableSecuritySignature : True
RequireSecuritySignature : False

RequireSecuritySignature : 0

Success if RequireSecuritySignature is 0 (disabled) on both client and server for relay attacks.

## Related

- [[procedures/SMB-Relay-Attack-via-Disabled-SMB-Signing]]
