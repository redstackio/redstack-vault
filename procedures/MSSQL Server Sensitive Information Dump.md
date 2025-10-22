---
id: 5df072de-e895-43df-9c17-62101bbc5771
name: MSSQL Server Sensitive Information Dump
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.997054+00:00'
updated_at: '2023-04-10T20:36:31.050161+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Dump common information from server to files]]'
- '[[Identify Sensitive Information]]'
- '[[MSSQL Server]]'
---

# MSSQL Server Sensitive Information Dump

## Summary

The MSSQL Server Sensitive Information Dump procedure is used to identify and extract sensitive information from a target MSSQL server. This procedure leverages the SQL Dump Info command to extract common information from the server and write it to files. This information can include usernames, pas

## Description

# Description

The MSSQL Server Sensitive Information Dump procedure is used to identify and extract sensitive information from a target MSSQL server. This procedure leverages the SQL Dump Info command to extract common information from the server and write it to files. This information can include usernames, passwords, and other sensitive data that can be used to further compromise the target.

From a technical standpoint, this procedure utilizes SQL queries to extract information from the target MSSQL server. This information is then written to files on the attacker's machine. The business value of this procedure is that it can provide valuable information for further attacks, such as password spraying or credential stuffing.

## Requirements

1. Valid credentials for the target MSSQL server

1. Network access to the target MSSQL server

1. SQL Dump Info command

## Defense

1. Ensure strong and complex passwords are used for all MSSQL server accounts

1. Limit network access to the MSSQL server to only necessary users and systems

1. Monitor MSSQL server logs for any suspicious activity, such as failed login attempts

## Objectives

1. Identify sensitive information on the target MSSQL server

1. Extract usernames and passwords for further attacks

# Instructions

1. This command is used to retrieve information about SQL Server dump files. It can be used to analyze the contents of a dump file and provide insights into the cause of a SQL Server crash. The -Verbose switch is used to provide detailed information about the dump file analysis. The -Instance parameter specifies the SQL Server instance to analyze, and the -csv switch is used to output the results in CSV format.

**Code**: [[Invoke-SQLDumpInfo -Verbose -Instance SQLSERVER1\I]]

> -Verbose: Provides detailed information about the dump file analysis.
-Instance: Specifies the SQL Server instance to analyze.
-csv: Outputs the results in CSV format.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[Dump common information from server to files]]
- [[Identify Sensitive Information]]
- [[MSSQL Server]]
