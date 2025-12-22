---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - discovery
  - firewall
validated: true
---

# Netsh-Firewall-Discovery-Commands

## Code

```powershell
netsh advfirewall firewall dump
# or 
netsh firewall show state
netsh firewall show config
```

## Description

This snippet provides commands to dump and display the Windows Defender Firewall configuration using netsh, a built-in Windows utility. It is useful for reconnaissance to extract rule sets, profiles, and state information without installing additional software.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; commands are self-contained. | N/A |

## Usage

Execute in an elevated PowerShell or Command Prompt session during post-compromise discovery. Redirect the dump to a file for exfiltration or analysis: `netsh advfirewall firewall dump > config.wfw`. The 'or' alternatives are for legacy compatibility (pre-Windows 8). Use this to identify open ports or rule exceptions for further exploitation.

## Detection

- Windows Event Logs (Event ID 4688 for process creation) showing netsh.exe with advfirewall arguments.
- Sysmon logs capturing command-line parameters containing 'firewall dump' or 'show config'.
- EDR alerts on administrative tool misuse in user contexts.

## Related

- [[procedures/Dump-Windows-Defender-Firewall-Configuration-and-List-Blocked-Ports]]
