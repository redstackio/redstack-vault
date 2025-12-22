---
tags:
  - mysql
  - setup
type: procedure
tools:
  - '[[tools/MySQL]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.722Z'
sub_techniques: []
id: ca239744-48e5-4525-9ce2-71594b2efd5c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Attacker-MySQL-Server

## Summary

This procedure sets up an attacker-controlled MySQL server to receive exfiltrated data from the LFI exploit in Infogram, including creating the necessary database and table.

## Description

In the context of exploiting LFI via Infogram's MySQL connection, this procedure prepares a remote MySQL instance that the Infogram server will connect to. The server acts as a receiver for the file contents loaded via LOAD DATA LOCAL INFILE. Prerequisites include a Linux host with MySQL installed and public accessibility on port 3306. Expected outcome is a ready-to-receive database structure.

## Requirements

1. Linux server with root access
2. MySQL server installed (e.g., via apt install mysql-server)
3. Firewall configured to allow inbound TCP 3306
4. Public IP address reachable from the internet

## Defense

Defensive measures and detection strategies:

- Disable LOAD DATA LOCAL INFILE on client-side MySQL configurations
- Monitor outbound MySQL connections from application servers to unknown hosts
- Use WAF rules to block suspicious SQL queries in data import features

## Objectives

1. Establish a controlled MySQL endpoint for data reception
2. Create database 'asd' and table 'asd' to match the exploit query
3. Ensure the server authenticates incoming connections from Infogram

## Instructions

### Step 1: Install and Start MySQL

**Context**: Ensure MySQL is running and accessible.

**Command** (MySQL Start):
```bash
sudo systemctl start mysql
sudo systemctl enable mysql
```

> Starts the MySQL service and sets it to auto-start. Expected output: Service active (running).

### Step 2: Create Database and Table

**Context**: Set up the target database and table for the LOAD DATA command.

**Command** (MySQL Admin):
```sql
CREATE DATABASE asd;
USE asd;
CREATE TABLE asd (data TEXT);
```

> Run these in the MySQL client (mysql -u root -p). Expected output: Database and table created successfully.

### Step 3: Configure User Access

**Context**: Create a user for the Infogram connection.

**Command** (MySQL User Create):
```sql
CREATE USER 'attacker'@'%' IDENTIFIED BY 'password';
GRANT ALL ON asd.* TO 'attacker'@'%';
FLUSH PRIVILEGES;
```

> Grants necessary permissions. Expected output: User created and privileges applied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/MySQL]]

## Tags

- mysql
- setup
