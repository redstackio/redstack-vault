---
data: >-
  DROP TABLE IF EXISTS `users`; /*!40101 SET @saved_cs_client =
  @@character_set_client */; /*!40101 SET character_set_client = utf8 */; CREATE
  TABLE `users` ( `username` varchar(50) DEFAULT NULL, `password` varchar(50)
  DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
tags:
  - mysql
  - setup
type: command
output: Table created successfully
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.072Z'
id: e4e33912-2a62-47a2-9ea5-f09c392bd770
verified: false
validated: true
submitted: true
---
# mysql-drop-create-users-table

## Command

```sql
DROP TABLE IF EXISTS `users`; /*!40101 SET @saved_cs_client = @@character_set_client */; /*!40101 SET character_set_client = utf8 */; CREATE TABLE `users` ( `username` varchar(50) DEFAULT NULL, `password` varchar(50) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## Description

Drops existing 'users' table if present and creates a new one with varchar columns for username and password, using InnoDB and UTF-8 for compatibility with Node.js queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| DROP TABLE | Removes old table | Yes |
| CREATE TABLE | Defines schema | Yes |

## Examples

### Basic Usage

```sql
DROP TABLE IF EXISTS `users`; CREATE TABLE `users` ( `username` varchar(50) DEFAULT NULL, `password` varchar(50) DEFAULT NULL ) ENGINE=InnoDB;
```

## Expected Output

Query OK, 0 rows affected; Table 'users' created.

## Related

- [[Related Procedure|procedures/Setup-Test-MySQL-Database-and-Table]]
