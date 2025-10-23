---
id: 3523d7db-da95-4e12-8096-e82f46670b33
name: DB2 Injection - Find Tables From Column Name
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.840684+00:00'
updated_at: '2023-04-10T20:22:04.805069+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Find Tables From Column Name]]'
commands:
- '[[Retrieve Table Name]]'
---

# DB2 Injection - Find Tables From Column Name

## Summary

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. In this specific procedure, we are looking to find tables based on a column name. This can be useful for attackers who are looking to extract sensitive information from the database. By using the 'Get Table 

## Description

# Description

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. In this specific procedure, we are looking to find tables based on a column name. This can be useful for attackers who are looking to extract sensitive information from the database. By using the 'Get Table Name for Username Column' command, we can identify which tables contain a specific column name, allowing us to further target our attack.

From a technical perspective, this procedure relies on injecting malicious code into the database in order to extract data. The 'Get Table Name for Username Column' command specifically uses a SQL injection technique to identify tables based on a column name.

The business value of this procedure is that it can help organizations identify vulnerabilities in their database and take steps to mitigate the risk of a data breach.

 

## Requirements

1. Access to a vulnerable DB2 database

1. Knowledge of SQL injection techniques

 

## Defense

1. Ensure that the DB2 database is properly secured and updated to prevent vulnerabilities

1. Regularly monitor the database for suspicious activity

1. Implement access controls to restrict access to sensitive data within the database

 

## Objectives

1. Identify tables in a DB2 database that contain a specific column name

1. Extract sensitive information from the identified tables

 

# Instructions

1. This command retrieves the name of the table that contains the 'username' column. To execute this command, connect to the database and run the SQL query provided in the 'data' field.

 



**Code**: [[select tbname from sysibm.syscolumns where name='u]]



> The 'select' statement is used to retrieve data from a database. In this case, we are retrieving the 'tbname' column from the 'sysibm.syscolumns' table where the 'name' column is equal to 'username'. This will return the name of the table that contains the 'username' column.



**Command** ([[Retrieve Table Name]]):

```bash
select tbname from sysibm.syscolumns where name='username'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Retrieve Table Name]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Find Tables From Column Name]]


