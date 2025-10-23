---
id: a9a8733b-9eea-4153-92c2-bde94f066a9c
name: MSSQL Database Name Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.614996+00:00'
updated_at: '2023-04-10T20:22:40.928529+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[MSSQL Database name]]'
- '[[MSSQL Injection]]'
commands:
- '[[Get current database name]]'
---

# MSSQL Database Name Enumeration

## Summary

MSSQL Database Name Enumeration is an attack technique used by adversaries to identify the name of a MSSQL database. This technique is commonly used in the reconnaissance phase of an attack. Attackers can use this information to better understand the target environment and plan future attacks. To e

## Description

# Description

MSSQL Database Name Enumeration is an attack technique used by adversaries to identify the name of a MSSQL database. This technique is commonly used in the reconnaissance phase of an attack. Attackers can use this information to better understand the target environment and plan future attacks. To execute this technique, attackers use MSSQL Injection to inject malicious SQL statements into a vulnerable application. The malicious SQL statements are designed to extract the name of the database from the target system. 

Technical Explanation: MSSQL Injection is a type of injection attack that exploits vulnerabilities in an application's SQL statements. Attackers can use this technique to execute malicious SQL statements that can extract sensitive information from a target system. In this case, attackers use MSSQL Injection to extract the name of the database from the target system. 

Business Value: MSSQL Database Name Enumeration can help attackers better understand the target environment and plan future attacks. By identifying the name of a database, attackers can launch targeted attacks against specific systems.

 

## Requirements

1. Access to a vulnerable application

1. Knowledge of SQL Injection techniques

 

## Defense

1. Implement input validation on all user input fields in applications to prevent SQL Injection attacks

1. Use parameterized queries to prevent SQL Injection attacks

1. Monitor network traffic for suspicious SQL statements

 

## Objectives

1. Identify the name of the MSSQL database

1. Gather information about the target environment

 

# Instructions

1. This command retrieves the name of the current database being used.

 



**Code**: [[SELECT DB_NAME()]]



> The SELECT DB_NAME() command is used to retrieve the name of the current database being used. This is useful when working with multiple databases or when needing to know the name of the current database for administrative purposes. There are no arguments required for this command.



**Command** ([[Get current database name]]):

```bash
SELECT DB_NAME()
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get current database name]]

## Tags

- [[MSSQL Database name]]
- [[MSSQL Injection]]


