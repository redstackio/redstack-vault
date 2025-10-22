---
id: 3146a3a4-e54d-4089-9cbd-1d2f41bbcb71
name: Search Windows for Installed Patches and Hotfixes
type: procedure
verified: false
submitted: false
created_at: '2020-01-24T21:45:45.045850+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]'
tags:
- '[[Enumeration]]'
- '[[Operating Systems]]'
commands:
- '[[PowerShell Query a System for Installed Patches]]'
- '[[Query a System for Installed Patches]]'
- '[[Sherlock Import Module and Enumerate Vulnerabilities]]'
- '[[systeminfo Display a Systems Configuration Information]]'
---

# Search Windows for Installed Patches and Hotfixes

## Summary

Systems that are not up to date with patched may have vulnerabilities which attackers can exploit. By enumerating installed hotfixes and patches, attackers can identify which updates are missing, and therefore which vulnerabilities may be present. 

## Description

# Description

Systems that are not up to date with patched may have vulnerabilities which attackers can exploit. By enumerating installed hotfixes and patches, attackers can identify which updates are missing, and therefore which vulnerabilities may be present.

# Instructions

## Manual Enumeration via WMIC

Windows Management Instrumentation (WMIC)  is a powerful built-in tool, which among many things, can enumerate installed patches and hotfixes.

**Command** ([[Query a System for Installed Patches]]):

```bash
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## Manual Enumeration via Systeminfo

In cases where wmic is not available, it may be possible to invoke the systeminfo command to view patches and hotfixes

**Command** ([[systeminfo Display a Systems Configuration Information]]):

```bash
systeminfo
```

## Manual Enumeration via PowerShell

**Command** ([[PowerShell Query a System for Installed Patches]]):

```bash
Get-HotFix | Sort-Object HotFixID
```

## Automatic Enumeration via Sherlock

Sherlock is a PowerShell script which will automatically enumerate patches and hotfixes, identify missing patches, and suggest possible exploits and vulnerabilities which may be present. 

1. Download Sherlock.ps1 and import it into a PowerShell session: [Download from GitHub](https://github.com/rasta-mouse/Sherlock/blob/master/Sherlock.ps1)

2. Execute "Find-AllVulns" to run all checks.

**Command** ([[Sherlock Import Module and Enumerate Vulnerabilities]]):

```bash
Find-AllVulns
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]

## Commands Used

- [[PowerShell Query a System for Installed Patches]]
- [[Query a System for Installed Patches]]
- [[Sherlock Import Module and Enumerate Vulnerabilities]]
- [[systeminfo Display a Systems Configuration Information]]

## Tags

- [[Enumeration]]
- [[Operating Systems]]
