---
id: 6cb4f1f4-ae5c-4937-bc1f-d88be48ff77b
name: Linked Database Crawling for MSSQL Server Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.070542+00:00'
updated_at: '2023-04-10T20:36:32.104156+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Crawl Links for Instances in the Domain]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
---

# Linked Database Crawling for MSSQL Server Enumeration

## Summary

Linked databases are a method of connecting two databases on different servers. This procedure involves crawling links to identify instances of MSSQL Server that are linked to a database on another server. This can be useful for identifying potential targets for lateral movement or privilege escala

## Description

# Description

Linked databases are a method of connecting two databases on different servers. This procedure involves crawling links to identify instances of MSSQL Server that are linked to a database on another server. This can be useful for identifying potential targets for lateral movement or privilege escalation. To execute this procedure, the user will need to identify the SQL Server link and crawl the links to enumerate the instances in the domain. This can be done using various tools and techniques. The result of this procedure will be a list of MSSQL Server instances that are linked to databases on other servers.

 

## Requirements

1. Authenticated access to the domain.

1. Access to tools for crawling links and enumerating instances of MSSQL Server.

 

## Defense

1. Ensure that MSSQL Server instances are not linked to databases on other servers unnecessarily.

1. Implement network segmentation to limit lateral movement.

1. Monitor network traffic for suspicious activity related to MSSQL Server link crawling.

 

## Objectives

1. Identify potential targets for lateral movement or privilege escalation.

1. Enumerate instances of MSSQL Server linked to databases on other servers.

 

# Instructions

1. This command retrieves information about SQL Server links and identifies valid links based on the DatabaseLinkName field in the results.

 



**Code**: [[Get-SQLInstanceDomain | Get-SQLServerLink -Verbose]]



> The 'Get-SQLInstanceDomain' command retrieves information about the SQL Server instances in the current domain. The 'Get-SQLServerLink' command is then used to retrieve information about SQL Server links for each of these instances. The command is run with the '-Verbose' parameter to provide detailed output. The 'select' statement at the end of the 'data' field is used to query the 'sysservers' table in the 'master' database to retrieve additional information about the SQL Server links. The 'text' field provides information about how to identify a valid SQL Server link based on the 'DatabaseLinkName' field in the results.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Tags

- [[Crawl Links for Instances in the Domain]]
- [[Linked Database]]
- [[MSSQL Server]]


