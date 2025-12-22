---
id: 7283d00a-2b01-49a9-af62-1523d6693672
name: netsh-trace-start-basic
type: command
executor: cmd
data: >-
  netsh trace start capture=yes report=disabled tracefile=$_TRACEFILE
  maxsize=$_MAXSIZE
output: null
created_at: '2023-04-06T03:56:23.096960+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Windows
tags:
  - netsh-trace
  - basic-capture
verified: true
validated: true
---

# netsh-trace-start-basic

## Command

```cmd
netsh trace start capture=yes report=disabled tracefile=$_TRACEFILE maxsize=$_MAXSIZE
```

## Description

Starts a basic network trace on Windows, capturing packets to an ETL file without diagnostic reports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| capture=yes | Enable packet capture | Yes |
| report=disabled | Disable XML reports | Yes |
| tracefile=$_TRACEFILE | Output file path (e.g., c:\trace.etl) | Yes |
| maxsize=$_MAXSIZE | Max file size in MB (e.g., 16384) | Yes |

## Examples

### Basic Usage

```cmd
netsh trace start capture=yes report=disabled tracefile=c:\trace.etl maxsize=16384
```

### Smaller File

```cmd
netsh trace start capture=yes report=disabled tracefile=c:\small.etl maxsize=1024
```

## Expected Output

"Trace configuration started."

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/netsh-trace-stop]]
