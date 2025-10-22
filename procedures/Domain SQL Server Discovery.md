---
id: 6ba4d15f-0028-4ade-b226-885dcd5822ae
name: Domain SQL Server Discovery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.802253+00:00'
updated_at: '2023-04-10T20:36:41.008602+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Discover Domain SQL Server Instances]]'
- '[[Identify Instances and Databases]]'
- '[[MSSQL Server]]'
commands:
- '[[Get Database Names]]'
- '[[Get Server Info for Found Instances]]'
- '[[Get SQL Instance Domain]]'
---

# Domain SQL Server Discovery

## Summary

Domain SQL Server Discovery is a technique used by attackers to identify SQL Server instances that are part of a Windows domain. Attackers can use this technique to gain an understanding of the domain's database infrastructure and to identify potential targets for further attacks. This technique ca

## Description

# Description

Domain SQL Server Discovery is a technique used by attackers to identify SQL Server instances that are part of a Windows domain. Attackers can use this technique to gain an understanding of the domain's database infrastructure and to identify potential targets for further attacks. This technique can be executed using various tools or scripts that can query the domain for SQL Server instances.

## Requirements

1. Access to the Windows domain.

## Defense

1. Disable or restrict access to unnecessary protocols and ports.

1. Implement network segmentation to limit access to sensitive systems.

1. Monitor network traffic for suspicious activity.

## Objectives

1. Identify SQL Server instances that are part of a Windows domain.

1. Gain an understanding of the domain's database infrastructure.

# Instructions

1. To retrieve information about SQL Server instances and databases, use the following commands:

**Code**: [[Get-SQLInstanceDomain -Verbose
# Get Server Info f]]

> 1. Get-SQLInstanceDomain -Verbose: This command retrieves information about all SQL Server instances found in the current domain.

2. Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose: This command retrieves detailed information about each SQL Server instance found in the current domain, including server name, version, edition, and more.

3. Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults: This command retrieves a list of all databases on each SQL Server instance found in the current domain, excluding system databases.

**Command** ([[Get SQL Instance Domain]]):

```bash
Get-SQLInstanceDomain -Verbose
```

**Command** ([[Get Server Info for Found Instances]]):

```bash
Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
```

**Command** ([[Get Database Names]]):

```bash
Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[Get Database Names]]
- [[Get Server Info for Found Instances]]
- [[Get SQL Instance Domain]]

## Tags

- [[Discover Domain SQL Server Instances]]
- [[Identify Instances and Databases]]
- [[MSSQL Server]]
