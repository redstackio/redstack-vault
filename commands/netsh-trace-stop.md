---
id: 130c2fe8-db4d-4daa-afc0-8879ea7a9596
name: netsh-trace-stop
type: command
executor: cmd
data: netsh trace stop
output: null
created_at: '2023-04-06T03:56:23.097021+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Windows
tags:
  - netsh-trace
  - stop-capture
verified: true
validated: true
---

# netsh-trace-stop

## Command

```cmd
netsh trace stop
```

## Description

Stops an active netsh trace session, finalizing the ETL file for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters needed | N/A |

## Examples

### Basic Usage

```cmd
netsh trace stop
```

## Expected Output

"Trace configuration stopped."

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/etl2pcapng-convert-trace]]
