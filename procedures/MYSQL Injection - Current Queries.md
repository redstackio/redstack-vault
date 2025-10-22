---
id: ff430666-de0e-40b1-bf26-eecb32c06e77
name: MYSQL Injection - Current Queries
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.745365+00:00'
updated_at: '2023-04-10T20:22:53.100184+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Supply Chain Compromise|T1195 - Supply Chain Compromise]]'
tags:
- '[[MYSQL Current queries]]'
- '[[MYSQL Injection]]'
---

# MYSQL Injection - Current Queries

## Summary

MYSQL Injection is a technique used to exploit a vulnerability in a web application that allows an attacker to execute malicious SQL statements. This procedure focuses on listing the current queries being executed on the MYSQL database. By injecting specific SQL statements, an attacker can gain acc

## Description

# Description

MYSQL Injection is a technique used to exploit a vulnerability in a web application that allows an attacker to execute malicious SQL statements. This procedure focuses on listing the current queries being executed on the MYSQL database. By injecting specific SQL statements, an attacker can gain access to sensitive information stored in the database. This can include user credentials, personal information, and other sensitive data. The business value of this procedure is to identify vulnerabilities in the web application and database and to prevent data breaches.

## Requirements

1. Access to the web application

1. Access to the MYSQL database

1. Knowledge of MYSQL Injection techniques

## Defense

1. Ensure that the web application is up-to-date with the latest security patches

1. Implement input validation and sanitization to prevent SQL Injection attacks

1. Implement database security measures such as access control and encryption

## Objectives

1. Identify current queries being executed on the MYSQL database

1. Identify vulnerabilities in the web application and database

1. Prevent data breaches

# Instructions

1. To use this command, simply execute the SQL query provided. The results will show all current operations being performed by the database.

**Code**: [[union SELECT 1,state,info,4 FROM INFORMATION_SCHEM]]

> The 'INFORMATION_SCHEMA.PROCESSLIST' table contains information about all current client connections and server threads. The 'state' and 'info' fields in the SELECT statement provide additional details about the current operation being performed by the database. The second part of the command is a one-shot example to dump the table content in a single query.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Supply Chain Compromise|T1195 - Supply Chain Compromise]]

## Tags

- [[MYSQL Current queries]]
- [[MYSQL Injection]]
