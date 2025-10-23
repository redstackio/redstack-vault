---
id: 6af27da7-3bf3-4172-be22-f0bb09ce3b13
name: Discovery of Local MSSQL Server Instances
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.775784+00:00'
updated_at: '2023-04-10T20:36:45.722496+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Software Discovery|T1518 - Software Discovery]]'
- '[[System Owner/User Discovery|T1033 - System Owner/User Discovery]]'
tags:
- '[[Discover Local SQL Server Instances]]'
- '[[Identify Instances and Databases]]'
- '[[MSSQL Server]]'
commands:
- '[[Get Local SQL Instances]]'
---

# Discovery of Local MSSQL Server Instances

## Summary

Discovery of local MSSQL Server instances is a technique used to identify any MSSQL Server instances running on the local machine. This information can be useful for attackers to determine what type of database is running and to identify potential targets. The discovery can be achieved by running a

## Description

# Description

Discovery of local MSSQL Server instances is a technique used to identify any MSSQL Server instances running on the local machine. This information can be useful for attackers to determine what type of database is running and to identify potential targets. The discovery can be achieved by running a simple command that lists all local instances of MSSQL Server. The business value of this procedure is that it helps attackers to identify potential targets for further attacks.

 

## Requirements

1. Access to the local machine

 

## Defense

1. Ensure that MSSQL Server instances are not running unnecessarily on machines that do not require them

1. Ensure that MSSQL Server instances are configured securely and are not accessible from the internet

1. Implement network segmentation to limit access to MSSQL Server instances

 

## Objectives

1. Identify local MSSQL Server instances

1. Determine the version and configuration of the MSSQL Server instance

 

# Instructions

1. This command retrieves information about all the SQL Server instances installed on the local machine.

 



**Code**: [[Get-SQLInstanceLocal]]



> The 'Get-SQLInstanceLocal' command is used to query the local machine for any installed SQL Server instances. The command returns a list of instances with details such as instance name, version, and edition. This command can be helpful when troubleshooting or managing SQL Server instances on a local machine. There are no arguments required for this command.



**Command** ([[Get Local SQL Instances]]):

```bash
Get-SQLInstanceLocal
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Software Discovery|T1518 - Software Discovery]]
- [[System Owner/User Discovery|T1033 - System Owner/User Discovery]]

## Commands Used

- [[Get Local SQL Instances]]

## Tags

- [[Discover Local SQL Server Instances]]
- [[Identify Instances and Databases]]
- [[MSSQL Server]]


