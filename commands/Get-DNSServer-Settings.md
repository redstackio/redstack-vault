---
id: 4de4020d-a4cc-4afc-8211-0c9dc23969c2
name: Get-DNSServer-Settings
type: command
executor: powershell
data: $dnsettings = Get-DnsServerSetting -ComputerName <servername> -Verbose -All
output: null
created_at: '2023-04-06T03:56:06.475008+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - dns
  - configuration
verified: true
validated: true
---

# Get-DNSServer-Settings

## Command

```powershell
$dnsettings = Get-DnsServerSetting -ComputerName <servername> -Verbose -All
```

## Description

Retrieves all DNS server settings into a variable for modification, such as updating the plugin DLL path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName | Target server name or IP | Yes |
| -Verbose | Detailed output | No |
| -All | All settings | Built-in |

## Examples

### Basic Usage

```powershell
$dnsettings = Get-DnsServerSetting -ComputerName DC01 -Verbose -All
```

## Expected Output

```
ServerLevelPluginDll : 
...
```

Object with current settings, including plugin DLL path.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
