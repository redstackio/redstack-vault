---
type: command
executor: bash
data: >-
  python3 dcomexec.py -object MMC20 -silentcommand -debug
  DOMAIN/USERNAME:PASSWORD@TARGET_HOST 'notepad.exe'
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

# DCOMExec Launch Notepad Debug

## Command

```bash
python3 dcomexec.py -object MMC20 -silentcommand -debug DOMAIN/USERNAME:PASSWORD@TARGET_HOST 'notepad.exe'
```

## Description

Launches notepad.exe on the target in silent debug mode via DCOM, providing verbose logs for troubleshooting execution issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -object MMC20 | COM object | Yes |
| -silentcommand | No output retrieval | Yes |
| -debug | Enable debug logging | Yes |
| DOMAIN/USERNAME:PASSWORD@TARGET_HOST | Creds and target | Yes |
| 'notepad.exe' | Binary to launch | Yes |

## Examples

### Basic Usage

```bash
python3 dcomexec.py -object MMC20 -silentcommand -debug 'DOMAIN/USER:PASS@TARGET' 'calc.exe'
```

## Expected Output

Debug logs like "[+] Opening SOCKS proxy" and "[+] MMC20.Application instantiated successfully", with no process output.

## Related

- [[procedures/dcom-lateral-movement]]
- [[tools/Impacket]]
