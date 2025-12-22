---
id: 6aae448a-96b2-487f-9565-b63088004bb3
name: netsh-trace-start-persistent
type: command
executor: cmd
data: >-
  netsh trace start capture=yes report=disabled persistent=yes
  tracefile=$_TRACEFILE maxsize=$_MAXSIZE
output: null
created_at: '2023-04-06T03:56:23.097114+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Windows
tags:
  - netsh-trace
  - persistent
verified: true
validated: true
---

# netsh-trace-start-persistent

## Command

```cmd
netsh trace start capture=yes report=disabled persistent=yes tracefile=$_TRACEFILE maxsize=$_MAXSIZE
```

## Description

Starts a network trace that persists across system reboots for ongoing monitoring.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| persistent=yes | Enable reboot persistence | Yes |
| tracefile=$_TRACEFILE | ETL output path | Yes |
| maxsize=$_MAXSIZE | Size limit in MB | Yes |

## Examples

### Basic Usage

```cmd
netsh trace start capture=yes report=disabled persistent=yes tracefile=c:\trace.etl maxsize=16384
```

## Expected Output

"Trace configuration started. Persistent trace enabled."

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/netsh-trace-stop]]
