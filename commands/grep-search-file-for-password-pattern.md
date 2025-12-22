---
id: 1b029442-33de-4ba1-bbc0-0b4398600025
name: grep-search-file-for-password-pattern
type: command
executor: bash
data: grep -i 'password|secret|key' $_FILE
output: null
created_at: '2023-04-06T03:56:04.401376+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - search
  - pattern-matching
verified: true
validated: true
---

# grep-search-file-for-password-pattern

## Command

```bash
grep -i 'password|secret|key' $_FILE
```

## Description

This command searches files or directories for patterns indicating passwords or secrets, such as in AD dump outputs. The -i flag makes it case-insensitive.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Case-insensitive search | Built-in |
| 'password|secret|key' | Regex pattern for keywords | Yes |
| $_FILE | Target file or directory (use -r for recursive) | Yes |

## Examples

### Basic Usage

```bash
grep -i 'password' users.ldif
```

### Recursive Search

```bash
grep -r -i 'secret' ./ad_dump/
```

## Expected Output

```
User: admin description: The password is TempPass
```

## Related

- [[procedures/Enumerate-Passwords-in-AD-User-Descriptions]]
- [[commands/ldapdomaindump-authenticated-dump]]
