---
id: 91413ba1-4433-4936-9eb7-6407e6916db5
name: Oracle SQL Database Name Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.140241+00:00'
updated_at: '2023-04-10T20:23:11.748832+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Oracle SQL database name]]'
- '[[Oracle SQL Injection]]'
commands:
- '[[Retrieve Database Name]]'
- '[[Retrieve Global Database Name]]'
- '[[Retrieve Instance Name]]'
- '[[Retrieve System Database Name]]'
---

# Oracle SQL Database Name Enumeration

## Summary

Oracle SQL Database Name Enumeration is a technique used to extract the name of the database running on an Oracle SQL server. This technique is often used as a reconnaissance step in a larger attack. The attacker can use the extracted information to research known vulnerabilities and plan subsequen

## Description

# Description

Oracle SQL Database Name Enumeration is a technique used to extract the name of the database running on an Oracle SQL server. This technique is often used as a reconnaissance step in a larger attack. The attacker can use the extracted information to research known vulnerabilities and plan subsequent attacks. 

To extract the database name, the attacker sends an SQL query that uses error-based SQL injection techniques. The attacker can then extract the database name from the error message returned by the server. 

This technique can be valuable to an attacker as it provides information about the target's infrastructure and can help them plan subsequent attacks.

 

## Requirements

1. Access to the Oracle SQL server

1. Knowledge of SQL injection techniques

 

## Defense

1. Ensure that the Oracle SQL server is properly patched and up-to-date to prevent known vulnerabilities

1. Implement secure coding practices to prevent SQL injection attacks

1. Monitor the server logs for suspicious activity, including SQL injection attempts

 

## Objectives

1. Extract the name of the Oracle SQL database running on the target server

1. Gather reconnaissance information to plan subsequent attacks

 

# Instructions

1. This command retrieves information about the database. The first query retrieves the global name of the database. The second query retrieves the name of the database. The third query retrieves the instance name of the database. The fourth query retrieves the database name using the DUAL table.

 



**Code**: [[SELECT global_name FROM global_name;
SELECT name F]]



> The 'global_name' is the globally unique name of the database. The 'name' is the name of the database. The 'instance_name' is the name of the instance that is connected to the database. The 'SYS.DATABASE_NAME' is the name of the database.



**Command** ([[Retrieve Global Database Name]]):

```bash
SELECT global_name FROM global_name;
```





**Command** ([[Retrieve Database Name]]):

```bash
SELECT name FROM V$DATABASE;
```





**Command** ([[Retrieve Instance Name]]):

```bash
SELECT instance_name FROM V$INSTANCE;
```





**Command** ([[Retrieve System Database Name]]):

```bash
SELECT SYS.DATABASE_NAME FROM DUAL;
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Retrieve Database Name]]
- [[Retrieve Global Database Name]]
- [[Retrieve Instance Name]]
- [[Retrieve System Database Name]]

## Tags

- [[Oracle SQL database name]]
- [[Oracle SQL Injection]]


