---
id: 289bcfd4-0013-4e70-a8ec-3120a6132649
name: PostgreSQL Time Based Table Dump
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.881111+00:00'
updated_at: '2023-04-10T20:23:16.496726+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Exfiltration Over Physical Medium|T1052 - Exfiltration Over Physical Medium]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[Identify time based]]'
- '[[PostgreSQL injection]]'
- '[[PostgreSQL Time Based]]'
- '[[Table dump time based]]'
---

# PostgreSQL Time Based Table Dump

## Summary

PostgreSQL Time Based Table Dump is a technique used to extract data from a PostgreSQL database by exploiting time-based SQL injection vulnerabilities. By using the 'Sleep Based on Table Name' command, an attacker can delay the response of the database to infer whether the injected query is success

## Description

# Description

PostgreSQL Time Based Table Dump is a technique used to extract data from a PostgreSQL database by exploiting time-based SQL injection vulnerabilities. By using the 'Sleep Based on Table Name' command, an attacker can delay the response of the database to infer whether the injected query is successful or not. This technique can be used to dump tables from the database and exfiltrate the data.

Technical Explanation: The attacker injects a query into the SQL statement that causes the database to delay the response by using the 'Sleep Based on Table Name' command. The attacker can then infer whether the query was successful or not based on the delay in the response. By using this technique, the attacker can dump tables from the database and exfiltrate the data.

Business Value: This technique can be used by attackers to steal sensitive data from a PostgreSQL database, such as personal information or intellectual property. By gaining access to this data, attackers can use it for financial gain or to obtain a competitive advantage.

 

## Requirements

1. Access to a vulnerable PostgreSQL database

1. Knowledge of SQL injection techniques

1. Access to tools for exploiting SQL injection vulnerabilities

 

## Defense

1. Implement input validation and sanitization to prevent SQL injection vulnerabilities

1. Use parameterized queries to prevent SQL injection vulnerabilities

1. Implement network segmentation to limit the scope of the attack

 

## Objectives

1. Dump tables from the PostgreSQL database

1. Exfiltrate data from the database

 

# Instructions

1. This command selects a single row from the 'information_schema.tables' table and sleeps for 5 seconds if the first character of the 'table_name' column is 'a', otherwise it sleeps for 0 seconds. The 'pg_sleep' function is used to pause the execution of the query for the specified number of seconds.

 



**Code**: [[select case when substring(table_name,1,1)='a' the]]



> The purpose of this command is to test the response time of the database when querying tables with different names. By sleeping for a longer period of time when the table name starts with 'a', we can observe if there is any difference in response time when querying tables with different names.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]
- [[Exfiltration|TA0010 - Exfiltration]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Exfiltration Over Physical Medium|T1052 - Exfiltration Over Physical Medium]]
- [[Scheduled Task|T1053 - Scheduled Task]]

## Tags

- [[Identify time based]]
- [[PostgreSQL injection]]
- [[PostgreSQL Time Based]]
- [[Table dump time based]]


