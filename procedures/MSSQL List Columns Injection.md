---
id: a9117d11-7d00-4f35-a94e-ef6e87b7b6c1
name: MSSQL List Columns Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.682834+00:00'
updated_at: '2023-04-10T20:22:44.509874+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL List columns]]'
commands:
- '[[List column names and types for ''sometable'']]'
- '[[List column names for ''mytable'']]'
- '[[List table catalog and column names]]'
---

# MSSQL List Columns Injection

## Summary

MSSQL List Columns Injection is a technique used by attackers to obtain information about columns in a database. This technique involves using SQL injection to manipulate the database into returning information about columns, such as their names and types. This technique can be used by attackers to

## Description

# Description

MSSQL List Columns Injection is a technique used by attackers to obtain information about columns in a database. This technique involves using SQL injection to manipulate the database into returning information about columns, such as their names and types. This technique can be used by attackers to gain a better understanding of the structure of a database and to plan subsequent attacks.

From a technical perspective, attackers can use SQL injection to inject malicious code into a vulnerable web application, which is then executed by the underlying database. This allows the attacker to extract information from the database that they would not normally have access to. From a business perspective, this technique can be used to steal sensitive data, such as customer information, which can then be sold on the black market or used for other malicious purposes.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL injection techniques

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Regularly update and patch web applications and underlying databases to address known vulnerabilities

## Objectives

1. To obtain information about columns in a database

1. To gain a better understanding of the structure of a database

1. To plan subsequent attacks

# Instructions

1. To list the column names and types of a table, execute one of the following SQL commands:

1. For the current database:
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'mytable');

2. For a specified table:
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='sometable';

3. Using information_schema:
SELECT table_catalog, column_name FROM information_schema.columns

**Code**: [[SELECT name FROM syscolumns WHERE id = (SELECT id ]]

> The first command will list the column names of a specified table in the current database. The second command will list the column names and types of a specified table in the master database. The third command will list the column names and their respective database names for all tables in the current database.

**Command** ([[List column names for 'mytable']]):

```bash
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'mytable'); -- for the current DB only
```

**Command** ([[List column names and types for 'sometable']]):

```bash
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='sometable'; -- list column names and types for master..sometable
```

**Command** ([[List table catalog and column names]]):

```bash
SELECT table_catalog, column_name FROM information_schema.columns
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[List column names and types for 'sometable']]
- [[List column names for 'mytable']]
- [[List table catalog and column names]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL List columns]]
