---
type: command
executor: cmd
data: wmic qfe
output: null
created_at: '2023-04-06T03:56:28.589201+00:00'
updated_at: '2023-04-10T20:37:36.292864+00:00'
platforms:
  - Windows
tags:
  - discovery
  - updates
verified: true
validated: true
---

# cmd-list-installed-hotfixes

## Command

```cmd
wmic qfe
```

## Description

Queries Windows Management Instrumentation (WMI) for installed hotfixes and updates (Quick Fix Engineering). Essential for checking patch levels during privilege escalation to spot unpatched vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| qfe | Queries the Quick Fix Engineering class | Built-in |

No additional parameters needed.

## Examples

### Basic Usage

```cmd
wmic qfe
```

### Advanced Usage

List with specific fields: `wmic qfe get HotFixID,InstalledOn`

## Expected Output

```
HotFixID   InstalledOn       Description
KB1234567  2023-01-15        Security Update
KB7890123  2023-02-20        Cumulative Update
```

Success shows a table of installed updates; empty or partial list indicates patching gaps.

## Related

- [[procedures/windows-os-information-gathering-for-privilege-escalation]]
