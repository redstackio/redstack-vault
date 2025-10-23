---
id: d6e534ca-065f-413f-8ac1-d21c5baf37e1
name: Google BigQuery SQL Injection with Comment Syntax
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.333291+00:00'
updated_at: '2023-04-10T20:21:06.444748+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[BigQuery Comment]]'
- '[[Google BigQuery SQL Injection]]'
---

# Google BigQuery SQL Injection with Comment Syntax

## Summary

Google BigQuery is a cloud-based data warehousing and business intelligence solution that allows users to query large datasets using SQL-like syntax. However, like any SQL-based system, BigQuery is vulnerable to SQL injection attacks. This particular procedure utilizes comment syntax to bypass inpu

## Description

# Description

Google BigQuery is a cloud-based data warehousing and business intelligence solution that allows users to query large datasets using SQL-like syntax. However, like any SQL-based system, BigQuery is vulnerable to SQL injection attacks. This particular procedure utilizes comment syntax to bypass input validation and inject malicious SQL code into a query, enabling an attacker to execute arbitrary SQL commands on the BigQuery database. This technique can be used to exfiltrate sensitive data, modify or delete data, or even gain unauthorized access to other parts of the system.

 

## Requirements

1. Valid BigQuery account credentials

1. Access to the BigQuery API

 

## Defense

1. Implement input validation to prevent malicious SQL code from being injected

1. Use parameterized queries to prevent SQL injection attacks

1. Limit user privileges to only necessary functions and data

 

## Objectives

1. Inject malicious SQL code into a BigQuery query

1. Execute arbitrary SQL commands on the BigQuery database

 

# Instructions

1. The 'select' command is used to retrieve data from one or more tables in a database. The '1' in the command indicates that we want to retrieve only the first column of data. The '#' symbol and the '/*' and '*/' are comments that can be used to add notes to the code.

 



**Code**: [[select 1#from here it is not working
select 1/*bet]]



> The 'select' command is followed by the column name(s) or an asterisk (*) to select all columns. The 'from' keyword is used to specify the table(s) from which the data should be retrieved. Additional clauses like 'where', 'order by', and 'group by' can be added to filter, sort, and group the data as needed. The '1' in the command tells the database to retrieve only the first column of data. Comments can be added to the code using the '#' symbol or '/*' and '*/'.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[BigQuery Comment]]
- [[Google BigQuery SQL Injection]]


