---
id: proc-002
tags:
  - sqli
  - mysql
  - database-setup
type: procedure
tools:
  - '[[tools/MySQL-Command-Line-Client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/mysql-drop-create-users-table]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Server Software Component]]'
updated_at: '2025-12-14T03:46:15.094Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Server Software Component]]'
---
# Setup-Test-MySQL-Database-and-Table

## Summary

This procedure creates a test MySQL database named 'test' and a 'users' table with username and password columns, simulating a vulnerable application's data store for SQL injection testing.

## Description

Using the MySQL CLI, drop any existing 'users' table and recreate it with UTF-8 charset and InnoDB engine. This sets up the target for the query-mysql module's fetchById function, where injection occurs at line 172 in lib/base.js via concatenation: "SELECT * FROM " + table + " WHERE " + name_id + "='" + id + "'".

## Requirements

1. MySQL 5.7.13 server running on localhost:3306
2. Root access with password 'root'
3. 'test' database exists (create if not: CREATE DATABASE test;)

## Defense

Defensive measures and detection strategies:

- Use prepared statements or ORMs like Sequelize
- Enable MySQL query logging to detect anomalous DDL
- Restrict database user privileges to least required

## Objectives

1. Clean slate by dropping existing table
2. Create schema for user data storage
3. Ensure compatibility with Node.js module queries

## Instructions

### Step 1: Connect to MySQL

**Context**: Access the database server.

**Command** ([[commands/mysql-login]]):
```bash
mysql -u root -p
```

> Enter password 'root'; expected output: mysql> prompt.

### Step 2: Create Table

**Context**: Drop and recreate 'users' table.

**Command** ([[commands/mysql-drop-create-users-table]]):
```sql
DROP TABLE IF EXISTS `users`; /*!40101 SET @saved_cs_client = @@character_set_client */; /*!40101 SET character_set_client = utf8 */; CREATE TABLE `users` ( `username` varchar(50) DEFAULT NULL, `password` varchar(50) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

> Executes in MySQL session; expected output: Query OK for create.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Server Software Component]] Server Software Component: Database Services

### Sub-Techniques


## Commands Used

- [[commands/mysql-drop-create-users-table]]

## Tools Used

- [[tools/MySQL-Command-Line-Client]]

## Tags

- sqli
- mysql
- database-setup
