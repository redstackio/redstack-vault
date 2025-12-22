---
data: >-
  INSERT INTO `user` (`id`, `firstName`, `lastName`, `age`) VALUES (1, 'Timber',
  'Saw', 25), (2, 'Timber 0', 'Saw', 25);
tags:
  - database
  - mysql
  - data-insertion
type: command
executor: sql
platforms:
  - Linux
  - macOS
id: 8d185866-6ab0-4c15-8614-540ea41a9cb6
created_at: '2025-12-14T03:46:15.034Z'
updated_at: '2025-12-14T03:46:15.034Z'
verified: false
validated: true
submitted: true
---
# insert-test-data-user-table

## Command

```sql
INSERT INTO `user` (`id`, `firstName`, `lastName`, `age`) VALUES (1, 'Timber', 'Saw', 25), (2, 'Timber 0', 'Saw', 25);
```

## Description

Inserts two sample user records into the 'user' table, providing data for normal and SQL-injected queries in the POC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `` `user` `` | Target table | Yes |
| `id` | Values 1 and 2 | Yes |
| `firstName` | 'Timber' and 'Timber 0' | Yes |
| `lastName` | 'Saw' for both | Yes |
| `age` | 25 for both | Yes |

## Examples

### Basic Usage

```sql
INSERT INTO `user` (`id`, `firstName`, `lastName`, `age`) VALUES (1, 'Timber', 'Saw', 25), (2, 'Timber 0', 'Saw', 25);
```

## Expected Output

Query OK, 2 rows affected (0.00 sec). Records available for querying.

## Related

- [[Related Procedure|procedures/Setup-Test-MySQL-Database]]
