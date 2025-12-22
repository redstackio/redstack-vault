---
type: command
executor: powershell
data: 'Get-NetIPConfiguration | ft InterfaceAlias,InterfaceDescription,IPv4Address'
output: null
platforms:
  - Windows
tags:
  - network-enumeration
  - discovery
verified: true
validated: true
---

# get-net-ip-configuration

## Command

```powershell
Get-NetIPConfiguration | ft InterfaceAlias,InterfaceDescription,IPv4Address
```

## Description

Retrieves IP configuration details for network adapters, focusing on aliases, descriptions, and IPv4 addresses. PowerShell alternative to ipconfig for scripted enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| InterfaceAlias | Filters by interface name | No |
| InterfaceDescription | Shows adapter description | Built-in |
| IPv4Address | Displays IPv4 addresses | Built-in |
| ft | Formats as table | Yes |

## Examples

### Basic Usage

```powershell
Get-NetIPConfiguration | ft InterfaceAlias,InterfaceDescription,IPv4Address
```

## Expected Output

```
InterfaceAlias InterfaceDescription                    IPv4Address
-------------- --------------------                    -----------
Ethernet       Intel(R) Ethernet Connection (2)      192.168.1.100
Wi-Fi          Intel(R) Wi-Fi 6 AX201 160MHz         10.0.0.50
```

## Related

- [[procedures/windows-network-enumeration-for-privilege-escalation]]
