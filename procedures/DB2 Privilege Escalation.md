---
id: 576ef785-2ab8-4a3f-8693-34b073c1dac9
name: DB2 Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.661596+00:00'
updated_at: '2023-04-10T20:22:04.091905+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Trusted Relationship|T1199 - Trusted Relationship]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[List Privileges]]'
commands:
- '[[List DB2 system privileges]]'
- '[[Show privileges for current user]]'
- '[[Show privileges for current user on database]]'
- '[[Show privileges on tables]]'
---

# DB2 Privilege Escalation

## Summary

DB2 Privilege Escalation is a technique used to elevate the privileges of a user in a DB2 database. This technique is used by attackers to gain access to sensitive data or perform unauthorized actions. By exploiting the trust relationship between users and the database, attackers can gain access to

## Description

# Description

DB2 Privilege Escalation is a technique used to elevate the privileges of a user in a DB2 database. This technique is used by attackers to gain access to sensitive data or perform unauthorized actions. By exploiting the trust relationship between users and the database, attackers can gain access to higher privileges than they are authorized for. This technique involves injecting malicious code into the database and executing it to gain access to higher privileges. This technique can be used to gain access to sensitive data or perform unauthorized actions.

## Requirements

1. Access to the DB2 database

1. Knowledge of SQL injection

1. Knowledge of DB2 database structure

## Defense

1. Implement secure coding practices to prevent SQL injection attacks

1. Limit the privileges of database users to only what is necessary for their job function

1. Monitor database activity for suspicious behavior

## Objectives

1. Gain access to sensitive data

1. Perform unauthorized actions

# Instructions

1. To view the privileges on tables for a particular user, use the following command: 

select * from syscat.tabauth where grantee = 'username'; 

To view the privileges for the current user, use the following command: 

select * from syscat.tabauth where grantee = current user; 

To view the privileges on the database for a particular user, use the following command: 

select * from syscat.dbauth where grantee = 'username';

To view the system privileges for a user, use the following command:

select * from SYSIBM.SYSUSERAUTH where grantee = 'username';

**Code**: [[select * from syscat.tabauth -- shows priv on tabl]]

> This command is used to view the user and table privileges in a DB2 database. It can be used to check which users have access to which tables and what kind of access they have. The 'select * from syscat.tabauth' command shows the privileges on tables, while 'select * from syscat.dbauth' shows the privileges on the database. The 'select * from SYSIBM.SYSUSERAUTH' command shows the system privileges for a user.

**Command** ([[Show privileges on tables]]):

```bash
select * from syscat.tabauth
```

**Command** ([[Show privileges for current user]]):

```bash
select * from syscat.tabauth where grantee = current user
```

**Command** ([[Show privileges for current user on database]]):

```bash
select * from syscat.dbauth where grantee = current user
```

**Command** ([[List DB2 system privileges]]):

```bash
select * from SYSIBM.SYSUSERAUTH
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Trusted Relationship|T1199 - Trusted Relationship]]

## Commands Used

- [[List DB2 system privileges]]
- [[Show privileges for current user]]
- [[Show privileges for current user on database]]
- [[Show privileges on tables]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[List Privileges]]
