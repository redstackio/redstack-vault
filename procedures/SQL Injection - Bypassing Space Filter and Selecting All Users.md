---
id: dc43f855-8755-482d-bc0b-9a60c9788959
name: SQL Injection - Bypassing Space Filter and Selecting All Users
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.676222+00:00'
updated_at: '2023-04-10T20:24:25.823352+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Security Support Provider|T1101 - Security Support Provider]]'
tags:
- '[[SQL Injection]]'
- '[[WAF Bypass]]'
- '[[White spaces alternatives]]'
---

# SQL Injection - Bypassing Space Filter and Selecting All Users

## Summary

SQL Injection is a technique used by attackers to exploit web applications that are using SQL databases. In this particular procedure, the attacker is bypassing a WAF filter that is blocking spaces in the input. The attacker is using different techniques such as comments and parenthesis to achieve 

## Description

# Description

SQL Injection is a technique used by attackers to exploit web applications that are using SQL databases. In this particular procedure, the attacker is bypassing a WAF filter that is blocking spaces in the input. The attacker is using different techniques such as comments and parenthesis to achieve the objective of selecting all users where a certain condition is met. This technique can lead to credential access and sensitive data exposure. Business value of this procedure is that it can be used to gain unauthorized access to sensitive data, such as customer information or financial data.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL Injection

1. Web browser and internet access

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL Injection attacks

1. Use a WAF that can detect and block SQL Injection attempts

1. Regularly update the web application and database software to prevent known vulnerabilities

 

## Objectives

1. Bypass WAF filter blocking spaces in the input

1. Select all users where a certain condition is met

 

# Instructions

1. This command is used for SQL injection attacks where the target application filters out the traditional space character (%20) to prevent SQL injection. This command provides a list of alternative whitespace characters that can be used to bypass the filter and inject malicious SQL code.

 



**Code**: [[?id=1%09and%091=1%09--
?id=1%0Dand%0D1=1%0D--
?id=]]



> The data field in the provided JSON object contains a list of SQL injection payloads that use alternative whitespace characters to bypass space filters. These payloads can be used in the query string of a URL to inject SQL code into the target application's database. The lang field specifies that the payloads are written in SQL. The text field provides a brief description of the payload. The instruction field provides an overview of the command and its purpose. The name field provides a descriptive name for the command.

2. This command is used to perform SQL injection using comments to bypass the requirement of whitespace. It can be used to manipulate data in a database by injecting malicious SQL code.

 



**Code**: [[?id=1/*comment*/and/**/1=1/**/--]]



> The '/*comment*/' and '/**/' are used to comment out parts of the SQL statement so that the injected code can be executed without the need for whitespace. The 'and 1=1' statement is used to ensure that the injected code is always executed. This command can be dangerous if not used properly and can lead to data breaches and other security issues.

3. To perform SQL injection using parenthesis, you need to identify the vulnerable parameter in the URL and add the injection payload inside the parenthesis. In this example, the injection payload is '1)and(1)=(1)--'. The double dash at the end is used to comment out the rest of the query.

 



**Code**: [[?id=(1)and(1)=(1)--]]



> The injection payload '1)and(1)=(1)--' is added inside the parenthesis of the vulnerable parameter. This will cause the SQL query to be modified and return all the records from the database. The 'and(1)=(1)' part of the payload is used to bypass the authentication check and the double dash at the end is used to comment out the rest of the query.

4. This command selects all users from the 'users' table where the value in the first column is equal to 1.

 

The 'SELECT' command is used to retrieve data from a database. The '*' symbol after 'SELECT' indicates that we want to retrieve all columns from the 'users' table. 'FROM' is used to specify the table we want to retrieve data from, in this case it is the 'users' table. 'WHERE' is used to specify a condition that must be met for the data to be retrieved. In this case, the condition is that the value in the first column must be equal to 1. This command is useful when we want to retrieve specific data from a table that meets certain criteria.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Security Support Provider|T1101 - Security Support Provider]]

## Tags

- [[SQL Injection]]
- [[WAF Bypass]]
- [[White spaces alternatives]]


