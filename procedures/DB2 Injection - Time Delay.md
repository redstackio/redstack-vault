---
id: 1bbe4a87-4876-4915-85de-85aff964c649
name: DB2 Injection - Time Delay
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.094963+00:00'
updated_at: '2023-04-10T20:22:03.367512+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
- '[[Port Knocking|T1205 - Port Knocking]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Time Delay]]'
---

# DB2 Injection - Time Delay

## Summary

DB2 Injection is a type of SQL Injection attack that targets IBM's DB2 database management system. Time Delay is a technique used in DB2 Injection to slow down the database's response time, making it easier for the attacker to extract sensitive information. To execute a Time Delay attack, the attac

## Description

# Description

DB2 Injection is a type of SQL Injection attack that targets IBM's DB2 database management system. Time Delay is a technique used in DB2 Injection to slow down the database's response time, making it easier for the attacker to extract sensitive information. To execute a Time Delay attack, the attacker injects a specially crafted SQL query that includes a sleep function. When the query is executed, the sleep function causes the database to pause for a specified amount of time before returning a response. This can be used to infer the success of an attack, as well as to bypass security measures that rely on timing-based defenses.

From a technical standpoint, a Time Delay attack is achieved by injecting malicious SQL code into a vulnerable application. The code is designed to exploit the application's use of DB2, allowing the attacker to execute arbitrary SQL commands on the database. By using a sleep function, the attacker can cause the database to delay its response, which can be used to infer the success of the attack.

The business value of DB2 Injection - Time Delay lies in its ability to extract sensitive information from a target organization's database. By exploiting vulnerabilities in the application layer, an attacker can gain access to sensitive data such as customer information, financial records, and intellectual property. This can result in significant financial losses, as well as reputational damage to the organization.

## Requirements

1. Access to a vulnerable application that uses DB2

1. Knowledge of SQL Injection techniques

1. Ability to inject malicious SQL code into the application

## Defense

1. Implement secure coding practices to prevent SQL Injection vulnerabilities

1. Use prepared statements and parameterized queries to protect against SQL Injection attacks

1. Implement rate limiting and other timing-based defenses to detect and prevent Time Delay attacks

## Objectives

1. Gain unauthorized access to a target organization's DB2 database

1. Extract sensitive information from the database

# Instructions

1. To prevent SQL Injection attacks, always use prepared statements with parameterized queries. Never use user input directly in SQL statements.

**Code**: [[' and (SELECT count(*) from sysibm.columns t1, sys]]

> The 'data' field contains a SQL Injection attack string that can be used to exploit vulnerabilities in the application's database. The 'text' field explains how the attack works and how it can be prevented. The 'instruction' field provides guidance on how to prevent SQL Injection attacks, and the 'explain' field provides additional information on the attack and its impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Code Signing|T1116 - Code Signing]]
- [[Non-Standard Port|T1571 - Non-Standard Port]]
- [[Port Knocking|T1205 - Port Knocking]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Time Delay]]
