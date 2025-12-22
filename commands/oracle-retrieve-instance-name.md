---
type: command
executor: sql
data: SELECT instance_name FROM V$INSTANCE;
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Oracle Database
tags:
  - oracle-sql
  - discovery
verified: true
validated: true
---

# oracle-retrieve-instance-name

## Command

```sql
SELECT instance_name FROM V$INSTANCE;
```

## Description

This SQL command queries the V$INSTANCE view to obtain the name of the current Oracle database instance, crucial for environments with multiple instances or RAC configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; assumes SELECT privilege on V$INSTANCE. | N/A |

## Examples

### Basic Usage

```sql
SELECT instance_name FROM V$INSTANCE;
```

### Error-Based Injection

Force an error to leak the instance name, e.g., by dividing by zero in a subquery involving V$INSTANCE.

## Expected Output

A single row with the instance name, e.g.:

INSTANCE_NAME
-------------
ORCL1

## Related

- [[procedures/Oracle-SQL-Database-Name-Enumeration]]
- [[commands/oracle-retrieve-database-name]]
