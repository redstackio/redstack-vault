---
id: 541e8bf7-5779-4e25-88ad-d2d42a8ded52
name: cytool-disable-protection
type: command
executor: powershell
data: cytool.exe protect disable
output: null
created_at: '2023-04-06T03:56:27.633121+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - tamper-protection
verified: true
validated: true
---

# cytool-disable-protection

## Command

```powershell
cytool.exe protect disable
```

## Description

Disables tamper protection for Cortex XDR files, processes, registry keys, and services, allowing modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard disable command | No |

## Examples

### Basic Usage

```powershell
cytool.exe protect disable
```

## Expected Output

```
Protection disabled.
```

Success allows editing agent components without blocks; verify by attempting file deletion.

## Related

- [[procedures/disable-elastic-agent-and-cortex-xdr-on-windows]]
