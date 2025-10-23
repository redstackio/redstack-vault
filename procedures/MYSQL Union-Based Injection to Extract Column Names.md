---
id: 6a57d8a3-1cfd-4583-8de0-c682f389480f
name: MYSQL Union-Based Injection to Extract Column Names
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.401446+00:00'
updated_at: '2023-04-10T20:22:52.403695+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[Extract columns name without information_schema]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Union Based]]'
commands:
- '[[Install MySQL 5]]'
- '[[MySQL version check]]'
---

# MYSQL Union-Based Injection to Extract Column Names

## Summary

A MYSQL union-based injection attack can be used to extract column names without using the information_schema database. This technique involves injecting a union statement into a vulnerable SQL query to retrieve the names of the columns in a table. By using this technique, an attacker can gain insi

## Description

# Description

A MYSQL union-based injection attack can be used to extract column names without using the information_schema database. This technique involves injecting a union statement into a vulnerable SQL query to retrieve the names of the columns in a table. By using this technique, an attacker can gain insight into the structure of a database and determine which columns contain sensitive information. This attack can be used to prepare for further attacks, such as data exfiltration or privilege escalation.

Technical Explanation: A union-based injection attack involves injecting a union statement into a vulnerable SQL query. This statement allows an attacker to combine the results of two or more SELECT statements into a single result set. By injecting a union statement along with a SELECT statement that retrieves column names, an attacker can retrieve the names of the columns in a table. 

Business Value: By understanding the structure of a database, an attacker can identify which columns contain sensitive information such as usernames, passwords, and other confidential data. This information can be used to launch further attacks, such as data exfiltration or privilege escalation.

 

## Requirements

1. Access to a vulnerable SQL query

1. Knowledge of SQL injection techniques

 

## Defense

1. Sanitize user input to prevent SQL injection attacks

1. Implement least privilege access controls to limit the impact of a successful attack

1. Monitor database activity for suspicious behavior, such as excessive queries or unusual data access patterns

 

## Objectives

1. Extract column names from a vulnerable SQL query

1. Identify sensitive information stored in a database

1. Prepare for further attacks, such as data exfiltration or privilege escalation

 

# Instructions

1. To check the version of MySQL, run the following command in the MySQL console:

SELECT VERSION();

 



**Code**: [[MySQL &gt;= 4.1]]



> This command will return the version of MySQL that is currently installed on the system. The output will be in the format of X.X.X, where X represents the version number. For example, if the output is 5.7.32, it means that MySQL version 5.7.32 is installed on the system.



**Command** ([[MySQL version check]]):

```bash
MySQL &gt;= 4.1
```



2. To perform SQL injection attack, use the following steps:
1. Identify the vulnerable input field
2. Determine the type of database
3. Determine the number of columns in the table
4. Use the UNION operator to append a malicious query
5. Extract sensitive information from the database
6. Modify or delete data in the database

 



**Code**: [[?id=(1)and(SELECT * from db.users)=(1)
-- Operand ]]



> In this specific example, the attacker is attempting to extract information from the 'users' table in the 'db' database. The injection attack is achieved by appending a malicious query to the original query, using the UNION operator to combine the results of the original query with the results of the malicious query. The '--' symbol is used to comment out the remaining part of the original query. The error message indicates that the original query is expecting 4 columns, but the injected query only returns one column, indicating that the query has been successfully injected.

3. To extract column name using SQL Injection, use the following command: ?id=1 and (1,2,3,4) = (SELECT * from db.users UNION SELECT 1,2,3,4 LIMIT 1)
--Column 'id' cannot be null

 



**Code**: [[?id=1 and (1,2,3,4) = (SELECT * from db.users UNIO]]



> This command can be used to extract the column name of a database table using SQL Injection. The command works by injecting a UNION SELECT statement into the original SQL query. This UNION SELECT statement is used to retrieve data from another table in the database, which can be used to extract the column name of the original table. The extracted column name can then be used to further exploit the system.

4. To install MySQL 5, follow these steps: 
1. Download the MySQL 5 installer from the official website. 
2. Run the installer and select the installation type (Typical, Complete, or Custom). 
3. Follow the prompts to complete the installation process. 
4. Once the installation is complete, configure the MySQL server by setting up the root user and creating any necessary databases and users. 
5. Start the MySQL server and verify that it is running correctly.

 



**Code**: [[MySQL 5]]



> The MySQL 5 installation process involves downloading the installer from the official website, selecting the appropriate installation type, following the prompts to complete the installation, and then configuring the MySQL server. During configuration, you will set up the root user and create any necessary databases and users. Once the installation and configuration are complete, you can start the MySQL server and begin using it. 



**Command** ([[Install MySQL 5]]):

```bash
sudo apt-get install mysql-server-5.7
```



5. This command is used to perform a SQL injection attack on a system that has a vulnerability of duplicate column names. The command uses the UNION operator to combine the results of two SELECT statements. In the first SELECT statement, we are selecting all columns from the users table and in the second SELECT statement, we are joining the users table with itself using the duplicate column name. The 'a' at the end of the query is an alias for the resulting table. This command can be used to bypass authentication, retrieve sensitive data, or modify data in the database.

 



**Code**: [[-1 UNION SELECT * FROM (SELECT * FROM users JOIN u]]



> The command starts with '-1' which is used to ensure that the injected SQL statement is not executed by the database. The 'UNION' operator is used to combine the results of two SELECT statements. In the first SELECT statement, we are selecting all columns from the 'users' table. In the second SELECT statement, we are joining the 'users' table with itself using the duplicate column name. The 'a' at the end of the query is an alias for the resulting table. The '--' symbol is used for commenting out the rest of the original query. This command can be used to bypass authentication, retrieve sensitive data, or modify data in the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Query Registry|T1012 - Query Registry]]

## Commands Used

- [[Install MySQL 5]]
- [[MySQL version check]]

## Tags

- [[Extract columns name without information_schema]]
- [[MYSQL Injection]]
- [[MYSQL Union Based]]


