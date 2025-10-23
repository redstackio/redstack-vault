---
id: 651db1ab-db19-41ce-9fc4-6e35d030b957
name: SQL Injection WAF Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.742998+00:00'
updated_at: '2023-04-10T20:24:17.351454+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Resource Hijacking|T1496 - Resource Hijacking]]'
tags:
- '[[No Equal]]'
- '[[SQL Injection]]'
- '[[WAF Bypass]]'
---

# SQL Injection WAF Bypass

## Summary

SQL Injection is a type of attack where an attacker injects malicious SQL code into a vulnerable application's database. A WAF (Web Application Firewall) is a security solution that is designed to protect web applications from attacks. However, attackers can bypass WAFs by using various techniques.

## Description

# Description

SQL Injection is a type of attack where an attacker injects malicious SQL code into a vulnerable application's database. A WAF (Web Application Firewall) is a security solution that is designed to protect web applications from attacks. However, attackers can bypass WAFs by using various techniques. One such technique is SQL Version Bypass, which involves exploiting a vulnerability in the WAF that allows attackers to inject SQL code that is specific to a particular database version, and thus bypass the WAF's protections. This technique can be used to steal sensitive data, modify or delete data, or take control of the entire application.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL Injection techniques

1. Knowledge of the target database version

 

## Defense

1. Implement a WAF with up-to-date rules and configurations

1. Regularly test and update the WAF to ensure it is effective against the latest threats

1. Use parameterized queries and input validation to prevent SQL Injection attacks

 

## Objectives

1. Bypass the WAF to perform SQL Injection attacks

1. Gain unauthorized access to sensitive data

1. Modify or delete data

1. Take control of the vulnerable application

 

# Instructions

1. This command is used to bypass SQL version restrictions by using different SQL commands such as LIKE, NOT IN, IN, and BETWEEN. The commands can be used to extract data that may not be accessible with the current version of SQL.

 



**Code**: [[?id=1 and substring(version(),1,1)like(5)
?id=1 an]]



> The commands in the 'data' field can be used to extract data from a SQL database. The first command uses the LIKE command to extract data where the first digit of the version number is 5. The second command uses the NOT IN command to extract data where the first digit is not 4 or 3. The third command uses the IN command to extract data where the first digit is either 4 or 3. The fourth command uses the BETWEEN command to extract data where the first digit is between 3 and 4. By using these commands, it is possible to bypass version restrictions and extract data that may not be accessible with the current version of SQL.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Resource Hijacking|T1496 - Resource Hijacking]]

## Tags

- [[No Equal]]
- [[SQL Injection]]
- [[WAF Bypass]]


