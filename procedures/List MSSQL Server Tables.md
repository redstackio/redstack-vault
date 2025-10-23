---
id: 43b74816-fae8-4a0d-8c00-aefaf38b3dec
name: List MSSQL Server Tables
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.800163+00:00'
updated_at: '2023-04-10T20:36:32.814207+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[List all tables]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
---

# List MSSQL Server Tables

## Summary

This procedure enables the user to manually query a MSSQL server to retrieve a list of all tables within the database. This can be useful for discovering sensitive data or identifying potential targets for further exploitation. To execute this procedure, the user must have valid credentials and acc

## Description

# Description

This procedure enables the user to manually query a MSSQL server to retrieve a list of all tables within the database. This can be useful for discovering sensitive data or identifying potential targets for further exploitation. To execute this procedure, the user must have valid credentials and access to the MSSQL server.

 

## Requirements

1. Valid credentials for the MSSQL server

1. Access to the MSSQL server

 

## Defense

1. Restrict user access to MSSQL servers to only those who require it

1. Implement strong password policies and multi-factor authentication for MSSQL server access

1. Monitor MSSQL server logs for suspicious activity

 

## Objectives

1. Enumerate all tables within a MSSQL database

 

# Instructions

1. To get the names of all the tables in the current database, execute the following SQL command:

 



**Code**: [[select table_name from information_schema.tables]]



> This command retrieves the names of all the tables in the current database from the 'information_schema.tables' table. The 'table_name' column contains the names of the tables.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[List all tables]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]


