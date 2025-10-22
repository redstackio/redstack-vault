---
id: ab835cb7-8549-4da6-935b-ff79388e6a4d
name: PostgreSQL Database Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.665658+00:00'
updated_at: '2023-04-10T20:23:14.414974+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL List Database]]'
commands:
- '[[List all databases]]'
---

# PostgreSQL Database Enumeration

## Summary

PostgreSQL Database Enumeration is a technique used by attackers to identify the databases running on a PostgreSQL server. Attackers can use this technique to identify the databases present on the server and plan their next steps. This technique involves injecting malicious code into the PostgreSQL

## Description

# Description

PostgreSQL Database Enumeration is a technique used by attackers to identify the databases running on a PostgreSQL server. Attackers can use this technique to identify the databases present on the server and plan their next steps. This technique involves injecting malicious code into the PostgreSQL server to extract the database names. Once the database names are extracted, the attacker can plan their next move. 

From a technical standpoint, this technique involves injecting SQL code into the PostgreSQL server to extract the database names. The attacker can use various tools and techniques to perform this injection. The attacker can also use various methods to extract the database names. 

The business value of this technique lies in the fact that it can help attackers identify the databases present on a PostgreSQL server. This information can be used to plan further attacks and gain access to sensitive information.

## Requirements

1. Access to the PostgreSQL server

1. Knowledge of SQL injection techniques

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Use strong and complex passwords for the PostgreSQL server

1. Implement network segmentation to limit access to the PostgreSQL server

## Objectives

1. Identify the databases present on a PostgreSQL server

1. Plan further attacks based on the identified databases

1. Gain access to sensitive information

# Instructions

1. This command lists all the databases in the current PostgreSQL server.

**Code**: [[SELECT datname FROM pg_database]]

> The 'SELECT' statement retrieves the 'datname' column from the 'pg_database' table. This table contains information about all the databases in the server. Running this command will return a list of all the database names.

**Command** ([[List all databases]]):

```bash
SELECT datname FROM pg_database
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[List all databases]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL List Database]]
