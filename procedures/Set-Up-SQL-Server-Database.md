---
id: proc-sql-setup-001
tags:
  - database
  - sql-server
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:16:25.458Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Set-Up-SQL-Server-Database

## Summary

This procedure sets up a SQL Server Express database instance and configures it for use with Acronis Cloud Manager, enabling full functionality of the admin portal for vulnerability exploitation testing.

## Description

SQL Server serves as the backend for Acronis Cloud Manager. This setup involves installing SQL Server Express and Management Studio, creating a user, and linking it to Acronis per the setup guide. This prepares the environment for accessing Swagger UI where XSS can be exploited.

## Requirements

1. Windows OS
2. Internet for downloads
3. Administrative privileges

## Defense

Defensive measures and detection strategies:

- Use least privilege for database users
- Enable SQL Server auditing for connection attempts
- Regularly patch SQL Server to prevent related exploits

## Objectives

1. Install and configure SQL Server
2. Create necessary user for Acronis
3. Verify connectivity

## Instructions

### Step 1: Download and Install SQL Server Express

**Context**: Install the database engine.

Download from https://go.microsoft.com/fwlink/?linkid=866658 and run the installer, selecting Express edition with default settings.

### Step 2: Install SQL Server Management Studio

**Context**: Install the management tool.

Download from https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15 and install.

### Step 3: Create User and Configure

**Context**: Set up database user as per Acronis guide.

Open SSMS, connect to the server, create a new login user with necessary permissions, and update Acronis configuration to use this connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- database
- sql-server
- setup
