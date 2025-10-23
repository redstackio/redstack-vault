---
id: daa3eeaa-67c6-49ec-87de-c9dcfff3f857
name: PostgreSQL Time Based Injection for Database Dump
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.855220+00:00'
updated_at: '2023-04-10T20:23:13.212202+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command
  and Control Channel]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Database dump time based]]'
- '[[Identify time based]]'
- '[[PostgreSQL injection]]'
- '[[PostgreSQL Time Based]]'
---

# PostgreSQL Time Based Injection for Database Dump

## Summary

PostgreSQL Time Based Injection for Database Dump is a method of injecting malicious SQL queries into a PostgreSQL database in order to extract sensitive data. This technique is used to bypass security measures and gain access to a target's database. By using the 'Database Sleep' command, an attack

## Description

# Description

PostgreSQL Time Based Injection for Database Dump is a method of injecting malicious SQL queries into a PostgreSQL database in order to extract sensitive data. This technique is used to bypass security measures and gain access to a target's database. By using the 'Database Sleep' command, an attacker can delay the response of the database, allowing them to extract data in a time-based manner. This technique can be used to dump the entire contents of a database or extract specific data, such as usernames and passwords. The business value of this technique is that it can be used to steal sensitive information from a target, which can be sold or used for further attacks.

 

## Requirements

1. Access to the target's PostgreSQL database

1. Knowledge of SQL injection techniques

1. Ability to execute the 'Database Sleep' command

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Monitor database activity for suspicious behavior

 

## Objectives

1. Extract sensitive data from a target's database

1. Dump the entire contents of a database

1. Extract specific data, such as usernames and passwords

 

# Instructions

1. This command is used to cause a delay in the database server. The argument passed to the substring function determines the condition for the delay. If the first character of the database name is '1', then the delay will be for 5 seconds, else there will be no delay. The limit clause is used to limit the result to one row.

 



**Code**: [[select case when substring(datname,1,1)='1' then p]]



> The command selects the first database from the pg_database table and checks if the first character of its name is '1'. If it is, then the command sleeps for 5 seconds, else it sleeps for 0 seconds. This command can be used for testing the performance of the database server under heavy load or to simulate a slow query.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command and Control Channel]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Database dump time based]]
- [[Identify time based]]
- [[PostgreSQL injection]]
- [[PostgreSQL Time Based]]


