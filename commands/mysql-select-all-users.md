---
data: select * from users;
tags:
  - mysql
  - query
type: command
output: >-
  +----------+----------+ | username | password | +----------+----------+ |
  admin | admin | | user | user | | noob | noob | +----------+----------+ 3 rows
  in set (0.00 sec)
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.056Z'
id: 3353ff49-d8aa-49d6-8fa1-377267fb43c1
verified: false
validated: true
submitted: true
---
# mysql-select-all-users

## Command

```sql
select * from users;
```

## Description

Retrieves all records from the 'users' table to verify data population or simulate exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| select * | All columns | Yes |
| from users | Target table | Yes |

## Examples

### Basic Usage

```sql
select * from users;
```

## Expected Output

Table with username/password rows for admin, user, noob.

## Related

- [[Related Procedure|procedures/Populate-Database-with-Sample-Data]]
