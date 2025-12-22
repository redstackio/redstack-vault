---
id: 7ed7d02c-4fc7-4bbd-823a-969706e96549
name: check-doas-presence
type: command
executor: bash
data: which doas || echo "doas not found"
output: null
created_at: '2023-04-06T03:56:19.040307+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - privilege-escalation
verified: true
validated: true
---

# check-doas-presence

## Command

```bash
which doas || echo "doas not found"
```

## Description

This command checks if the doas executable is present in the system's PATH, indicating whether the doas utility is installed and available for potential exploitation in privilege escalation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `which` | Built-in command to locate executables in PATH | Yes |
| `doas` | The target executable to check | Yes |
| `|| echo \"doas not found\"` | Fallback message if not found | No |

## Examples

### Basic Usage

```bash
which doas || echo "doas not found"
```

### Advanced Usage

Combine with other checks:
```bash
which doas && echo "Doas available" || echo "Fallback to sudo check"
```

## Expected Output

If doas is installed:
```
/usr/bin/doas
```

If not installed:
```
doas not found
```

## Related

- [[procedures/Linux-Privilege-Escalation-via-Doas-Misconfiguration]]
- [[commands/view-doas-configuration]]
