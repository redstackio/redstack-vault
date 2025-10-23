---
id: f13b91fd-829d-43a2-bccd-64780d1a8bf3
name: SQL Injection via POST request with SQLMap
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.314510+00:00'
updated_at: '2023-04-10T20:24:25.105654+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Custom injection in UserAgent/Header/Referer/Cookie]]'
- '[[SQL Injection]]'
- '[[SQL injection using SQLmap]]'
commands:
- '[[SQL Injection using sqlmap]]'
---

# SQL Injection via POST request with SQLMap

## Summary

SQL Injection is a technique used to exploit vulnerabilities in web applications that use SQL databases. Attackers use SQL injection to execute malicious SQL statements that can access sensitive data, modify data, or even delete data. In this procedure, an attacker uses SQLMap to perform SQL inject

## Description

# Description

SQL Injection is a technique used to exploit vulnerabilities in web applications that use SQL databases. Attackers use SQL injection to execute malicious SQL statements that can access sensitive data, modify data, or even delete data. In this procedure, an attacker uses SQLMap to perform SQL injection via a POST request. SQLMap is an open-source tool that automates the process of detecting and exploiting SQL injection vulnerabilities. By using SQLMap, an attacker can easily identify and exploit SQL injection vulnerabilities in a web application.

From a technical perspective, SQLMap sends a series of specially crafted SQL statements to the web application's backend database in order to extract information. The tool automates the process of identifying the type of database management system (DBMS) being used, the structure of the database, and the data stored within it. SQLMap can also be used to gain a remote shell on the target system, allowing the attacker to execute arbitrary commands and take control of the system.

From a business perspective, SQL injection attacks can have serious consequences. Attackers can steal sensitive data such as customer information, financial records, and intellectual property. This can result in financial loss, damage to reputation, and legal and regulatory penalties.

 

## Requirements

1. Access to the target web application

1. Knowledge of the target web application's backend database

1. SQLMap tool installed on the attacker's system

 

## Defense

1. Input validation and sanitization should be implemented in the web application to prevent SQL injection attacks

1. Database access should be restricted to only authorized users

1. Regular vulnerability assessments and penetration testing should be performed to identify and mitigate SQL injection vulnerabilities

 

## Objectives

1. Identify and exploit SQL injection vulnerabilities in a web application

1. Extract sensitive data from the backend database

1. Gain remote access to the target system

 

# Instructions

1. To perform a SQL injection attack on a website, use SQLMap with the following command:

python sqlmap.py -u "http://example.com" --data "username=admin&password=pass"  --headers="x-forwarded-for:127.0.0.1*"

This command will send a POST request to the specified URL with the specified data and headers. SQLMap will then automatically detect any SQL injection vulnerabilities and exploit them.

Note: The '*' in the output indicates the location of the injection.

 



**Code**: [[python sqlmap.py -u "http://example.com" --data "u]]



> The 'python' command is used to run the SQLMap tool. The '-u' flag specifies the URL of the target website. The '--data' flag specifies the data to be sent in the POST request. The '--headers' flag specifies any additional headers to be sent with the request.

SQLMap is a tool designed to automate the detection and exploitation of SQL injection vulnerabilities. It supports various database management systems and can perform a variety of tasks, such as dumping databases, accessing the underlying file system, and executing arbitrary commands on the server.



**Command** ([[SQL Injection using sqlmap]]):

```bash
python sqlmap.py -u "http://example.com" --data "username=admin&password=pass"  --headers="x-forwarded-for:127.0.0.1*"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[SQL Injection using sqlmap]]

## Tags

- [[Custom injection in UserAgent/Header/Referer/Cookie]]
- [[SQL Injection]]
- [[SQL injection using SQLmap]]


