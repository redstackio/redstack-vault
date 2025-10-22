---
id: 6c1cbd71-0f33-45d2-876a-94a25101001a
name: Identify Sensitive Information in MSSQL Server Columns
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.944498+00:00'
updated_at: '2023-04-10T20:36:34.212883+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Gather 5 Entries from Each Column]]'
- '[[Identify Sensitive Information]]'
- '[[MSSQL Server]]'
---

# Identify Sensitive Information in MSSQL Server Columns

## Summary

This procedure aims to identify sensitive information stored in MSSQL Server columns. By gathering 5 entries from each column, an attacker can gain insight into the types of data being stored and potentially identify sensitive information such as passwords, credit card numbers, or personal identifi

## Description

# Description

This procedure aims to identify sensitive information stored in MSSQL Server columns. By gathering 5 entries from each column, an attacker can gain insight into the types of data being stored and potentially identify sensitive information such as passwords, credit card numbers, or personal identifiable information (PII). This information can be used for further attacks or sold on the black market. 

Technically, this procedure involves querying the MSSQL Server database and retrieving a sample of data from each column in the specified table. The results are then analyzed to identify sensitive information. 

From a business perspective, this procedure highlights the importance of properly securing sensitive data and limiting access to those who need it. A successful attack on this type of data could result in reputational damage, legal ramifications, and financial loss.

## Requirements

1. Access to the MSSQL Server database

1. Proper authentication and authorization

1. SQL querying tool or language knowledge

## Defense

1. Properly secure sensitive data by limiting access and implementing proper access controls

1. Monitor MSSQL Server logs for suspicious activity

1. Regularly review and update MSSQL Server security settings and configurations

## Objectives

1. Identify sensitive information stored in MSSQL Server columns

1. Gain insight into the types of data being stored

1. Potentially identify passwords, credit card numbers, or personal identifiable information (PII)

# Instructions

1. This command retrieves sample data for specified columns in a SQL database. The 'Get-SQLInstanceDomain' cmdlet retrieves information about the SQL instance, and 'Get-SQLColumnSampleData' cmdlet retrieves sample data for specified columns. The '-Keywords' parameter specifies the column names to retrieve data for. The '-Verbose' parameter provides detailed output, and the '-SampleSize' parameter specifies the number of rows to retrieve for each column.

**Code**: [[Get-SQLInstanceDomain | Get-SQLColumnSampleData -K]]

> To use this command, run it in a PowerShell console with the appropriate SQL Server module installed. Replace '<columnname1,columnname2,columnname3,columnname4,columnname5>' with a comma-separated list of the column names you want to retrieve sample data for. The output will include the specified column names and a sample of the data contained in each column.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[Gather 5 Entries from Each Column]]
- [[Identify Sensitive Information]]
- [[MSSQL Server]]
