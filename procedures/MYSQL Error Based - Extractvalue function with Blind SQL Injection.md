---
id: b929b08c-8245-4ae0-b3b3-9ac717f160f3
name: MYSQL Error Based - Extractvalue function with Blind SQL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.502228+00:00'
updated_at: '2023-04-10T20:22:51.610775+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[MYSQL Error Based]]'
- '[[MYSQL Error Based - Extractvalue function]]'
- '[[MYSQL Injection]]'
---

# MYSQL Error Based - Extractvalue function with Blind SQL Injection

## Summary

This procedure leverages MYSQL Error Based - Extractvalue function with Blind SQL Injection to extract sensitive data from a MYSQL database. This technique is used to bypass input validation and authentication mechanisms to gain unauthorized access to sensitive data. The attacker can inject malicio

## Description

# Description

This procedure leverages MYSQL Error Based - Extractvalue function with Blind SQL Injection to extract sensitive data from a MYSQL database. This technique is used to bypass input validation and authentication mechanisms to gain unauthorized access to sensitive data. The attacker can inject malicious SQL code into the database by exploiting vulnerabilities in the application or web server. By using the Extractvalue function, the attacker can extract specific data from the database without knowing the exact location of the data. Blind SQL Injection is used to infer the presence of data based on the application's response.

 

## Requirements

1. Access to the vulnerable application or web server

1. Knowledge of MYSQL and SQL Injection techniques

 

## Defense

1. Implement input validation mechanisms to prevent SQL Injection attacks

1. Use parameterized queries to prevent SQL Injection attacks

1. Regularly update and patch the application and web server to prevent known vulnerabilities

 

## Objectives

1. Extract sensitive data from the MYSQL database

1. Bypass input validation and authentication mechanisms

1. Gain unauthorized access to sensitive data

 

# Instructions

1. mysql --version

 



**Code**: [[MySQL &gt;= 5.1]]



> This command checks the version of MySQL installed on the system and confirms whether it is compatible with the application or not. The output of the command shows the version of MySQL, which can be compared with the minimum required version to ensure compatibility.

2. The Blind SQL Injection command allows an attacker to extract sensitive information from a database by injecting malicious SQL code into a vulnerable application. The code in this command extracts information such as the database version, schema names, table names, and column names by using the 'extractvalue' function in SQL. The 'data_offset' parameter can be used to specify the offset of the data to be extracted.

 



**Code**: [[?id=1 AND extractvalue(rand(),concat(CHAR(126),ver]]



> The 'id' parameter in the URL is vulnerable to SQL injection. The injected code uses the 'extractvalue' function in SQL to extract sensitive information from the database. The 'concat' function is used to concatenate the extracted information with the tilde (~) character as a delimiter. The 'data_offset' parameter is used to specify the offset of the data to be extracted. The extracted information is then displayed in the response of the application.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[MYSQL Error Based]]
- [[MYSQL Error Based - Extractvalue function]]
- [[MYSQL Injection]]


