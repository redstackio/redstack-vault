---
data: >-
  INSERT INTO users (username, password) VALUES ('admin', 'admin'), ('user',
  'user'), ('noob', 'noob');
tags:
  - mysql
  - data
type: command
output: 3 rows in set
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.058Z'
id: 7f79ec3b-ae57-4f98-9df0-d90c5f24b839
verified: false
validated: true
submitted: true
---
# mysql-insert-sample-users

## Command

```sql
INSERT INTO users (username, password) VALUES ('admin', 'admin'), ('user', 'user'), ('noob', 'noob');
```

## Description

Inserts three sample user records into the 'users' table for testing SQL injection exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| INSERT INTO | Target table | Yes |
| VALUES | Data tuples | Yes |

## Examples

### Basic Usage

```sql
INSERT INTO users (username, password) VALUES ('admin', 'admin');
```

## Expected Output

Query OK, 3 rows affected.

## Related

- [[Related Procedure|procedures/Populate-Database-with-Sample-Data]]
