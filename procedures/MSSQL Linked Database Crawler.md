---
id: 6980badd-b176-40c6-9514-5a49d01d5922
name: MSSQL Linked Database Crawler
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.091498+00:00'
updated_at: '2023-04-10T20:36:31.401982+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Network Sniffing|T1040 - Network Sniffing]]'
tags:
- '[[Crawl Links for a Specific Instance]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
---

# MSSQL Linked Database Crawler

## Summary

The MSSQL Linked Database Crawler is a tool used for discovering linked databases in a specific MSSQL instance. This tool can be used by an attacker to identify other databases that are linked to the target database. The crawler works by querying the MSSQL instance for all linked databases and then

## Description

# Description

The MSSQL Linked Database Crawler is a tool used for discovering linked databases in a specific MSSQL instance. This tool can be used by an attacker to identify other databases that are linked to the target database. The crawler works by querying the MSSQL instance for all linked databases and then crawling through each linked database to find additional links. This tool can be useful for lateral movement within a network and for identifying high value targets. 

From a technical perspective, the crawler uses SQL queries to retrieve information about linked databases from the sys.servers system catalog view. It then uses this information to connect to each linked database and crawl through all of its objects to find additional linked databases. 

The business value of this tool is that it can help organizations identify potential security risks in their MSSQL environment. By using this tool, organizations can proactively identify and address any misconfigured linked databases that may be vulnerable to attack.

## Requirements

1. Access to a MSSQL instance

1. Credentials with sufficient privileges to query and crawl linked databases

## Defense

1. Regularly review and audit linked databases to ensure they are properly configured and secured

1. Implement strict access controls and permissions for linked databases

1. Monitor network traffic for any unusual activity related to linked databases

## Objectives

1. Identify linked databases in a specific MSSQL instance

1. Discover additional linked databases through crawling

1. Assist in lateral movement within a network

# Instructions

1. This command retrieves information about linked servers in SQL Server. It uses the Get-SQLServerLinkCrawl cmdlet with the -Instance parameter to specify the SQL Server instance to crawl. The command then executes a SQL query using the openquery function to retrieve information about linked servers from the master..sysservers table. The query is executed on the specified instance and then on a linked server within that instance.

**Code**: [[Get-SQLServerLinkCrawl -Instance "<DBSERVERNAME\DB]]

> The -Instance parameter specifies the SQL Server instance to crawl. The openquery function is used to execute a query on a linked server. The first argument of the openquery function specifies the linked server to execute the query on, and the second argument is the query to execute. In this case, the query is retrieving information about linked servers from the master..sysservers table. The double quotes within the query are escaped with two single quotes. The -Verbose parameter provides detailed output about the crawling process.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Network Sniffing|T1040 - Network Sniffing]]

## Tags

- [[Crawl Links for a Specific Instance]]
- [[Linked Database]]
- [[MSSQL Server]]
