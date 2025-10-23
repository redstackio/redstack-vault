---
id: 9230179f-b306-4b73-b4e1-b8fbe56c2704
name: SQL Injection using SQLmap for MySQL Database Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.344790+00:00'
updated_at: '2023-04-10T20:24:23.631197+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Second order injection]]'
- '[[SQL Injection]]'
- '[[SQL injection using SQLmap]]'
commands:
- '[[SQL Injection using sqlmap]]'
- '[[SQL Injection using sqlmap]]'
---

# SQL Injection using SQLmap for MySQL Database Enumeration

## Summary

SQL Injection is a type of attack that allows an attacker to inject malicious SQL statements into an application's database backend. SQLmap is a popular tool used to automate the process of identifying and exploiting SQL Injection vulnerabilities. Second order injection is a technique where the inj

## Description

# Description

SQL Injection is a type of attack that allows an attacker to inject malicious SQL statements into an application's database backend. SQLmap is a popular tool used to automate the process of identifying and exploiting SQL Injection vulnerabilities. Second order injection is a technique where the injection payload is stored in the database and executed at a later time, making it more difficult to detect.

In this procedure, we will use SQLmap to enumerate a MySQL database for information such as table names and column names. This information can be used to further exploit the database and extract sensitive data.

The business value of this procedure is that it allows an attacker to gain unauthorized access to sensitive data stored in a database, such as customer information or financial data. This can result in financial loss, reputational damage, and legal consequences.

 

## Requirements

1. Access to the target network

1. Credentials with sufficient privileges to access the database

1. SQLmap installed on the attacker's system

 

## Defense

1. Input validation should be implemented to prevent SQL Injection vulnerabilities

1. Database access should be restricted to only authorized users with the least privileges necessary

1. Regular security assessments should be conducted to identify and remediate vulnerabilities

 

## Objectives

1. Identify SQL Injection vulnerabilities in a MySQL database

1. Enumerate the database to gather information such as table and column names

 

# Instructions

1. The above command is used to enumerate MySQL databases using sqlmap tool. The command accepts multiple arguments such as:
1. -r: Path to the file containing the HTTP request that will be used in the attack.
2. --dbms: Specify the database management system to be targeted.
3. --second-order: Use second order injection point to exploit the target.
4. -v: Verbosity level of the output.
5. -D: Specify the database to be targeted.
6. -dbs: Enumerate all databases on the target server.

 



**Code**: [[python sqlmap.py -r /tmp/r.txt --dbms MySQL --seco]]



> This command is useful in situations where you want to identify the databases running on a MySQL server. It can also be used to gather information about the structure of the databases and tables within them. The tool sqlmap automates the process of exploiting SQL injection vulnerabilities and provides a lot of flexibility in terms of the types of attacks that can be performed.



**Command** ([[SQL Injection using sqlmap]]):

```bash
python sqlmap.py -r /tmp/r.txt --dbms MySQL --second-order "http://targetapp/wishlist" -v 3
```





**Command** ([[SQL Injection using sqlmap]]):

```bash
sqlmap -r 1.txt -dbms MySQL -second-order "http://<IP/domain>/joomla/administrator/index.php" -D "joomla" -dbs
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[SQL Injection using sqlmap]]
- [[SQL Injection using sqlmap]]

## Tags

- [[Second order injection]]
- [[SQL Injection]]
- [[SQL injection using SQLmap]]


