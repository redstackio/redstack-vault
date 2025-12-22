---
id: c9860073-8018-40bc-922c-86d0fddb8701
name: cytool-disable-startup
type: command
executor: powershell
data: cytool.exe startup disable
output: null
created_at: '2023-04-06T03:56:27.633012+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - antivirus-removal
  - persistence
verified: true
validated: true
---

# cytool-disable-startup

## Command

```powershell
cytool.exe startup disable
```

## Description

Disables the Cortex XDR agent from starting automatically on system boot using the cytool utility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard disable command | No |

## Examples

### Basic Usage

```powershell
cytool.exe startup disable
```

## Expected Output

```
Startup disabled successfully.
```

Or no output if successful; test by rebooting and checking if agent launches.

## Related

- [[procedures/disable-elastic-agent-and-cortex-xdr-on-windows]]
