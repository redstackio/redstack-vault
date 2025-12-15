---
id: cmd-cat-read-001
data: cat /var/run/ubnt-session
tags:
  - file-read
  - recon
type: command
output: |-
  SESSION_TOKEN=abc123
  UBNT_USER=ubnt
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.950Z'
verified: false
validated: true
submitted: true
---
# cat-file-read

## Command

```bash
cat /var/run/ubnt-session
```

## Description

Reads content of exposed session files to extract sensitive data for hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| File path | Target file | Yes |

## Examples

### Basic Usage

```bash
cat /var/run/ubnt-session
```

### Advanced Usage

```bash
cat /var/run/ubnt-session | grep TOKEN
```

## Expected Output

Session tokens or credentials in plain text.

## Related

- [[commands/ls-directory-list]]
