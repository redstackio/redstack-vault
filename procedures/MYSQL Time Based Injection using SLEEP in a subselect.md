---
id: ffb03725-82af-4281-ba3a-c1aeb92d0314
name: MYSQL Time Based Injection using SLEEP in a subselect
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.694624+00:00'
updated_at: '2023-04-10T20:22:56.223223+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[System Service Discovery|T1007 - System Service Discovery]]'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL Time Based]]'
- '[[Using SLEEP in a subselect]]'
commands:
- '[[SQL Injection Attack]]'
---

# MYSQL Time Based Injection using SLEEP in a subselect

## Summary

A MYSQL Time Based Injection attack using SLEEP in a subselect is a technique used by attackers to gain unauthorized access to a victim's database by exploiting vulnerabilities in the MYSQL database management system. The attacker uses a specially crafted SQL injection attack to inject malicious co

## Description

# Description

A MYSQL Time Based Injection attack using SLEEP in a subselect is a technique used by attackers to gain unauthorized access to a victim's database by exploiting vulnerabilities in the MYSQL database management system. The attacker uses a specially crafted SQL injection attack to inject malicious code into the victim's database. Once the attacker has gained access to the database, they can steal sensitive data or modify data to achieve their objectives.

Technical Explanation: The attacker sends a specially crafted SQL query to the victim's database that contains a subselect statement with a SLEEP function. The SLEEP function causes the database to pause execution for a specified amount of time, allowing the attacker to determine if the injection was successful. If the injection was successful, the attacker can continue to execute additional commands to achieve their objectives.

Business Value: This type of attack can cause significant damage to a victim's business by stealing sensitive data, modifying data, or disrupting business operations. It is important for organizations to implement security measures to protect their databases from SQL injection attacks.

## Requirements

1. Knowledge of MYSQL database management system

1. Access to a vulnerable MYSQL database

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Monitor database logs for suspicious activity

## Objectives

1. Gain unauthorized access to the victim's database

1. Steal sensitive data or modify data

1. Disrupt business operations

# Instructions

1. This command is used to perform SQL injection attacks on a database. The data field contains a payload that is injected into a vulnerable database to extract sensitive information. The payload is designed to cause the database to sleep for 10 seconds, which can be used to identify a successful injection.

**Code**: [[1 and (select sleep(10) from dual where database()]]

> The payload in the data field is designed to exploit a vulnerability in a database that allows an attacker to execute arbitrary SQL code. The payload is injected into the database through a vulnerable input field, such as a login form. The payload is designed to extract sensitive information from the database, such as usernames and passwords. The payload is constructed using the 'like' operator, which allows the attacker to search for data that matches a specific pattern. The payload is designed to cause the database to sleep for 10 seconds, which can be used to identify a successful injection. The instruction field should contain information on how to prevent SQL injection attacks, such as using prepared statements and input validation.

**Command** ([[SQL Injection Attack]]):

```bash
1 and (select sleep(10) from dual where database() like '%')#
1 and (select sleep(10) from dual where database() like '___')# 
1 and (select sleep(10) from dual where database() like '____')#
1 and (select sleep(10) from dual where database() like '_____')#
1 and (select sleep(10) from dual where database() like 'a____')#
...
1 and (select sleep(10) from dual where database() like 's____')#
1 and (select sleep(10) from dual where database() like 'sa___')#
...
1 and (select sleep(10) from dual where database() like 'sw___')#
1 and (select sleep(10) from dual where database() like 'swa__')#
1 and (select sleep(10) from dual where database() like 'swb__')#
1 and (select sleep(10) from dual where database() like 'swi__')#
...
1 and (select sleep(10) from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '%pass%' limit 0,1) like '%')#
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Credential Dumping|T1003 - Credential Dumping]]
- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[SQL Injection Attack]]

## Tags

- [[MYSQL Injection]]
- [[MYSQL Time Based]]
- [[Using SLEEP in a subselect]]
