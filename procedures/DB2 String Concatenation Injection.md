---
id: e5ccfcdf-0453-47a0-9101-2bfe263d7c74
name: DB2 String Concatenation Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.025858+00:00'
updated_at: '2023-04-10T20:22:05.151662+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[String Concat]]'
commands:
- '[[Concatenation of Strings using CONCAT function]]'
- '[[Concatenation of Strings using Double Pipe Operator]]'
---

# DB2 String Concatenation Injection

## Summary

DB2 String Concatenation Injection is a technique used by attackers to execute arbitrary SQL code in a DB2 database through a vulnerable application. The technique involves injecting specially crafted SQL code into an application's input fields that will be concatenated with other SQL statements in

## Description

# Description

DB2 String Concatenation Injection is a technique used by attackers to execute arbitrary SQL code in a DB2 database through a vulnerable application. The technique involves injecting specially crafted SQL code into an application's input fields that will be concatenated with other SQL statements in the application's code. This can lead to unauthorized access to sensitive data, modification of data, or even complete compromise of the database.

From a technical perspective, an attacker can use the CONCAT function to inject SQL code into an application. This function concatenates two or more strings into a single string. By injecting SQL code into one of the strings, the attacker can execute arbitrary SQL code in the database.

The business value of this technique for an attacker is that it can provide access to sensitive data, such as customer information, financial data, and intellectual property. This can lead to reputational damage, loss of revenue, and legal liabilities for the organization.

 

## Requirements

1. Access to a vulnerable application that uses a DB2 database

1. Knowledge of SQL syntax and the CONCAT function

 

## Defense

1. Use prepared statements or parameterized queries to prevent SQL injection attacks

1. Implement input validation and sanitization to prevent malicious input from being processed

1. Regularly patch and update the DB2 database and the application to prevent known vulnerabilities from being exploited

 

## Objectives

1. To execute arbitrary SQL code in a DB2 database

1. To gain unauthorized access to sensitive data

1. To modify data in a DB2 database

 

# Instructions

1. To concatenate strings in SQL, you can use the CONCAT function or the double pipe (||) operator. The CONCAT function takes two or more string arguments and returns a single string that is the concatenation of all the arguments. The double pipe operator is a shorthand for the CONCAT function and is used to concatenate two strings. In the example provided, the first SELECT statement uses the CONCAT function to concatenate three strings 'a', 'b', and 'c' and returns the result 'abc'. The second SELECT statement uses the double pipe operator to concatenate two strings 'a' and 'b' and returns the result 'ab'.

 



**Code**: [[select 'a' concat 'b' concat 'c' from sysibm.sysdu]]



> The CONCAT function takes two or more string arguments and returns a single string that is the concatenation of all the arguments. The double pipe (||) operator is a shorthand for the CONCAT function and is used to concatenate two strings. In the example provided, the first SELECT statement uses the CONCAT function to concatenate three strings 'a', 'b', and 'c' and returns the result 'abc'. The second SELECT statement uses the double pipe operator to concatenate two strings 'a' and 'b' and returns the result 'ab'.



**Command** ([[Concatenation of Strings using CONCAT function]]):

```bash
select 'a' concat 'b' concat 'c' from sysibm.sysdummy1
```





**Command** ([[Concatenation of Strings using Double Pipe Operator]]):

```bash
select 'a' || 'b' from sysibm.sysdummy1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]

## Commands Used

- [[Concatenation of Strings using CONCAT function]]
- [[Concatenation of Strings using Double Pipe Operator]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[String Concat]]


