---
id: 6a4dc94e-a187-42e9-8dd5-25818e01b4b9
name: DB2 User Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.624480+00:00'
updated_at: '2023-04-10T20:22:05.502526+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[List Users]]'
commands:
- '[[Retrieve authorized users in DB2 instance]]'
- '[[Retrieve schema owners in DB2 instance]]'
- '[[Retrieve users with database-level privileges]]'
- '[[Retrieve users with table-level privileges]]'
---

# DB2 User Enumeration

## Summary

The DB2 User Enumeration procedure aims to list all the users and their associated authorization information in a DB2 database. This technique can be used by an attacker to gain a better understanding of the target system and its users. By identifying the users and their privileges, the attacker ca

## Description

# Description

The DB2 User Enumeration procedure aims to list all the users and their associated authorization information in a DB2 database. This technique can be used by an attacker to gain a better understanding of the target system and its users. By identifying the users and their privileges, the attacker can then plan their attack strategy accordingly. 

To accomplish this, the attacker can use the 'DB2 User and Authorization Information' command. This command retrieves a list of all users and their associated authorization information from the target DB2 database. 

From a business perspective, this procedure can help organizations identify potential vulnerabilities in their DB2 databases and take necessary steps to secure them.

## Requirements

1. Access to the DB2 database

1. Valid authentication credentials

## Defense

1. Ensure that only authorized users have access to the DB2 database

1. Implement proper authentication and authorization mechanisms to prevent unauthorized access

1. Regularly monitor and audit the DB2 database for any suspicious activity

## Objectives

1. List all users and their associated authorization information in a DB2 database

1. Identify potential vulnerabilities in the target DB2 database

# Instructions

1. To retrieve information about authorized users and their privileges in a DB2 instance, execute one or more of the following SQL commands:

**Code**: [[select distinct(authid) from sysibmadm.privileges ]]

> Each of the SQL commands provided in the 'data' field retrieves a different type of user and authorization information. Please note that some of the commands may require elevated privileges to execute. The 'instruction' field provides a brief overview of how to execute these commands, while the 'explain' field provides additional information about what each command does.

**Command** ([[Retrieve authorized users in DB2 instance]]):

```bash
select distinct(authid) from sysibmadm.privileges
```

**Command** ([[Retrieve users with database-level privileges]]):

```bash
select grantee from syscat.dbauth
```

**Command** ([[Retrieve schema owners in DB2 instance]]):

```bash
select distinct(definer) from syscat.schemata
```

**Command** ([[Retrieve users with table-level privileges]]):

```bash
select distinct(grantee) from sysibm.systabauth
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Retrieve authorized users in DB2 instance]]
- [[Retrieve schema owners in DB2 instance]]
- [[Retrieve users with database-level privileges]]
- [[Retrieve users with table-level privileges]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[List Users]]
