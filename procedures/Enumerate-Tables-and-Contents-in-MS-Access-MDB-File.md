---
type: procedure
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
sub_techniques: []
tags:
  - data-exposure
  - database-enumeration
platforms:
  - Windows
commands:
  - '[[commands/mdb-tables-List-Tables-in-MDB-Database]]'
  - '[[commands/mdb-export-Export-Contents-of-MDB-Table]]'
tools:
  - '[[tools/mdbtools]]'
skill_level: beginner
impact_level: medium
detection_risk: low
verified: true
validated: true
---

# Enumerate-Tables-and-Contents-in-MS-Access-MDB-File

## Summary

This procedure outlines how to list all tables within a Microsoft Access .mdb database file and export the contents of specific tables in CSV format using the mdbtools suite. It is particularly useful in post-exploitation scenarios where attackers have obtained access to legacy Windows systems storing sensitive data, such as user credentials or configuration details, in Access databases.

## Description

Microsoft Access databases in the .mdb format are commonly used in older Windows environments for storing structured data like employee records, passwords, or application configurations. Without Microsoft Access installed, extracting this data requires specialized tools like mdbtools, an open-source library and set of utilities for parsing .mdb files on Linux systems. This procedure assumes the attacker has copied the .mdb file from a compromised Windows host to a Linux attack machine (e.g., Kali). The process involves first enumerating table names to identify relevant data structures, then exporting table contents for analysis. This technique aligns with data collection tactics, enabling the exfiltration of local system information without triggering proprietary software dependencies.

## Requirements

1. Local access to the .mdb database file (e.g., obtained via file transfer from a compromised Windows system).
2. mdbtools package installed on a Linux system (e.g., Kali or Ubuntu).
3. Bash shell environment for executing the commands.
4. Basic file permissions to read the .mdb file.

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive .mdb files using tools like BitLocker or database-level encryption to prevent offline parsing.
- Implement file access monitoring with tools like Windows Sysmon or Linux auditd to detect unauthorized copying or access to database files.
- Use modern database formats (e.g., SQL Server) that are harder to parse without credentials.
- Scan for mdbtools processes or related network transfers of .mdb files in endpoint detection systems.

## Objectives

1. Identify all tables within the .mdb file to scope potential data sources.
2. Extract readable contents from targeted tables for further analysis or exfiltration.
3. Verify successful data retrieval without corrupting the original file.

## Instructions

### Step 1: List All Tables in the Database

**Context**: Begin by using the mdb-tables command to enumerate all table names in the .mdb file. This step reveals the database schema, helping identify tables that may contain valuable information like user accounts or credentials. The -1 flag ensures output is one table per line for easy parsing.

**Command** ([[commands/mdb-tables-List-Tables-in-MDB-Database]]):
```bash
mdb-tables -1 $_MDB_FILE
```

> This command reads the .mdb file's metadata and lists table names without altering the file. Review the output to select tables of interest, such as 'users' or 'accounts'. If the file is password-protected, this step will fail, requiring additional cracking techniques.

### Step 2: Export Contents of a Specific Table

**Context**: Once tables are identified, use mdb-export to dump the contents of a chosen table into CSV format. This allows offline analysis of records, such as searching for plaintext passwords or sensitive data. Repeat for multiple tables as needed.

**Command** ([[commands/mdb-export-Export-Contents-of-MDB-Table]]):
```bash
mdb-export $_MDB_FILE $_TABLE_NAME
```

> The command exports the table data as comma-separated values, handling quoted fields appropriately. Pipe the output to a file (e.g., `> output.csv`) for persistence. Success is indicated by structured data output; errors may occur if the table contains binary fields or if the file is corrupted.
