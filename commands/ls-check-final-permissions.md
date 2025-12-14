---
id: c-ls-final
name: ls-check-final-permissions
type: command
executor: bash
data: ls -l cookie.jar
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.733Z'
platforms:
  - Linux
tags:
  - verification
  - permissions
  - exposure
verified: false
validated: true
submitted: true
---

# ls-check-final-permissions

## Command

```bash
ls -l cookie.jar
```

## Description

Lists the detailed attributes of cookie.jar after curl execution to verify the permission change to group/world readable (0644).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Long format including permissions, owner, group, size, date | Yes |
| `cookie.jar` | Target filename | Yes |

## Examples

### Basic Usage

```bash
ls -l cookie.jar
```

### Advanced Usage

```bash
ls -l cookie.jar | awk '{print $1}'  # Extract permissions only
```

## Expected Output

-rw-r--r-- 1 user group [size] [date] cookie.jar (confirms 0644 mode and exposure).

## Related

- [[commands/curl-save-cookies-to-jar]]
- [[procedures/Verify-Changed-File-Permissions]]
