---
id: cmd-base64-encode-query
data: echo -n 'SQL_QUERY_HERE' | base64 -w 0
tags:
  - encoding
  - sqli
type: command
output: Base64 encoded string without line wraps
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.208Z'
verified: false
validated: true
submitted: true
---
# base64-encode-query

## Command

```bash
echo -n 'SQL_QUERY_HERE' | base64 -w 0
```

## Description

Encodes a SQL query string into Base64 format without line wraps, useful for injecting into URL parameters like ExpressionEngine's `thequery` to bypass direct SQL input restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `SQL_QUERY_HERE` | The plain SQL string to encode (e.g., 'SELECT * FROM exp_members') | Yes |
| `-n` | Suppress trailing newline | Yes |
| `-w 0` | Disable line wrapping | Yes |

## Examples

### Basic Usage

```bash
echo -n 'SELECT * FROM exp_members' | base64 -w 0
```

### Advanced Usage

```bash
echo -n 'SELECT <svg onload=alert(1)>' | base64 -w 0
```

## Expected Output

A single line Base64 string, e.g., `c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw==` for the basic query.

## Related

- [[commands/curl-send-query]]
