---
type: command
executor: cmd
data: wmic qfe list | findstr "3139914"
output: null
created_at: '2023-04-06T03:56:30Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - recon
  - vulnerability-check
verified: true
validated: true
---

# check-windows-update-kb3139914

## Command

```cmd
wmic qfe list | findstr "3139914"
```

## Description

This command queries the list of installed Windows hotfixes (Quick Fix Engineering) and filters for KB3139914, the patch for MS16-032. Use it to determine if a Windows system is vulnerable to the privilege escalation exploit. Run as any user on the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses default wmic output filtering. | No |

## Examples

### Basic Usage

```cmd
wmic qfe list | findstr "3139914"
```

### With Brief Output (Alternative)

```cmd
wmic qfe get HotFixID | findstr "3139914"
```

## Expected Output

If patched:

```
KB3139914
```

If vulnerable (unpatched): No output (empty result).

## Related

- [[procedures/MS16-032-Local-Privilege-Escalation]]
