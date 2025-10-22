---
id: 5477eaac-075b-48a4-80a5-e3dccc298c73
name: MSSQL Server Version Query
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.886561+00:00'
updated_at: '2023-04-10T20:36:38.573527+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Software Discovery|T1518 - Software Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Identify Instances and Databases]]'
- '[[MSSQL Server]]'
- '[[Version Query]]'
commands:
- '[[Get SQL Instance Domain]]'
- '[[Get SQL Version]]'
---

# MSSQL Server Version Query

## Summary

The MSSQL Server Version Query procedure is used to identify the version of a Microsoft SQL Server instance. This information can be used to determine if the server is vulnerable to known exploits or if specific features are available. The procedure executes a simple query to retrieve the version i

## Description

# Description

The MSSQL Server Version Query procedure is used to identify the version of a Microsoft SQL Server instance. This information can be used to determine if the server is vulnerable to known exploits or if specific features are available. The procedure executes a simple query to retrieve the version information from the target server. This procedure can be useful for both offensive and defensive purposes. 

From a technical perspective, this procedure executes a query against the target MSSQL Server instance using the Get-SQLInstanceDomain cmdlet. The cmdlet retrieves the version information from the SQL Server instance and returns it to the user. This information can be used to identify the specific version of the SQL Server instance that is running on the target system.

The business value of this procedure is that it allows organizations to identify potential vulnerabilities in their MSSQL Server instances before they can be exploited by attackers. By identifying vulnerable systems, organizations can take steps to patch or update their systems to prevent exploitation.

## Requirements

1. Authenticated access to the target MSSQL Server instance

1. PowerShell with the SQLServer module installed

## Defense

1. Ensure that MSSQL Server instances are kept up to date with the latest security patches

1. Limit access to MSSQL Server instances to only authorized personnel

1. Monitor MSSQL Server logs for suspicious activity

## Objectives

1. Identify the version of a Microsoft SQL Server instance

# Instructions

1. Get-SQLInstanceDomain

**Code**: [[Get-SQLInstanceDomain | Get-Query "select @@versio]]

> This command retrieves the SQL Server instances running on the current domain. The output of this command is piped to Get-Query which is used to execute the SQL query 'select @@version' against each instance. The result is the version of SQL Server running on each instance.

**Command** ([[Get SQL Instance Domain]]):

```bash
Get-SQLInstanceDomain
```

**Command** ([[Get SQL Version]]):

```bash
Get-Query "select @@version"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Software Discovery|T1518 - Software Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get SQL Instance Domain]]
- [[Get SQL Version]]

## Tags

- [[Identify Instances and Databases]]
- [[MSSQL Server]]
- [[Version Query]]
