---
id: d50f9e11-3f69-40f4-86ad-08d3e3318485
name: MSSQL Version Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.557317+00:00'
updated_at: '2023-04-10T20:22:39.738059+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL version]]'
commands:
- '[[MySQL Version]]'
---

# MSSQL Version Enumeration

## Summary

MSSQL Version Enumeration is a technique used to identify the version of Microsoft SQL Server running on a targeted system. An attacker can use this information to identify vulnerabilities or weaknesses specific to the version of SQL Server running. By exploiting these vulnerabilities, the attacker

## Description

# Description

MSSQL Version Enumeration is a technique used to identify the version of Microsoft SQL Server running on a targeted system. An attacker can use this information to identify vulnerabilities or weaknesses specific to the version of SQL Server running. By exploiting these vulnerabilities, the attacker can gain access to sensitive information or even take control of the system. This technique is commonly used in conjunction with other SQL injection attacks.

To perform this technique, the attacker sends a specially crafted SQL query to the targeted system. The response to this query provides information about the version of SQL Server running on the system. This technique can be performed manually or using automated tools.

The business value of this technique is that it allows organizations to identify vulnerabilities and weaknesses in their SQL Server deployments, and take steps to remediate them before they can be exploited by attackers.

## Requirements

1. Access to the targeted system

1. Knowledge of SQL injection techniques

1. Access to a tool capable of sending SQL queries to the targeted system

## Defense

1. Ensure that all SQL Server deployments are running the latest version and have all security patches applied

1. Implement strong authentication and access controls to prevent unauthorized access to SQL Server

1. Regularly perform vulnerability assessments and penetration testing to identify and remediate vulnerabilities in SQL Server deployments

## Objectives

1. Identify the version of Microsoft SQL Server running on a targeted system

1. Identify vulnerabilities or weaknesses specific to the version of SQL Server running

1. Use the identified vulnerabilities to gain access to sensitive information or take control of the system

# Instructions

1. This command retrieves the version of SQL currently running.

**Code**: [[SELECT @@version]]

> The SELECT @@version command returns the version of SQL Server that is currently running. This is useful when troubleshooting issues or verifying that the correct version is installed. The output will include the version number, build number, and other information about the SQL Server instance.

**Command** ([[MySQL Version]]):

```bash
SELECT @@version
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Commands Used

- [[MySQL Version]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL version]]
