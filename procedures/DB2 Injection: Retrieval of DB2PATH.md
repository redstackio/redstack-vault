---
id: 4dae1d77-de7f-4b61-b134-0b14117f96b4
name: 'DB2 Injection: Retrieval of DB2PATH'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.179761+00:00'
updated_at: '2023-04-10T20:21:58.312192+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Location of DB Files]]'
---

# DB2 Injection: Retrieval of DB2PATH

## Summary

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. By injecting malicious code into SQL statements, attackers can gain unauthorized access to sensitive data stored in the database. In this particular procedure, the objective is to retrieve the DB2PATH, which

## Description

# Description

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. By injecting malicious code into SQL statements, attackers can gain unauthorized access to sensitive data stored in the database. In this particular procedure, the objective is to retrieve the DB2PATH, which is the location of the DB2 database files. This information can be used to further exploit the database and gain access to sensitive data. 

Technical Explanation: 
DB2PATH is an environment variable that specifies the location of the DB2 database files. Attackers can use SQL injection techniques to retrieve this information and use it to gain unauthorized access to the database. 

Business Value: 
By gaining access to sensitive data stored in the database, attackers can steal confidential information, such as customer data, financial information, and intellectual property. This can lead to reputational damage, financial losses, and legal consequences.

## Requirements

1. Access to a vulnerable DB2 database

1. Knowledge of SQL injection techniques

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use secure coding practices to minimize the risk of vulnerabilities in the software

1. Monitor database activity for suspicious behavior and unauthorized access

## Objectives

1. Retrieve the DB2PATH environment variable

1. Gain unauthorized access to the DB2 database

# Instructions

1. This command retrieves the value of the DB2PATH variable from the system registry.

**Code**: [[select * from sysibmadm.reg_variables where reg_va]]

> The 'select' statement is used to retrieve data from the 'sysibmadm.reg_variables' table. The 'where' clause filters the results to only include the row where the 'reg_var_name' column is equal to 'DB2PATH'. This command requires privileges to access the system registry.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Location of DB Files]]
