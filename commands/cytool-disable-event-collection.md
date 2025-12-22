---
id: b37186bc-9765-4f59-a8e6-8d98105eb153
name: cytool-disable-event-collection
type: command
executor: powershell
data: cytool.exe event_collection disable
output: null
created_at: '2023-04-06T03:56:27.633241+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - event-logging
verified: true
validated: true
---

# cytool-disable-event-collection

## Command

```powershell
cytool.exe event_collection disable
```

## Description

Disables event collection and telemetry sending in Cortex XDR, preventing data from reaching the management console.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard disable command | No |

## Examples

### Basic Usage

```powershell
cytool.exe event_collection disable
```

## Expected Output

```
Event collection disabled.
```

No further logs or network uploads; monitor traffic to confirm.

## Related

- [[procedures/disable-elastic-agent-and-cortex-xdr-on-windows]]
