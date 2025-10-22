---
id: e6cfec99-f094-4ed4-a7bb-32f6bcf0395b
name: MSSQL Server Linked Database Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.014835+00:00'
updated_at: '2023-04-10T20:36:39.276730+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[Find Trusted Link]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
---

# MSSQL Server Linked Database Enumeration

## Summary

The MSSQL Server Linked Database Enumeration procedure involves the discovery of linked databases within a Microsoft SQL Server environment. This procedure is typically used by an attacker to gain access to sensitive data stored in a linked database. The attacker can use this procedure to discover 

## Description

# Description

The MSSQL Server Linked Database Enumeration procedure involves the discovery of linked databases within a Microsoft SQL Server environment. This procedure is typically used by an attacker to gain access to sensitive data stored in a linked database. The attacker can use this procedure to discover the trusted links between different databases, which can be used to pivot to other systems within the network. 

Technical Explanation: The MSSQL Server Linked Database Enumeration procedure involves querying the SQL Server system tables to identify linked servers and their configuration details. The attacker can use this information to identify potential vulnerabilities and targets for further exploitation. 

Business Value: By discovering linked databases, an attacker can gain access to sensitive data stored in the linked database. This data could include financial information, personally identifiable information (PII), and other sensitive data. The attacker can use this information for financial gain, identity theft, or other malicious purposes.

## Requirements

1. Access to the target MSSQL Server environment

1. Query permissions on the MSSQL Server system tables

## Defense

1. Implement network segmentation to limit access to the MSSQL Server environment

1. Enforce least privilege access controls to limit access to the MSSQL Server system tables

1. Regularly monitor and review MSSQL Server logs for suspicious activity

## Objectives

1. Identify linked databases within the target MSSQL Server environment

1. Gain access to sensitive data stored in the linked database

1. Pivot to other systems within the network

# Instructions

1. This command retrieves information for all servers in the master database.

**Code**: [[select * from master..sysservers]]

> The 'select' statement is used to retrieve data from a database. In this case, the 'master..sysservers' table is queried to retrieve all server information. The 'from' keyword specifies the table to query, and 'master' is the name of the database. The '..' notation is used to specify the default schema for the database. The 'sysservers' table contains information about all servers that are known to the current instance of SQL Server. This command does not take any arguments.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Query Registry|T1012 - Query Registry]]

## Tags

- [[Find Trusted Link]]
- [[Linked Database]]
- [[MSSQL Server]]
