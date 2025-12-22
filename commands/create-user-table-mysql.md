---
data: >-
  CREATE TABLE `user` ( `id` int(11) NOT NULL, `firstName` varchar(255) NOT
  NULL, `lastName` varchar(255) NOT NULL, `age` int(11) NOT NULL ) ENGINE=InnoDB
  DEFAULT CHARSET=latin1;
tags:
  - database
  - mysql
  - setup
type: command
executor: sql
platforms:
  - Linux
  - macOS
id: 3fb53230-2588-4395-97f8-3efbb92c2c28
created_at: '2025-12-14T03:46:15.035Z'
updated_at: '2025-12-14T03:46:15.035Z'
verified: false
validated: true
submitted: true
---
# create-user-table-mysql

## Command

```sql
CREATE TABLE `user` ( `id` int(11) NOT NULL, `firstName` varchar(255) NOT NULL, `lastName` varchar(255) NOT NULL, `age` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

## Description

Creates a MySQL table named 'user' with integer id and age columns, and varchar firstName/lastName columns, using InnoDB engine for transactional support.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `` `user` `` | Table name | Yes |
| `id` | Primary key integer column | Yes |
| `firstName`, `lastName` | String columns for names | Yes |
| `age` | Integer column | Yes |
| ENGINE=InnoDB | Storage engine | Yes |
| DEFAULT CHARSET=latin1 | Character encoding | Yes |

## Examples

### Basic Usage

```sql
CREATE TABLE `user` ( `id` int(11) NOT NULL, `firstName` varchar(255) NOT NULL, `lastName` varchar(255) NOT NULL, `age` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

## Expected Output

Query OK, 0 rows affected (0.01 sec). Table ready for inserts.

## Related

- [[Related Procedure|procedures/Setup-Test-MySQL-Database]]
