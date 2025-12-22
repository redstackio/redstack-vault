---
id: 4e8f872d-31ed-4256-b80e-47cc0b594e8c
name: netsh-trace-start-with-filters
type: command
executor: cmd
data: >-
  netsh trace start capture=yes report=disabled Ethernet.Type=IPv4
  IPv4.Address=$_TARGET_IP tracefile=$_TRACEFILE maxsize=$_MAXSIZE
output: null
created_at: '2023-04-06T03:56:23.097239+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Windows
tags:
  - netsh-trace
  - filtered-capture
verified: true
validated: true
---

# netsh-trace-start-with-filters

## Command

```cmd
netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=$_TARGET_IP tracefile=$_TRACEFILE maxsize=$_MAXSIZE
```

## Description

Initiates a filtered network trace, e.g., for IPv4 traffic to a specific IP, to target relevant communications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Ethernet.Type=IPv4 | Filter to IPv4 | Yes |
| IPv4.Address=$_TARGET_IP | Specific IP address | Yes |
| tracefile=$_TRACEFILE | Output ETL file | Yes |
| maxsize=$_MAXSIZE | File size limit in MB | Yes |

## Examples

### Basic Usage

```cmd
netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3 tracefile=c:\trace.etl maxsize=16384
```

### Multiple Filters

```cmd
netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Protocol=TCP tracefile=c:\trace.etl maxsize=16384
```

## Expected Output

"Trace configuration started."

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/netsh-trace-start-basic]]
