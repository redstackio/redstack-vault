---
data: >-
  curl -s
  "https://www.khanacademy.org/translations/videos/en'_youtube_stats.csv"
tags:
  - sqli
  - test
  - web
type: command
output: HTTP 500 Internal Server Error or error page indicating database syntax issue
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 26c83860-a436-4a30-993e-e3f2097a14f6
created_at: '2025-12-14T03:46:20.263Z'
updated_at: '2025-12-14T03:46:20.263Z'
verified: false
validated: true
submitted: true
---
# curl-test-single-quote-sqli

## Command

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'_youtube_stats.csv"
```

## Description

This command tests for SQL injection by sending a GET request with a single quote in the language parameter, expecting a server error if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| URL | Target endpoint with injected quote | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://www.khanacademy.org/translations/videos/en'_youtube_stats.csv"
```

### Advanced Usage

```bash
curl -s -v "https://www.khanacademy.org/translations/videos/en'_youtube_stats.csv" > response.html
```

## Expected Output

A 500 error response or HTML error page mentioning SQL syntax error, confirming injection point.

## Related

- [[Related Procedure: Test-SQL-Injection-with-Single-Quote]]
