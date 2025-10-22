---
id: db3ad674-d5de-4526-9542-0226c75cb894
name: MSSQL Hostname Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.585477+00:00'
updated_at: '2023-04-10T20:22:44.905238+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[MSSQL Hostname]]'
- '[[MSSQL Injection]]'
commands:
- '[[Get Host Name]]'
- '[[Get Server Name]]'
---

# MSSQL Hostname Enumeration

## Summary

MSSQL Hostname Enumeration is a technique used to identify the hostname of a MSSQL server using SQL Injection. This technique can be used by an attacker to gain information about the target environment, which can be used in further attacks. To use this technique, an attacker will leverage SQL Injec

## Description

# Description

MSSQL Hostname Enumeration is a technique used to identify the hostname of a MSSQL server using SQL Injection. This technique can be used by an attacker to gain information about the target environment, which can be used in further attacks. To use this technique, an attacker will leverage SQL Injection vulnerabilities in MSSQL to execute a query that returns the hostname of the server. This technique can be used to identify the target environment, which can be used in further attacks such as lateral movement or privilege escalation. 

From a technical perspective, this technique involves crafting SQL Injection payloads that leverage the MSSQL SERVERPROPERTY() function to retrieve the hostname. The SERVERPROPERTY() function is used to retrieve information about the server, including the hostname. This technique requires knowledge of SQL Injection and the MSSQL syntax. 

From a business value perspective, this technique can be used to identify vulnerable MSSQL servers within an organization. This information can be used to prioritize patching and remediation efforts.

## Requirements

1. Access to a vulnerable MSSQL server

1. Knowledge of SQL Injection and MSSQL syntax

## Defense

1. Implement input validation and sanitization to prevent SQL Injection vulnerabilities

1. Use parameterized queries to prevent SQL Injection vulnerabilities

1. Implement network segmentation to limit the attack surface for MSSQL servers

## Objectives

1. Identify the hostname of a MSSQL server using SQL Injection

# Instructions

1. This command retrieves the hostname of the server on which the SQL Server instance is running.

To execute this command, open SQL Server Management Studio and connect to the instance you want to retrieve the hostname for. Then, open a new query window and paste the command into the window. Finally, click the Execute button to run the command.

**Code**: [[SELECT HOST_NAME()
SELECT @@hostname;]]

> The command consists of two SELECT statements. The first statement uses the HOST_NAME() function to retrieve the hostname of the server. The second statement uses the @@hostname system variable to retrieve the same information. Both statements produce the same result, which is the name of the server on which the SQL Server instance is running.

**Command** ([[Get Host Name]]):

```bash
SELECT HOST_NAME()
```

**Command** ([[Get Server Name]]):

```bash
SELECT @@hostname;
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Get Host Name]]
- [[Get Server Name]]

## Tags

- [[MSSQL Hostname]]
- [[MSSQL Injection]]
