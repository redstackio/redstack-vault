---
type: command
executor: sql
data: '''i''=''i'''
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Database
tags:
  - sql-injection
  - fingerprinting
verified: true
validated: true
---

# generic-string-equality-test

## Command

```sql
'i'='i'
```

## Description

Generic string tautology for SQLi confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND 'i'='i' --`

## Expected Output

True response.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/generic-numeric-equality-test]]
