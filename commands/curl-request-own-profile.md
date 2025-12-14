---
data: >-
  curl -X GET "https://wakatime.com/api/v1/users/attacker_user" -H "Host:
  wakatime.com" -b cookies.txt
tags:
  - api
  - recon
type: command
output: JSON response with user's own profile metadata
executor: bash
platforms:
  - Web
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.064Z'
id: a0b3c151-34ac-482c-b982-565362818db2
verified: false
validated: true
submitted: true
---
# curl-request-own-profile

## Command

```bash
curl -X GET "https://wakatime.com/api/v1/users/attacker_user" -H "Host: wakatime.com" -b cookies.txt
```

## Description

This command retrieves the authenticated user's own profile data from the WakaTime API to baseline the endpoint structure and confirm session validity. Use after authentication to capture the request format for modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `https://wakatime.com/api/v1/users/attacker_user` | API endpoint with own username | Yes |
| `-H "Host: wakatime.com"` | Sets the Host header | Yes |
| `-b cookies.txt` | Loads session cookie from file | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://wakatime.com/api/v1/users/attacker_user" -H "Host: wakatime.com" -b cookies.txt
```

### Advanced Usage

```bash
curl -v -X GET "https://wakatime.com/api/v1/users/attacker_user" -H "Host: wakatime.com" -H "User-Agent: Mozilla/5.0" -b cookies.txt > own_profile.json
```

## Expected Output

HTTP/2 200 OK response with JSON body containing profile fields like {"is_email_confirmed": true, "is_email_public": false}.

## Related

- [[commands/curl-request-arbitrary-profile]]
- [[procedures/Exploit-WakaTime-API-Broken-Access-Control]]
