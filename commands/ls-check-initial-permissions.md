---
id: c-ls-initial
name: ls-check-initial-permissions
type: command
executor: bash
data: ls -l cookie.jar
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.758Z'
platforms:
  - Linux
tags:
  - verification
  - permissions
verified: false
validated: true
submitted: true
---

# ls-check-initial-permissions

## Command

```bash
ls -l cookie.jar
```

## Description

Lists the detailed attributes of cookie.jar in long format to verify initial secure permissions before vulnerability exploitation.

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
ls -l cookie.jar | grep permissions
```

## Expected Output

-rw------- 1 user group 0 [date] cookie.jar (confirms 0600 mode).

## Related

- [[commands/install-create-cookie-jar]]
- [[procedures/Create-and-Verify-Secure-Cookie-Jar-File]]
