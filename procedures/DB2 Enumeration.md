---
id: b716ba85-9ebb-4f79-86f5-d7b70485a756
name: DB2 Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.753406+00:00'
updated_at: '2023-04-10T20:21:59.771710+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[List Databases]]'
commands:
- '[[Select distinct table_catalog from sysibm.tables]]'
- '[[SELECT schemaname FROM syscat.schemata]]'
---

# DB2 Enumeration

## Summary

DB2 Enumeration is a technique used to identify and list all available databases and schemas within a DB2 instance. This technique is commonly used by attackers to gain an understanding of the target system's data architecture, which can be used to plan further attacks. DB2 Enumeration can be achie

## Description

# Description

DB2 Enumeration is a technique used to identify and list all available databases and schemas within a DB2 instance. This technique is commonly used by attackers to gain an understanding of the target system's data architecture, which can be used to plan further attacks. DB2 Enumeration can be achieved through various methods, including SQL injection attacks or by using authorized credentials to query the database.

From a technical perspective, DB2 Enumeration involves sending specially crafted SQL queries to the DB2 instance in order to retrieve information about the available databases and schemas. This information can then be used to identify potential targets for further exploitation.

The business value of DB2 Enumeration lies in its ability to provide attackers with valuable information about the target system's data architecture. This information can be used to plan further attacks or to gain access to sensitive data.

## Requirements

1. Access to the DB2 instance

1. Knowledge of SQL queries

## Defense

1. Implement input validation and parameterized queries to prevent SQL injection attacks

1. Limit access to the DB2 instance to authorized personnel only

1. Monitor the database for suspicious activity

## Objectives

1. Identify all available databases and schemas within a DB2 instance

1. Gain an understanding of the target system's data architecture

1. Plan further attacks or gain access to sensitive data

# Instructions

1. This command will list the names of all available databases and schemas in the current environment.

**Code**: [[select distinct(table_catalog) from sysibm.tables
]]

> The first query 'select distinct(table_catalog) from sysibm.tables' will list the names of all available databases in the current environment. The second query 'SELECT schemaname FROM syscat.schemata;' will list the names of all available schemas in the current environment.

**Command** ([[Select distinct table_catalog from sysibm.tables]]):

```bash
select distinct(table_catalog) from sysibm.tables
```

**Command** ([[SELECT schemaname FROM syscat.schemata]]):

```bash
SELECT schemaname FROM syscat.schemata
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Select distinct table_catalog from sysibm.tables]]
- [[SELECT schemaname FROM syscat.schemata]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[List Databases]]
