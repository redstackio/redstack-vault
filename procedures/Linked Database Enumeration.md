---
id: 5886866f-af95-4e00-bda7-ed592016d34c
name: Linked Database Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.153989+00:00'
updated_at: '2023-04-10T20:36:32.460016+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Determine Names of Linked Databases]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
---

# Linked Database Enumeration

## Summary

Linked databases in MSSQL Server allow for communication between different databases, potentially across different servers. This procedure aims to enumerate the names of linked databases on a target MSSQL Server. An attacker could use this information to map out the network architecture and identif

## Description

# Description

Linked databases in MSSQL Server allow for communication between different databases, potentially across different servers. This procedure aims to enumerate the names of linked databases on a target MSSQL Server. An attacker could use this information to map out the network architecture and identify high-value databases to target. 

To determine the names of linked databases, the 'Get-DatabaseNames' command can be used. This command queries the target server for a list of database names that are linked to the current database. 

The business value of this procedure is that it allows for an attacker to gain a better understanding of the target's network architecture and identify potential targets for further exploitation.

## Requirements

1. Access to the target MSSQL Server.

1. Credentials with sufficient privileges to run the 'Get-DatabaseNames' command.

## Defense

1. Ensure that MSSQL Server is configured securely and unnecessary linked databases are removed.

1. Implement network segmentation to limit the potential impact of an attacker who gains access to a linked database.

1. Monitor MSSQL Server logs for suspicious activity, such as failed login attempts or unusual queries.

## Objectives

1. Enumerate the names of linked databases on the target MSSQL Server.

1. Map out the network architecture of the target.

1. Identify high-value databases to target for further exploitation.

# Instructions

1. This command retrieves the names of all databases on the specified SQL server instance.

**Code**: [[Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>"]]

> The 'Get-SQLQuery' command is used to execute a SQL query against a specified SQL server instance. The '-Instance' parameter is used to specify the name of the SQL server instance. The '-Query' parameter is used to specify the SQL query to execute. In this case, the query retrieves the names of all databases on the server using the 'openquery' function. The '-Verbose' parameter is used to display detailed information about the execution of the command. This command can be useful for retrieving a list of all databases on a server for administrative purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Tags

- [[Determine Names of Linked Databases]]
- [[Linked Database]]
- [[MSSQL Server]]
