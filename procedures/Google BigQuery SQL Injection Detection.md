---
id: f0ab8039-cbed-4195-b5cb-9bea319b9773
name: Google BigQuery SQL Injection Detection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.303846+00:00'
updated_at: '2023-04-10T20:21:04.791649+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Application Window Discovery|T1010 - Application Window Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
tags:
- '[[Detection]]'
- '[[Google BigQuery SQL Injection]]'
commands:
- '[[Gathering all dataset names]]'
- '[[Gathering data from specific project id & dataset]]'
- '[[Gathering project id]]'
---

# Google BigQuery SQL Injection Detection

## Summary

Google BigQuery is a cloud-based data warehouse that allows users to analyze large datasets using SQL queries. However, if not properly secured, BigQuery can be vulnerable to SQL injection attacks. SQL injection is a technique where an attacker injects malicious SQL code into a query, which can the

## Description

# Description

Google BigQuery is a cloud-based data warehouse that allows users to analyze large datasets using SQL queries. However, if not properly secured, BigQuery can be vulnerable to SQL injection attacks. SQL injection is a technique where an attacker injects malicious SQL code into a query, which can then be executed by the database. This can result in unauthorized access to sensitive data or even the complete compromise of the system.

Technical Explanation: An attacker can use SQL injection to bypass authentication, execute arbitrary SQL queries, and access sensitive data. This can be achieved by injecting malicious SQL code into a query that is executed by the database. For example, an attacker can use the 'union' operator to combine the results of two different queries, or the 'drop table' command to delete a table from the database.

Business Value: Detecting SQL injection attacks in BigQuery can prevent unauthorized access to sensitive data and protect the integrity of the system.

## Requirements

1. Access to Google BigQuery

1. Knowledge of SQL and SQL injection techniques

1. Proper authentication and access control measures in place

## Defense

1. Implement input validation and parameterized queries to prevent SQL injection attacks

1. Regularly monitor and analyze BigQuery logs for suspicious activity

1. Limit access to BigQuery and ensure proper authentication and access control measures are in place

## Objectives

1. Detect and prevent SQL injection attacks in Google BigQuery

1. Protect sensitive data stored in BigQuery

1. Ensure the integrity of the system

# Instructions

1. To gather information about the project and dataset, you can use the following commands:

1. select @@project_id: This command will return the project ID of the current project.

2. select schema_name from INFORMATION_SCHEMA.SCHEMATA: This command will return the names of all datasets in the current project.

3. select * from `project_id.dataset_name.table_name`: This command will return all the data from the specified table in the specified dataset of the current project.

**Code**: [[# Gathering project id
select @@project_id

# Gath]]

> The first command is used to get the project ID of the current project. This can be useful when working with multiple projects.

The second command is used to get the names of all datasets in the current project. This can be useful when you want to see what datasets are available to you.

The third command is used to get data from a specific table in a specific dataset of the current project. You need to replace 'project_id', 'dataset_name' and 'table_name' with the actual names of the project, dataset and table that you want to get data from.

**Command** ([[Gathering project id]]):

```bash
select @@project_id
```

**Command** ([[Gathering all dataset names]]):

```bash
select schema_name from INFORMATION_SCHEMA.SCHEMATA
```

**Command** ([[Gathering data from specific project id & dataset]]):

```bash
select * from `project_id.dataset_name.table_name`
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Application Window Discovery|T1010 - Application Window Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]
- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]

## Commands Used

- [[Gathering all dataset names]]
- [[Gathering data from specific project id & dataset]]
- [[Gathering project id]]

## Tags

- [[Detection]]
- [[Google BigQuery SQL Injection]]
