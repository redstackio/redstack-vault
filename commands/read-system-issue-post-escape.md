---
id: cmd-cat-etc-issue-escape
data: cat /etc/issue
tags:
  - escape-verification
  - host-access
type: command
output: Ubuntu 18.04.4 LTS \n \l
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.780Z'
verified: false
validated: true
submitted: true
---
# read-system-issue-post-escape

## Command

```bash
cat /etc/issue
```

## Description

Read system issue file after escape to verify host access.

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
cat /etc/os-release
```

## Expected Output

Ubuntu 18.04.4 LTS \n \l.

## Related

- [[commands/modify-dotfile-post-escape]]
- [[procedures/Verify-Host-Access-After-Escape]]
