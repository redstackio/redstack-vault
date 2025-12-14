---
id: cmd-curl-login
data: >-
  curl -X POST 'https://████/login.php' -d 'username=████████&password=██████'
  -c cookies.txt
tags:
  - login
  - http-post
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.817Z'
verified: false
validated: true
submitted: true
---
# curl-login-zendto

## Command

```bash
curl -X POST 'https://████/login.php' -d 'username=████████&password=██████' -c cookies.txt
```

## Description

Performs a POST login to ZendTo demo server, saving session cookies for authenticated requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d` | Data payload with credentials | Yes |
| `-c cookies.txt` | Saves cookies to file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://████/login.php' -d 'username=████████&password=██████' -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST 'https://████/login.php' -d 'username=████████&password=██████' -c cookies.txt -v
```

## Expected Output

HTTP 200 OK with session cookie in cookies.txt and redirect to dashboard.

## Related

- [[Related Procedure: Login-to-ZendTo-Demo-Server]]
