---
id: b7e648c4-fd77-48a5-9b34-ed5554cc631c
name: DB2 Injection with Comment Filtering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.578999+00:00'
updated_at: '2023-04-10T20:22:01.903665+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Bash History|T1139 - Bash History]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Comments]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
---

# DB2 Injection with Comment Filtering

## Summary

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. Attackers can use SQL injection attacks to bypass authentication, access sensitive data, and even take control of the database. This particular procedure involves using comments to filter out certain parts o

## Description

# Description

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. Attackers can use SQL injection attacks to bypass authentication, access sensitive data, and even take control of the database. This particular procedure involves using comments to filter out certain parts of a select query, which can help evade detection and bypass security measures. By using this technique, attackers can exfiltrate data from the database without being detected.

From a technical standpoint, this procedure involves injecting malicious SQL code into a select query that is executed by the database. By using comments, the attacker can filter out parts of the query that would normally trigger security alerts or errors. This allows the attacker to bypass security measures and access sensitive data.

The business value of this procedure is that attackers can gain access to sensitive data, such as customer information or financial records. This can lead to reputational damage, financial losses, and legal liabilities for the affected organization.

## Requirements

1. Access to the target network

1. Knowledge of the target DB2 database

1. Ability to inject SQL code into a select query

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries instead of dynamic queries to prevent injection attacks

1. Monitor database logs for suspicious activity and review access controls regularly

## Objectives

1. Gain unauthorized access to the DB2 database

1. Extract sensitive information from the database

1. Evade detection by security measures

# Instructions

1. To retrieve data from a database table, use the SELECT statement followed by the column names separated by commas. You can include comments in your query by using double dashes (--) followed by your comment.

**Code**: [[select blah from foo -- comment like this (double ]]

> The above command will select the 'blah' column from the 'foo' table in the database. The double dash comment is used to add a comment to the query that will not be executed. This can be used to explain the purpose of the query or to temporarily disable a part of the query.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Bash History|T1139 - Bash History]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Comments]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
