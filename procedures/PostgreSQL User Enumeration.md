---
id: d353fe7b-5297-454d-afa9-923ea83ebc86
name: PostgreSQL User Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.493931+00:00'
updated_at: '2023-04-10T20:23:19.928737+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL List Users]]'
commands:
- '[[Retrieve List of Users]]'
---

# PostgreSQL User Enumeration

## Summary

PostgreSQL User Enumeration is a technique used by attackers to identify valid usernames within a PostgreSQL database. This technique is typically used in conjunction with other attacks, such as password spraying or brute force attacks. Attackers can use the information gathered to craft more targe

## Description

# Description

PostgreSQL User Enumeration is a technique used by attackers to identify valid usernames within a PostgreSQL database. This technique is typically used in conjunction with other attacks, such as password spraying or brute force attacks. Attackers can use the information gathered to craft more targeted attacks against the identified users, or to gain access to sensitive data. To perform this attack, the attacker must first gain access to the PostgreSQL database through an injection vulnerability. Once access is gained, the attacker can use the 'List PostgreSQL Users' command to enumerate the valid usernames within the database.

 

## Requirements

1. Access to a PostgreSQL database through an injection vulnerability

1. Access to a tool capable of executing the 'List PostgreSQL Users' command

 

## Defense

1. Regularly perform vulnerability scans and penetration testing to identify and remediate injection vulnerabilities

1. Implement least privilege access controls to limit the impact of a successful attack

1. Monitor database logs for suspicious activity, such as repeated failed login attempts

 

## Objectives

1. Identify valid usernames within a PostgreSQL database

1. Craft more targeted attacks against identified users

1. Gain access to sensitive data

 

# Instructions

1. This command lists all the users in the PostgreSQL database.

 



**Code**: [[SELECT usename FROM pg_user]]



> The 'SELECT usename' part of the command selects the 'usename' column from the 'pg_user' table, which contains the names of all the users in the database. Running this command will return a list of all the usernames in the database.



**Command** ([[Retrieve List of Users]]):

```bash
SELECT usename FROM pg_user
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Retrieve List of Users]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL List Users]]


