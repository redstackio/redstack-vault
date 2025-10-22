---
id: c68b06d5-fae1-44db-b7e6-cc23958b2ac4
name: SQL Stored Procedures
type: sub-technique
mitre_id: T1505.001
mitre_url: null
created_at: '2023-04-06T00:31:27.226527+00:00'
updated_at: '2023-04-06T00:31:27.226527+00:00'
parent_technique: '[[Server Software Component|T1505 - Server Software Component]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# SQL Stored Procedures

**MITRE ID**: T1505.001

**Parent Technique**: [[Server Software Component|T1505 - Server Software Component]]

This is a sub-technique of T1505 - Server Software Component.

## Summary

Adversaries may abuse SQL stored procedures to establish persistent access to systems. SQL Stored Procedures are code that can be saved and reused so that database users do not waste time rewriting frequently used SQL queries. Stored procedures can be invoked via SQL statements to the database using

## Description

Adversaries may abuse SQL stored procedures to establish persistent access to systems. SQL Stored Procedures are code that can be saved and reused so that database users do not waste time rewriting frequently used SQL queries. Stored procedures can be invoked via SQL statements to the database using the procedure name or via defined events (e.g. when a SQL server application is started/restarted).

Adversaries may craft malicious stored procedures that can provide a persistence mechanism in SQL database servers.(Citation: NetSPI Startup Stored Procedures)(Citation: Kaspersky MSSQL Aug 2019) To execute operating system commands through SQL syntax the adversary may have to enable additional functionality, such as xp_cmdshell for MSSQL Server.(Citation: NetSPI Startup Stored Procedures)(Citation: Kaspersky MSSQL Aug 2019)(Citation: Microsoft xp_cmdshell 2017) 

Microsoft SQL Server can enable common language runtime (CLR) integration. With CLR integration enabled, application developers can write stored procedures using any .NET framework language (e.g. VB .NET, C#, etc.).(Citation: Microsoft CLR Integration 2017) Adversaries may craft or modify CLR assemblies that are linked to stored procedures since these CLR assemblies can be made to execute arbitrary commands.(Citation: NetSPI SQL Server CLR) 

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
