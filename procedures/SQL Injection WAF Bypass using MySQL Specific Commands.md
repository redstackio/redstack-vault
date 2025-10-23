---
id: cdc95f23-a64f-4764-80a4-9f9dead3c53c
name: SQL Injection WAF Bypass using MySQL Specific Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.843368+00:00'
updated_at: '2023-04-10T20:24:24.377119+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[More MySQL specific]]'
- '[[SQL Injection]]'
- '[[WAF Bypass]]'
commands:
- '[[Check InnoDB version]]'
- '[[Check MySQL version]]'
- '[[Check MySQL version]]'
- '[[Retrieving tables from public schema]]'
- '[[Select from mysql.innodb_table_stats]]'
- '[[Show Tables in dvwa]]'
---

# SQL Injection WAF Bypass using MySQL Specific Commands

## Summary

SQL Injection is a technique used to exploit vulnerabilities in a web application's input validation process, allowing an attacker to inject malicious SQL statements into the application's backend database. WAF Bypass is a technique used to bypass Web Application Firewalls. This specific procedure 

## Description

# Description

SQL Injection is a technique used to exploit vulnerabilities in a web application's input validation process, allowing an attacker to inject malicious SQL statements into the application's backend database. WAF Bypass is a technique used to bypass Web Application Firewalls. This specific procedure uses MySQL specific commands to bypass WAFs and execute SQL Injection attacks. By using commands like Information Schema Tables, MySQL InnoDB Table Stats, and MySQL Version Information, an attacker can gather information about the database and bypass WAFs that are not configured to block these types of commands. This technique can be used to gain unauthorized access to sensitive data, modify or delete data, or escalate privileges within the system.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL Injection techniques

1. Knowledge of MySQL specific commands

 

## Defense

1. Implement proper input validation techniques to prevent SQL Injection attacks

1. Configure WAFs to block MySQL specific commands

1. Regularly monitor and analyze web application logs for suspicious activities

 

## Objectives

1. Bypass WAFs that are not configured to block MySQL specific commands

1. Execute SQL Injection attacks

1. Gain unauthorized access to sensitive data

1. Modify or delete data

1. Escalate privileges within the system

 

# Instructions

1. This command retrieves a list of tables in the current database schema.

 



**Code**: [[information_schema.tables]]



> The `information_schema.tables` table contains information about tables in the current database schema. This command can be used to retrieve a list of tables in the schema. The table includes information such as the table name, table type, and the database engine used for the table. This command can be useful for database administrators or developers who need to work with database metadata.



**Command** ([[Retrieving tables from public schema]]):

```bash
SELECT * FROM information_schema.tables WHERE table_schema = 'public';
```



2. The 'mysql.innodb_table_stats' table provides information about InnoDB tables in the MySQL instance. The 'select *' command is used to retrieve all the available information from the table. The 'show tables' command is used to display the list of tables in the 'dvwa' database.

 



**Code**: [[select * from mysql.innodb_table_stats;
+---------]]



> The 'database_name' and 'table_name' fields provide the name of the database and the table respectively. The 'last_update' field provides the date and time when the table was last updated. The 'n_rows' field provides the number of rows in the table. The 'clustered_index_size' field provides the size of the clustered index for the table. The 'sum_of_other_index_sizes' field provides the sum of the sizes of all the other indexes for the table. The 'show tables' command is used to display the list of tables in the 'dvwa' database.



**Command** ([[Select from mysql.innodb_table_stats]]):

```bash
select * from mysql.innodb_table_stats;
+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+
| database_name  | table_name            | last_update         | n_rows | clustered_index_size | sum_of_other_index_sizes |
+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+
| dvwa           | guestbook             | 2017-01-19 21:02:57 |      0 |                    1 |                        0 |
| dvwa           | users                 | 2017-01-19 21:03:07 |      5 |                    1 |                        0 |
...\n+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+\n\n
```





**Command** ([[Show Tables in dvwa]]):

```bash
show tables in dvwa;
+----------------+
| Tables_in_dvwa |
+----------------+
| guestbook      |
| users          |
+----------------+
```



3. To retrieve the version information of MySQL, you can use any of the following commands:
1. select @@innodb_version;
2. select @@version;
3. select version();

The first command returns the version of the InnoDB storage engine, while the second and third commands return the version of MySQL itself. These commands can be useful when troubleshooting issues or checking compatibility with other software.

 



**Code**: [[mysql> select @@innodb_version;
+-----------------]]



> The argument for each command is simply the command itself. There are no additional arguments required to retrieve the version information.



**Command** ([[Check InnoDB version]]):

```bash
mysql> select @@innodb_version;
```





**Command** ([[Check MySQL version]]):

```bash
mysql> select @@version;
```





**Command** ([[Check MySQL version]]):

```bash
mysql> select version();
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Check InnoDB version]]
- [[Check MySQL version]]
- [[Check MySQL version]]
- [[Retrieving tables from public schema]]
- [[Select from mysql.innodb_table_stats]]
- [[Show Tables in dvwa]]

## Tags

- [[More MySQL specific]]
- [[SQL Injection]]
- [[WAF Bypass]]


