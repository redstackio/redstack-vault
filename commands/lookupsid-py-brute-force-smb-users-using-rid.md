---
type: command
executor: bash
data: 'lookupsid.py ''$_USERNAME:$_PASSWORD''@$_TARGET_IP'
output: |-
  [*] Brute forcing SIDs at 10.10.10.10
  [*] Domain SID is: S-1-5-21-...
  500: DOMAIN\Administrator (SidTypeUser)
  1001: DOMAIN\user (SidTypeUser)
platforms:
  - Windows
tags:
  - rid
  - impacket
verified: true
validated: true
---

# lookupsid-py-brute-force-smb-users-using-rid

## Command

```bash
lookupsid.py '$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

## Description

Uses Impacket to bruteforce SID enumeration via LSA lookups over SMB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Valid username | Yes |
| $_PASSWORD | Valid password | Yes |
| $_TARGET_IP | Target IP | Yes |

## Examples

### Basic Usage

```bash
lookupsid.py 'user:pass'@10.10.10.10
```

### Advanced Usage

```bash
lookupsid.py 'user:pass'@10.10.10.10 -hashes aad3b435b51404eeaad3b435b51404ee:...
```

## Expected Output

Bruteforced SIDs with usernames.

## Related

- [[procedures/brute-force-smb-users-using-rid-authenticated]]
- [[tools/Impacket]]
