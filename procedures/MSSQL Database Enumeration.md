---
id: 771eb178-060e-472c-a2ea-b2095648090a
name: MSSQL Database Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.646275+00:00'
updated_at: '2023-04-10T20:22:46.779092+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL List databases]]'
commands:
- '[[Concatenate all database names]]'
- '[[List all databases]]'
- '[[List system databases]]'
---

# MSSQL Database Enumeration

## Summary

MSSQL Database Enumeration is an attack that involves using SQL injection techniques to identify and list all databases on a target MSSQL server. This attack can be used to gather information about the target's database environment and plan further attacks. The attacker can use this information to 

## Description

# Description

MSSQL Database Enumeration is an attack that involves using SQL injection techniques to identify and list all databases on a target MSSQL server. This attack can be used to gather information about the target's database environment and plan further attacks. The attacker can use this information to identify the target's sensitive data and launch targeted attacks against it. The technical explanation involves injecting malicious SQL code into the target's database management system (DBMS) to retrieve information about the databases. The business value of this attack is that it can help an attacker to identify and exploit vulnerabilities in the target's database environment that could lead to data theft, data manipulation, or denial of service attacks.

## Requirements

1. Access to the target's MSSQL server

1. Knowledge of SQL injection techniques

1. MSSQL client or tool to interact with the target's database management system

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Limit user privileges to prevent unauthorized access to the database management system

## Objectives

1. Identify all MSSQL databases on the target server

1. Gather information about the target's database environment

1. Plan further attacks against the target

# Instructions

1. To list all databases in the current SQL Server instance, run the following commands:

**Code**: [[SELECT name FROM master..sysdatabases;
SELECT DB_N]]

> The first command retrieves the names of all databases in the instance. The second command lists the names of the system databases, including master, tempdb, model, and msdb. The third command uses the STRING_AGG function (available only in MSSQL 2017+) to concatenate the names of all databases into a single string, separated by a specified delimiter.

**Command** ([[List all databases]]):

```bash
SELECT name FROM master..sysdatabases;
```

**Command** ([[List system databases]]):

```bash
SELECT DB_NAME(N); -- for N = 0, 1, 2, ...
```

**Command** ([[Concatenate all database names]]):

```bash
SELECT STRING_AGG(name, ', ') FROM master..sysdatabases; -- Change delimiter value such as ', ' to anything else you want => master, tempdb, model, msdb   (Only works in MSSQL 2017+)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Concatenate all database names]]
- [[List all databases]]
- [[List system databases]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL List databases]]
