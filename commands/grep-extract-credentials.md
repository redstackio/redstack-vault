---
data: grep -E 'username|password' filename
tags:
  - credential-extraction
type: command
executor: bash
platforms:
  - Linux
id: 632014be-240f-43d8-8b82-1907eecfc619
created_at: '2025-12-11T03:47:59.565Z'
updated_at: '2025-12-11T03:47:59.565Z'
verified: false
validated: true
submitted: true
---
# grep-extract-credentials

## Command

```bash
grep -E 'username|password' filename
```

## Description

Searches files for patterns matching usernames and passwords, useful for extracting credentials from downloaded data like VPN cache files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-E` | Extended regex mode | Yes |
| `'username|password'` | Pattern to search for | Yes |
| `filename` | File to search | Yes |

## Examples

### Basic Usage

```bash
grep -E 'username|password' /data/runtime/mtmp/system
```

### Advanced Usage

```bash
grep -E 'username|password' /data/runtime/mtmp/lmdb/dataa/data.mdb > credentials.txt
```

## Expected Output

Extracted lines containing username/password pairs, e.g., '█████████ / ████'.

## Related

- [[procedures/Extract-Credentials-from-Downloaded-VPN-Files]]
