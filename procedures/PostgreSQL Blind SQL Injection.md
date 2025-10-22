---
id: 454d3b97-762a-4df7-967e-75b9b20ceaef
name: PostgreSQL Blind SQL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.812258+00:00'
updated_at: '2023-04-10T20:23:18.696613+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[PostgreSQL Blind]]'
- '[[PostgreSQL injection]]'
---

# PostgreSQL Blind SQL Injection

## Summary

PostgreSQL Blind SQL Injection is a technique used by attackers to exploit web applications that use PostgreSQL databases. This technique allows an attacker to execute arbitrary SQL queries on the database, without actually seeing the results of the query. This type of attack is particularly danger

## Description

# Description

PostgreSQL Blind SQL Injection is a technique used by attackers to exploit web applications that use PostgreSQL databases. This technique allows an attacker to execute arbitrary SQL queries on the database, without actually seeing the results of the query. This type of attack is particularly dangerous because it can be difficult to detect and can result in the theft of sensitive data.

To perform a blind SQL injection, the attacker must first identify a vulnerable parameter in the web application. Once a vulnerable parameter has been identified, the attacker can use SQL injection techniques to inject malicious SQL code into the parameter. This code can then be used to execute arbitrary SQL queries on the database.

The business value of this attack is that it allows an attacker to gain unauthorized access to sensitive data, which can be used for financial gain or to damage the reputation of the targeted organization.

## Requirements

1. Access to the web application that uses a PostgreSQL database

## Defense

1. Use parameterized SQL queries to prevent SQL injection attacks

1. Regularly monitor and log database activity to detect suspicious behavior

1. Implement web application firewalls to detect and block SQL injection attacks

## Objectives

1. Gain unauthorized access to sensitive data stored in a PostgreSQL database

# Instructions

1. To use this command, simply copy and paste the provided query into a PostgreSQL command prompt or SQL injection tool.

**Code**: [[' and substr(version(),1,10) = 'PostgreSQL' and '1]]

> The command uses the 'version()' function to retrieve the version of the target PostgreSQL installation. It then compares the first 10 characters of the version string to 'PostgreSQL'. If the comparison is true, the command returns '1  -> OK
', indicating that the target system is running PostgreSQL. If the comparison is false, the command returns '1  -> KO', indicating that the target system is not running PostgreSQL.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[PostgreSQL Blind]]
- [[PostgreSQL injection]]
