---
id: c1da6504-3cc6-4f11-8149-eab2e553f53f
name: MSSQL Instance Discovery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.831936+00:00'
updated_at: '2023-04-10T20:36:47.877280+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Application Window Discovery|T1010 - Application Window Discovery]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Discover Remote SQL Server Instances]]'
- '[[Identify Instances and Databases]]'
- '[[MSSQL Server]]'
commands:
- '[[Get-SQLInstanceBroadcast]]'
- '[[Get-SQLInstanceScanUDPThreaded]]'
---

# MSSQL Instance Discovery

## Summary

MSSQL Instance Discovery is a reconnaissance technique used to identify remote SQL Server instances by broadcasting a SQL Server Browser request to the network. This technique can be used to identify potential targets for further attacks, such as SQL Injection or Privilege Escalation. 

The SQL Ins

## Description

# Description

MSSQL Instance Discovery is a reconnaissance technique used to identify remote SQL Server instances by broadcasting a SQL Server Browser request to the network. This technique can be used to identify potential targets for further attacks, such as SQL Injection or Privilege Escalation. 

The SQL Instance Broadcast and Scan command sends a request to the SQL Server Browser service, which responds with a list of all SQL Server instances running on the network. This information can be used to identify potential targets for further attacks or to verify the presence of a specific SQL Server instance.

 

## Requirements

1. Network access

 

## Defense

1. Limit network access to SQL Server instances to only trusted IP addresses

1. Disable SQL Server Browser service if not needed

1. Implement network segmentation to prevent lateral movement

 

## Objectives

1. Identify remote SQL Server instances on the network

 

# Instructions

1. This command allows you to broadcast and scan for SQL instances on a specified computer. The Get-SQLInstanceBroadcast command sends a UDP broadcast message to discover SQL Server instances on the network. The Get-SQLInstanceScanUDPThreaded command scans for SQL Server instances on the specified computer. 

 



**Code**: [[Get-SQLInstanceBroadcast -Verbose
Get-SQLInstanceS]]



> The -Verbose parameter provides detailed information about the progress of the command. The -ComputerName parameter specifies the name of the computer to scan for SQL Server instances. Use this command to discover SQL Server instances on a network and gather information about them. 



**Command** ([[Get-SQLInstanceBroadcast]]):

```bash
Get-SQLInstanceBroadcast -Verbose
```





**Command** ([[Get-SQLInstanceScanUDPThreaded]]):

```bash
Get-SQLInstanceScanUDPThreaded -Verbose -ComputerName SQLServer1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Application Window Discovery|T1010 - Application Window Discovery]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Get-SQLInstanceBroadcast]]
- [[Get-SQLInstanceScanUDPThreaded]]

## Tags

- [[Discover Remote SQL Server Instances]]
- [[Identify Instances and Databases]]
- [[MSSQL Server]]


