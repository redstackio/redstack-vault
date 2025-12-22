---
data: >-
  curl -X POST 'https://partner.steamgames.com/login' --data
  'username=yourusername&password=yourpassword' -c cookies.txt
tags:
  - authentication
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a679b2bb-88e4-4c21-a285-3ba28052277d
created_at: '2025-12-11T03:47:59.385Z'
updated_at: '2025-12-11T03:47:59.385Z'
verified: false
validated: true
submitted: true
---
# curl-authenticate-steam

## Command

```bash
curl -X POST 'https://partner.steamgames.com/login' --data 'username=yourusername&password=yourpassword' -c cookies.txt
```

## Description

This command authenticates to the Steam partner site by sending a POST request with credentials and saves session cookies for future use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `--data` | Sends username and password | Yes |
| `-c cookies.txt` | Saves cookies to file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://partner.steamgames.com/login' --data 'username=yourusername&password=yourpassword' -c cookies.txt
```

## Expected Output

HTTP response with session cookies stored in cookies.txt, indicating successful authentication.

## Related

- [[commands/curl-exploit-assignkeys]]
- [[procedures/Authenticate-to-Steam-Partner-Site]]
