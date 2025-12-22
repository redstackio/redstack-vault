---
id: 14465998-4f8d-431f-9cbd-3117dd5fbe33
name: seatbelt-all-full-checks
type: command
executor: cmd
data: Seatbelt.exe -group=all -full
output: null
created_at: '2023-04-06T03:56:28.514012+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - safety-checks
verified: true
validated: true
---

# seatbelt-all-full-checks

## Command

```cmd
Seatbelt.exe -group=all -full
```

## Description

Runs all Seatbelt security checks in full mode to survey host for privesc risks like weak permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -group=all | Checks all categories (system, user, etc.) | Yes |
| -full | Performs exhaustive checks | Yes |

## Examples

### Basic Usage

```cmd
Seatbelt.exe -group=all -full
```

## Expected Output

Detailed console output, e.g., "System Information: RDP Enabled - Potential Lateral Move Vector".

## Related

- [[commands/seatbelt-system-output-file]]
- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
