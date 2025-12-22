---
type: command
executor: bash
data: python3 ./rpcdump.py @$_TARGET_IP | egrep 'MS-RPRN|MS-PAR'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - enumeration
  - rpc
verified: true
validated: true
---

# rpcdump-filter-ms-rprn-ms-par

## Command

```bash
python3 ./rpcdump.py @$_TARGET_IP | egrep 'MS-RPRN|MS-PAR'
```

## Description

Uses Impacket's rpcdump to enumerate RPC interfaces on a remote Windows target and filters for Print Spooler protocols (MS-RPRN and MS-PAR) to confirm PrintNightmare vulnerability exposure. Requires Impacket installed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target Windows IP address (e.g., 10.10.10.10) | Yes |
| @ | Impacket syntax for remote host | Yes |
| egrep pattern | Filters for 'MS-RPRN|MS-PAR' | Yes |

## Examples

### Basic Usage

```bash
python3 ./rpcdump.py @10.10.10.10 | egrep 'MS-RPRN|MS-PAR'
```

## Expected Output

Protocol: [MS-RPRN]: Print System Remote Protocol
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol

## Related

- [[procedures/PrintNightmare-Remote-Code-Execution]]
