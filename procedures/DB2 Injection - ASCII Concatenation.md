---
id: 85356103-4c38-4e2c-9f46-fc9054b577a1
name: DB2 Injection - ASCII Concatenation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.071338+00:00'
updated_at: '2023-04-10T20:22:01.532995+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Avoiding Quotes]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
commands:
- '[[Concatenate ASCII values]]'
---

# DB2 Injection - ASCII Concatenation

## Summary

DB2 Injection is a technique used by attackers to inject malicious SQL statements into a DB2 database. This specific procedure, ASCII Concatenation, is used to avoid using quotes in SQL statements by concatenating ASCII values of the desired characters. This technique can be used to bypass input va

## Description

# Description

DB2 Injection is a technique used by attackers to inject malicious SQL statements into a DB2 database. This specific procedure, ASCII Concatenation, is used to avoid using quotes in SQL statements by concatenating ASCII values of the desired characters. This technique can be used to bypass input validation and gain unauthorized access to sensitive data. 

To execute this technique, the attacker will first identify a vulnerable input field in the target application. They will then use the Concatenation of ASCII values command to craft a malicious SQL statement that will be executed by the DB2 database. Successful exploitation of this technique can result in the attacker gaining access to sensitive data, including usernames, passwords, and other confidential information. 

The business value of understanding and mitigating against DB2 Injection is crucial for organizations that use DB2 databases to store sensitive information. By implementing proper input validation and other security measures, organizations can prevent attackers from exploiting this technique and gaining unauthorized access to their data.

 

## Requirements

1. Access to a vulnerable input field in a DB2 database

 

## Defense

1. Implement proper input validation to prevent SQL injection attacks

1. Use prepared statements or parameterized queries to avoid SQL injection vulnerabilities

1. Regularly monitor and audit database activity for suspicious behavior

 

## Objectives

1. Inject malicious SQL statements into a vulnerable input field in a DB2 database

1. Bypass input validation and gain unauthorized access to sensitive data

 

# Instructions

1. The CONCATENATION operator (||) is used to concatenate two or more strings or expressions. In this command, we are concatenating the ASCII values of the characters A, D, R, and I which results in the string 'ADRI'. The SELECT statement is used to retrieve the result. This command can also be used without the SELECT statement.

 



**Code**: [[SELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sys]]



> The chr() function is used to return the character associated with the specified ASCII value. In this command, we are using the chr() function to convert the ASCII values of the characters A, D, R, and I into their corresponding characters, and then concatenating them using the CONCATENATION operator. The result is a string 'ADRI'. The sysibm.sysdummy1 table is a special one-row table that can be used to retrieve a single row of dummy data.



**Command** ([[Concatenate ASCII values]]):

```bash
SELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sysibm.sysdummy1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Concatenate ASCII values]]

## Tags

- [[Avoiding Quotes]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]


