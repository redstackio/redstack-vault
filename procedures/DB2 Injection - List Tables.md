---
id: c4dc100b-12cb-4c4e-b57b-eb43a5d1bdd4
name: DB2 Injection - List Tables
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.810846+00:00'
updated_at: '2023-04-10T20:21:58.667068+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[List Tables]]'
commands:
- '[[Select names from sysibm.systables]]'
- '[[Select table names from sysibm.tables]]'
---

# DB2 Injection - List Tables

## Summary

DB2 Injection is a technique used to exploit vulnerabilities in IBM DB2 databases. In this specific procedure, we will be using the 'Retrieve Table Names' command to list all tables in the database. By injecting malicious SQL code into the application, an attacker can execute unauthorized commands 

## Description

# Description

DB2 Injection is a technique used to exploit vulnerabilities in IBM DB2 databases. In this specific procedure, we will be using the 'Retrieve Table Names' command to list all tables in the database. By injecting malicious SQL code into the application, an attacker can execute unauthorized commands and gain access to sensitive data. This technique can be used to exfiltrate data, escalate privileges, or perform other malicious activities. To perform this procedure, the attacker needs to have access to the application and be able to inject SQL code into it.

## Requirements

1. Access to the application

1. Ability to inject SQL code

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to avoid SQL injection vulnerabilities

1. Monitor database activity for suspicious behavior

## Objectives

1. List all tables in the DB2 database

# Instructions

1. To retrieve the names of all tables in the database, execute the following SQL commands:
1. select table_name from sysibm.tables
2. select name from sysibm.systables

**Code**: [[select table_name from sysibm.tables
select name f]]

> The 'select table_name from sysibm.tables' command retrieves the names of all tables in the current schema. The 'select name from sysibm.systables' command retrieves the names of all tables in the database. Both commands can be used to retrieve table names, but the first command is faster and more efficient as it only retrieves table names from the current schema.

**Command** ([[Select table names from sysibm.tables]]):

```bash
select table_name from sysibm.tables
```

**Command** ([[Select names from sysibm.systables]]):

```bash
select name from sysibm.systables
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Select names from sysibm.systables]]
- [[Select table names from sysibm.tables]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[List Tables]]
