---
id: e4708209-c91a-4531-b6e9-d5f049588e0a
name: sql-len-subquery-length
type: command
executor: sql
data: SELECT LEN((SELECT(1)))
output: null
created_at: '2023-04-06T03:56:33.402081+00:00'
updated_at: '2023-04-10T20:22:25.418354+00:00'
platforms:
  - SQL Server
tags:
  - sql-injection
  - hql
verified: true
validated: true
---

# sql-len-subquery-length

## Command

```sql
SELECT LEN((SELECT(1)))
```

## Description

This SQL command calculates the length of the result from a simple subquery, useful for testing injection points in HQL applications by confirming nested query execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| LEN() | Built-in function to get string length | Yes |
| (SELECT(1)) | Subquery returning a constant value | Yes |

## Examples

### Basic Usage

```sql
SELECT LEN((SELECT(1)))
```

### Advanced Usage

```sql
SELECT LEN((SELECT TOP 1 name FROM users WHERE id=1))
```

## Expected Output

A single integer value representing the length, e.g., `1` for the basic subquery result.

## Related

- [[procedures/Hibernate-Query-Language-Injection-Using-Unicode]]
