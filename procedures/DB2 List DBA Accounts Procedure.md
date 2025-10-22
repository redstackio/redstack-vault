---
id: c81c8d10-d4ab-4d06-82a0-cc6a8a9e1351
name: DB2 List DBA Accounts Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.695800+00:00'
updated_at: '2023-04-10T20:22:02.639861+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[List DBA Accounts]]'
commands:
- '[[List of users with CONTROLAUTH]]'
- '[[List of users with SYSADMAUTH]]'
---

# DB2 List DBA Accounts Procedure

## Summary

This procedure aims to list DBA accounts in a DB2 database by exploiting a vulnerability in the application that allows for DB2 injection. An attacker can use this procedure to gain access to sensitive information stored in the database, including usernames and passwords. To execute this procedure,

## Description

# Description

This procedure aims to list DBA accounts in a DB2 database by exploiting a vulnerability in the application that allows for DB2 injection. An attacker can use this procedure to gain access to sensitive information stored in the database, including usernames and passwords. To execute this procedure, the attacker needs to have access to the application and be able to inject malicious code into the SQL queries sent to the database. The business value of this procedure is that it allows the attacker to gain access to valuable information that can be used for further attacks or sold on the black market.

## Requirements

1. Access to the vulnerable application

1. Ability to inject malicious code into SQL queries

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Enforce the principle of least privilege to limit access to sensitive information

1. Monitor database activity for suspicious behavior

## Objectives

1. List all DBA accounts in the DB2 database

1. Gain access to sensitive information stored in the database

# Instructions

1. To list all users with control authority over a table, run the following SQL command:
select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'

To list all users with SYSADM authority, run the following SQL command:
select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = ‘Y’ or SYSADMAUTH = ‘G’

**Code**: [[select distinct(grantee) from sysibm.systabauth wh]]

> The first SQL command lists all users who have control authority over at least one table in the database. The second SQL command lists all users who have SYSADM authority, which grants full administrative access to the database. The 'distinct' keyword in the first command ensures that each user is only listed once, even if they have control authority over multiple tables.

**Command** ([[List of users with CONTROLAUTH]]):

```bash
select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'
```

**Command** ([[List of users with SYSADMAUTH]]):

```bash
select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = ‘Y’ or SYSADMAUTH = ‘G’
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[List of users with CONTROLAUTH]]
- [[List of users with SYSADMAUTH]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[List DBA Accounts]]
