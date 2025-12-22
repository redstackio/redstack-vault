---
id: cmd-curl-discover-endpoint-001
data: >-
  curl -X GET https://target-weblate.com/api/user/keys/ -H "Authorization: Token
  YOUR_API_TOKEN" -v
tags:
  - recon
  - api
type: command
output: |-
  HTTP/1.1 200 OK
  {"keys": [...]}
  No RateLimit headers
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.095Z'
verified: false
validated: true
submitted: true
---
# curl-discover-endpoint

## Command

```bash
curl -X GET https://target-weblate.com/api/user/keys/ -H "Authorization: Token YOUR_API_TOKEN" -v
```

## Description

This command uses curl to GET the API keys endpoint in Weblate, discovering potential regeneration paths through verbose inspection. Use it during reconnaissance to map API features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `https://target-weblate.com/api/user/keys/` | Target endpoint URL | Yes |
| `-H "Authorization: Token YOUR_API_TOKEN"` | Auth header with API token | Yes |
| `-v` | Verbose output for headers | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://target-weblate.com/api/user/keys/ -H "Authorization: Token abc123" -v
```

### Advanced Usage

```bash
curl -X GET https://target-weblate.com/api/user/keys/ -H "Authorization: Token abc123" -v -o keys.json
```

## Expected Output

Verbose HTTP response showing 200 OK, JSON with key list, and headers without rate limits. Errors if unauthorized.

## Related

- [[Related Procedure: Locate-Weblate-API-Key-Regeneration-Endpoint]]
