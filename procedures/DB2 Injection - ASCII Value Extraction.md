---
id: 7549bb35-2027-4f56-bbde-016653d17887
name: DB2 Injection - ASCII Value Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.942007+00:00'
updated_at: '2023-04-10T20:22:03.739650+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[ASCII Value]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
commands:
- '[[Select Character A]]'
---

# DB2 Injection - ASCII Value Extraction

## Summary

DB2 Injection is a type of SQL Injection attack that targets IBM DB2 database servers. In this specific procedure, we will focus on extracting ASCII values from the database using the 'Select Character from IBM Dummy Table' command. This command can be used to extract the ASCII value of any charact

## Description

# Description

DB2 Injection is a type of SQL Injection attack that targets IBM DB2 database servers. In this specific procedure, we will focus on extracting ASCII values from the database using the 'Select Character from IBM Dummy Table' command. This command can be used to extract the ASCII value of any character from the database. The ASCII values can then be used for further exploitation or enumeration of the database.

To execute this procedure, an attacker must first identify a vulnerable input field that can be used for injection. Once a vulnerable input field is identified, the attacker can inject a specially crafted SQL query that includes the 'Select Character from IBM Dummy Table' command to extract the ASCII value of a specific character. The extracted ASCII values can then be used to identify other vulnerable fields or to gather information about the database.

The business value of this procedure is that an attacker can use it to gain unauthorized access to sensitive information stored in a DB2 database.

 

## Requirements

1. Access to a vulnerable input field that can be used for injection

1. Knowledge of SQL Injection techniques

1. Knowledge of the 'Select Character from IBM Dummy Table' command

 

## Defense

1. Ensure that all input fields are properly sanitized and validated to prevent SQL Injection attacks

1. Implement least privilege access control to limit the permissions of database users

1. Regularly monitor and analyze database logs for suspicious activity

 

## Objectives

1. Extract ASCII values from a vulnerable DB2 database using the 'Select Character from IBM Dummy Table' command

1. Use the extracted ASCII values for further exploitation or enumeration of the database

 

# Instructions

1. This command selects a character from the IBM dummy table.

 



**Code**: [[Char	select chr(65) from sysibm.sysdummy1 -- retur]]



> The argument of this command is the ASCII code of the character you want to select. In this example, the argument is 65 which corresponds to the character 'A'. The command uses the chr() function to convert the ASCII code to its corresponding character and then selects it from the IBM dummy table. The IBM dummy table is a special table that only contains one row and is used to test SQL statements without affecting any real data.



**Command** ([[Select Character A]]):

```bash
select chr(65) from sysibm.sysdummy1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[Select Character A]]

## Tags

- [[ASCII Value]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]


