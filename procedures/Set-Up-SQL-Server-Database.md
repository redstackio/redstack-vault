---
tags:
  - database
  - setup
  - sql-server
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.849Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 75ed831f-dbdd-47c2-9392-98f6e94729c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-SQL-Server-Database

## Summary

This procedure details the installation and configuration of SQL Server Express for use with Acronis Cloud Manager, including creating a database user to enable connection during the Acronis setup process.

## Description

SQL Server Express serves as the backend database for the local Acronis Cloud Manager instance. Download and install SQL Server Express and SQL Server Management Studio (SSMS), then configure a database user. During Acronis installation, provide the connection details to integrate the database. This step ensures the full environment is operational for accessing the admin portal and Swagger UI.

## Requirements

1. Windows machine with .NET Framework installed
2. Internet access for downloads from Microsoft
3. Administrative privileges for SQL Server installation

## Defense

Defensive measures and detection strategies:

- Limit SQL Server installations to necessary environments
- Enforce least-privilege for database users
- Monitor for unauthorized database configurations

## Objectives

1. Install and run SQL Server Express
2. Create a dedicated database user for Acronis
3. Successfully connect Acronis to the database

## Instructions

### Step 1: Download and Install SQL Server Express

**Context**: Install the lightweight SQL Server edition suitable for local testing.

Download from https://go.microsoft.com/fwlink/?linkid=866658 and run the installer. Choose basic installation and set up the instance.

### Step 2: Install SQL Server Management Studio

**Context**: Use SSMS to manage the database and create users.

Download from https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15 and install it.

### Step 3: Create Database User and Connect

**Context**: During Acronis setup, provide SQL Server details and create a user via SSMS if needed.

Launch SSMS, connect to the local instance, create a new login/user for the Acronis database, and input these details in the Acronis configuration wizard.

**Expected Output**: Acronis reports successful database connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[database]]
- [[sql-server]]
- [[setup]]
