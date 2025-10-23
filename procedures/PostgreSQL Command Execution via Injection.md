---
id: 0023c0bf-05fc-46c4-b1fc-4a5dcd0bad3f
name: PostgreSQL Command Execution via Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.078828+00:00'
updated_at: '2023-04-10T20:23:14.805946+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypass Filter]]'
- '[[PostgreSQL Command execution]]'
- '[[PostgreSQL injection]]'
- '[[Quotes]]'
---

# PostgreSQL Command Execution via Injection

## Summary

PostgreSQL injection is a type of SQL injection attack that targets PostgreSQL databases. Attackers can use this technique to execute arbitrary SQL commands on the database. This specific procedure focuses on PostgreSQL command execution via injection. By bypassing filters and using quotes, attacke

## Description

# Description

PostgreSQL injection is a type of SQL injection attack that targets PostgreSQL databases. Attackers can use this technique to execute arbitrary SQL commands on the database. This specific procedure focuses on PostgreSQL command execution via injection. By bypassing filters and using quotes, attackers can concatenate characters and select strings with dollar-signs to execute commands. The technical explanation involves crafting malicious SQL queries that exploit vulnerabilities in the application's input validation. The business value of this attack is that it can lead to data theft, data modification, and disruption of business operations.

 

## Requirements

1. Access to the application's input validation

1. Knowledge of the database schema and SQL syntax

1. Ability to craft malicious SQL queries

1. Access to the network or application

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Use parameterized queries to avoid concatenation of user input

1. Implement least privilege access controls to limit the impact of successful attacks

 

## Objectives

1. Execute arbitrary SQL commands on the PostgreSQL database

1. Gain unauthorized access to sensitive data

1. Modify data in the database

1. Disrupt business operations

 

# Instructions

1. This command is used to concatenate multiple characters in SQL. The CHR function is used to return a character based on the ASCII code provided as an argument. In this example, the characters 'A', 'B', and 'C' are concatenated using the '||' operator.

 



**Code**: [[SELECT CHR(65)||CHR(66)||CHR(67);]]



> The argument passed to the CHR function is an ASCII code. For example, CHR(65) will return 'A', CHR(66) will return 'B', and so on. The '||' operator is used to concatenate the characters. The resulting output of this command will be the string 'ABC'.

2. To select a string in PostgreSQL, we can use the dollar-sign notation. This allows us to use any character we desire to delimit our string value. In the provided example, we have two strings being selected, one using double dollar-signs and the other using the dollar-sign with a custom tag. The double dollar-sign notation is used to select a string that does not contain the delimiter character. In this case, we have used '$$' to select the string 'This is a string'. The second string is selected using the dollar-sign with a custom tag. In this case, we have used '$TAG$' to select the string 'This is another string$TAG$'.

 



**Code**: [[SELECT $$This is a string$$
SELECT $TAG$This is an]]



> The 'SELECT' statement is used to retrieve data from a database table. In this case, we are selecting two string values. The '$$' and '$TAG$' characters are used to delimit the string values being selected. The first string is delimited by '$$' and the second string is delimited by '$TAG$'. The selected strings are 'This is a string' and 'This is another string'.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Bypass Filter]]
- [[PostgreSQL Command execution]]
- [[PostgreSQL injection]]
- [[Quotes]]


