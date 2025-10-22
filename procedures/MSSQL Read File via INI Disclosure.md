---
id: 8c552990-a92c-4f85-99e0-173f57d298be
name: MSSQL Read File via INI Disclosure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.922224+00:00'
updated_at: '2023-04-10T20:22:42.008363+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL Read file]]'
commands:
- '[[Check if database is in bulk-logged recovery model]]'
- '[[Switch database back to full recovery model]]'
- '[[Switch database to bulk-logged recovery model]]'
---

# MSSQL Read File via INI Disclosure

## Summary

This procedure involves exploiting a vulnerability in MSSQL to read sensitive information from an INI file. An attacker can use a SQL injection vulnerability to execute stored procedures and query system tables to locate the INI file. Once located, an attacker can read the contents of the INI file,

## Description

# Description

This procedure involves exploiting a vulnerability in MSSQL to read sensitive information from an INI file. An attacker can use a SQL injection vulnerability to execute stored procedures and query system tables to locate the INI file. Once located, an attacker can read the contents of the INI file, which may contain sensitive information such as database credentials, server names, and other configuration details. This attack can be used to gain access to additional systems and data within the network.

Technical Explanation: This attack takes advantage of a SQL injection vulnerability to execute stored procedures and query system tables to locate and read the contents of an INI file. An attacker can use the Bulk Data Processing and Bulk Operations Administration commands to execute stored procedures and query system tables to locate the INI file. Once located, the attacker can use the Windows INI File Disclosure command to read the contents of the INI file. This attack can be performed remotely and does not require direct access to the target system.

Business Value: An attacker can use this attack to gain access to sensitive information that can be used to further compromise the network. This information can be used to gain access to additional systems and data within the network, which can result in data theft, financial loss, and damage to the organization's reputation.

## Requirements

1. Access to a vulnerable MSSQL server

1. Knowledge of SQL injection techniques

1. Access to the Bulk Data Processing, Bulk Operations Administration, and Windows INI File Disclosure commands

## Defense

1. Implement input validation to prevent SQL injection vulnerabilities

1. Monitor MSSQL server logs for suspicious activity

1. Restrict access to MSSQL servers to trusted users and systems

## Objectives

1. Locate and read the contents of an INI file

1. Gather sensitive information such as database credentials and server names

# Instructions

1. bulk process command allows for the processing of large amounts of data at once.

**Code**: [[BULK]]

> This command is particularly useful when dealing with large datasets that need to be processed in batches. It allows for the efficient handling of large volumes of data, reducing processing time and increasing overall efficiency. The command takes in multiple arguments, including the size of the batches, the location of the data, and the type of processing to be performed. It is important to note that proper planning and testing should be done before implementing this command to ensure that it is being used effectively and efficiently.

2. Use this command to perform bulk operations on multiple items at once.

**Code**: [[ADMINISTER BULK OPERATIONS]]

> This command allows you to perform actions on multiple items at once, which can save time and effort when dealing with large amounts of data. To use this command, you will need to provide a list of the items you want to perform the action on, as well as the action you want to perform. The specific syntax for this command will depend on the action you want to perform, so refer to the documentation for more information.

3. Use this command to perform bulk operations on your database.

**Code**: [[ADMINISTER DATABASE BULK OPERATIONS]]

> This command is used to execute bulk operations on your database. It can be used to perform tasks such as importing large amounts of data, exporting data, and deleting large amounts of data. The command requires specific arguments to be provided, such as the name of the table or file to be operated on, and the type of operation to be performed. Please refer to the documentation for the specific arguments required for each operation.

**Command** ([[Check if database is in bulk-logged recovery model]]):

```bash
USE master
GO
SELECT [name], [recovery_model_desc] FROM sys.databases WHERE [name] = 'database_name'
```

**Command** ([[Switch database to bulk-logged recovery model]]):

```bash
ALTER DATABASE database_name SET RECOVERY BULK_LOGGED
```

**Command** ([[Switch database back to full recovery model]]):

```bash
ALTER DATABASE database_name SET RECOVERY FULL
```

4. This command is used to disclose the contents of the Windows INI file. It uses the SQL injection technique to execute the OpenRowset function to read the contents of the file. The 'BULK' keyword specifies the file path and the 'SINGLE_CLOB' keyword specifies that the file contents should be returned as a single character large object (CLOB).

**Code**: [[-1 union select null,(select x from OpenRowset(BUL]]

> The 'union select' statement is used to combine the results of two SELECT statements into a single result set. In this case, the first SELECT statement selects null values for the first and third columns, and the second SELECT statement reads the contents of the win.ini file and returns them as a CLOB object. The null values in the first and third columns are used to fill the remaining columns in the result set.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Code Signing|T1116 - Code Signing]]
- [[Query Registry|T1012 - Query Registry]]

## Commands Used

- [[Check if database is in bulk-logged recovery model]]
- [[Switch database back to full recovery model]]
- [[Switch database to bulk-logged recovery model]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL Read file]]
