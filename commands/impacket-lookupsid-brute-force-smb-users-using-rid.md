---
id: fc0ae50f-6c12-4e92-a256-304b6af90dc1
name: impacket-lookupsid-brute-force-smb-users-using-rid
type: command
executor: bash
data: 'lookupsid.py ''$_USERNAME:$_PASSWORD''@$_TARGET_IP'
output: |-
  [*] Brute forcing SIDs
  500: TARGET\Administrator (SidTypeUser)
created_at: '2019-12-27T22:38:42.675982+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - sid
verified: true
validated: true
---

# impacket-lookupsid-brute-force-smb-users-using-rid

## Command

```bash
lookupsid.py '$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

## Description

Uses Impacket to brute-force SIDs for user enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME:$_PASSWORD | Creds in format user:pass | Yes |
| $_TARGET_IP | Target IP | Yes |

## Examples

### Basic Usage

```bash
lookupsid.py 'bob:pass'@10.10.10.10
```

## Expected Output

SID and user list.

## Related

- [[procedures/brute-force-smb-users-using-rid-authenticated]]
