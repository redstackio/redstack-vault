---
id: 7b8f1de3-48cc-4818-8852-871c04659331
name: DB2 Injection - List Columns
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.782456+00:00'
updated_at: '2023-04-10T20:22:00.114645+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[List Columns]]'
commands:
- '[[Retrieve information about columns in a table]]'
---

# DB2 Injection - List Columns

## Summary

DB2 Injection is a technique used to exploit vulnerabilities in DB2 databases to gain unauthorized access to sensitive information. In this procedure, the attacker uses SQL injection to retrieve details of columns from a table in the database. By doing so, the attacker can gain insight into the str

## Description

# Description

DB2 Injection is a technique used to exploit vulnerabilities in DB2 databases to gain unauthorized access to sensitive information. In this procedure, the attacker uses SQL injection to retrieve details of columns from a table in the database. By doing so, the attacker can gain insight into the structure of the database and the types of data stored in it. This information can be used to plan further attacks or to exfiltrate sensitive data.

To retrieve column details from a table, the attacker can use the 'LISTAGG' function in a SQL injection query. The 'LISTAGG' function concatenates the values of a column into a single string, which can be used to retrieve the column names and data types. The attacker can then use this information to craft further SQL injection queries to extract sensitive data.

The business value of this procedure is that it allows attackers to gain access to sensitive data stored in DB2 databases, which can include personal information, financial data, and intellectual property.

 

## Requirements

1. Access to a vulnerable DB2 database

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Monitor database logs for suspicious activity

 

## Objectives

1. Retrieve details of columns from a table in a DB2 database

1. Gain insight into the structure of the database and the types of data stored in it

1. Plan further attacks or exfiltrate sensitive data

 

# Instructions

1. This command retrieves the details of columns present in a table. The 'sysibm.syscolumns' table contains the details of all columns present in all tables in the database. The 'select' statement is used to retrieve the 'name' of the column, the 'tbname' of the table to which it belongs, and the 'coltype' of the column.

 



**Code**: [[select name, tbname, coltype from sysibm.syscolumn]]



> To use this command, simply replace 'sysibm.syscolumns' with 'syscat.columns' or 'sysstat.columns' to retrieve the details of columns present in all tables or system tables respectively. The 'name' column contains the name of the column, 'tbname' column contains the name of the table to which the column belongs, and the 'coltype' column contains the data type of the column.



**Command** ([[Retrieve information about columns in a table]]):

```bash
select name, tbname, coltype from sysibm.syscolumns -- also valid syscat and sysstat
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Retrieve information about columns in a table]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[List Columns]]


