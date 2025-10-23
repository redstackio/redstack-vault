---
id: 50d9106f-aca6-4569-825a-49af3acf9577
name: SQL Injection WAF Bypass using OFFSET, FROM and JOIN
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.713845+00:00'
updated_at: '2023-04-10T20:24:19.936864+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[No Comma]]'
- '[[SQL Injection]]'
- '[[WAF Bypass]]'
commands:
- '[[Combine SELECT statements with UNION]]'
- '[[Modify LIMIT clause]]'
- '[[Modify SUBSTR function]]'
---

# SQL Injection WAF Bypass using OFFSET, FROM and JOIN

## Summary

SQL Injection is a type of attack where an attacker injects malicious SQL code into a vulnerable application. This particular procedure involves using OFFSET, FROM, and JOIN to bypass a Web Application Firewall (WAF). This technique is used to evade detection and execute malicious SQL queries that 

## Description

# Description

SQL Injection is a type of attack where an attacker injects malicious SQL code into a vulnerable application. This particular procedure involves using OFFSET, FROM, and JOIN to bypass a Web Application Firewall (WAF). This technique is used to evade detection and execute malicious SQL queries that can lead to data exfiltration, privilege escalation, or complete system compromise.

The technical explanation for this technique involves manipulating the SQL query to bypass the WAF. By using the OFFSET and FROM clauses, an attacker can bypass the WAF's signature-based detection by adding additional characters to the query. The JOIN clause is used to join two tables together, which can be used to extract sensitive data from the database.

The business value of this procedure is that it allows an attacker to gain unauthorized access to sensitive data, which can be used for financial gain or corporate espionage.

 

## Requirements

1. Access to a vulnerable application

1. Knowledge of SQL Injection techniques

1. Knowledge of the vulnerable application's database schema

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL Injection attacks

1. Use a modern WAF that is capable of detecting and blocking SQL Injection attacks

1. Regularly monitor and analyze application logs for suspicious activity

 

## Objectives

1. Bypass a Web Application Firewall using SQL Injection

1. Extract sensitive data from a database

 

# Instructions

1. To bypass using OFFSET, FROM, and JOIN, you can use the following commands:
1. LIMIT 1 OFFSET 0 instead of LIMIT 0,1
2. SUBSTR('SQL' FROM 1 FOR 1) instead of SUBSTR('SQL',1,1)
3. UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c JOIN (SELECT 4)d instead of SELECT 1,2,3,4


 



**Code**: [[LIMIT 0,1         -> LIMIT 1 OFFSET 0
SUBSTR('SQL']]



> The LIMIT command is used to limit the number of results returned in a SQL query. By using LIMIT 1 OFFSET 0, we can bypass using OFFSET and achieve the same result. The SUBSTR command is used to extract a substring from a string. By using SUBSTR('SQL' FROM 1 FOR 1), we can bypass using the comma and achieve the same result. The UNION command is used to combine the results of two or more SELECT statements. By using UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c JOIN (SELECT 4)d, we can bypass using FROM and JOIN and achieve the same result.



**Command** ([[Modify LIMIT clause]]):

```bash
LIMIT 0,1
```





**Command** ([[Modify SUBSTR function]]):

```bash
SUBSTR('SQL',1,1)
```





**Command** ([[Combine SELECT statements with UNION]]):

```bash
SELECT 1,2,3,4
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Combine SELECT statements with UNION]]
- [[Modify LIMIT clause]]
- [[Modify SUBSTR function]]

## Tags

- [[No Comma]]
- [[SQL Injection]]
- [[WAF Bypass]]


