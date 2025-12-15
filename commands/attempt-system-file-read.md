---
id: cmd-attempt-etc-issue
data: cat /etc/issue
tags:
  - confinement-test
  - permission-denied
type: command
output: 'cat: /etc/issue: Permission denied'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.789Z'
verified: false
validated: true
submitted: true
---
# attempt-system-file-read

## Command

```bash
cat /etc/issue
```

## Description

Attempt to read system issue file inside snap to show non-home access denial.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /etc/issue | Target file path | Yes |

## Examples

### Basic Usage

```bash
cat /etc/issue
```

### Advanced Usage

```bash
cat /etc/passwd
```

## Expected Output

Permission denied.

## Related

- [[commands/attempt-dotfile-modification]]
- [[procedures/Demonstrate-Snap-Container-Restrictions]]
