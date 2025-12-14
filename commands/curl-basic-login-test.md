---
id: cmd-curl-login-test-001
data: >-
  curl -X POST https://www.acronis.cz/wp-login.php -d
  "log=admin&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
tags:
  - recon
  - http
type: command
output: 'Quick response time, e.g., 0.912s, with login error page.'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.888Z'
verified: false
validated: true
submitted: true
---
# curl-basic-login-test

## Command

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=admin&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Description

Sends a basic login attempt to the WordPress endpoint to verify accessibility and baseline timing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Data payload with log, pwd, submit | Yes |
| `-w "%{time_total}s"` | Outputs total response time | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=admin&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

### Advanced Usage

```bash
curl -v -X POST https://www.acronis.cz/wp-login.php -d "log=admin&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

## Expected Output

Response time printed, e.g., 0.912, followed by HTML error page for invalid login.

## Related

- [[Related Procedure: Identify WordPress Login Endpoint for SQLi]]
