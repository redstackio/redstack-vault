---
id: uuid-2
tags:
  - hive
  - connection
  - unauthenticated
type: procedure
tools:
  - '[[tools/java]]'
  - '[[tools/Hive-JDBC]]'
  - '[[tools/DataGrip]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/java-queryhive-select1]]'
verified: false
platforms:
  - Linux
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.642Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Connect-to-Open-Apache-Hive-Database

## Summary

This procedure establishes an unauthenticated JDBC connection to a publicly exposed Apache Hive server on port 10000, verifying access with a simple query to confirm the database is reachable and exploitable.

## Description

The vulnerability stems from a misconfigured Hive server in Evernote's GCP non-production environment, accessible without credentials. Using a compatible JDBC client, connect via URI jdbc:hive2://IP:10000 with username 'hive' and empty password. This grants full query execution rights, setting the stage for XXE injection.

## Requirements

1. Configured Hive JDBC 1.1.0 client
2. Public IP of the Hive server
3. Java runtime with classpath including Hive JARs

## Defense

Defensive measures and detection strategies:

- Implement IP whitelisting and authentication (e.g., Kerberos for Hive)
- Use GCP Security Groups to block port 10000 externally
- Log and alert on anomalous database connections

## Objectives

1. Gain initial access to the database
2. Validate query execution capabilities
3. Confirm no authentication barriers

## Instructions

### Step 1: Execute Test Connection

**Context**: Run a basic SELECT query to test connectivity and protocol compatibility.

**Command** ([[commands/java-queryhive-select1]]):
```bash
java -classpath '.:./runtime/*' QueryHive IP:10000 "SELECT 1"
```

> The command uses the compiled QueryHive class, specifying the server IP:10000 and a simple SQL query. Expected output is the value 1, indicating successful connection.

### Step 2: Verify in DataGrip

**Context**: Alternative GUI verification.

**Instructions**: In DataGrip, create a new connection with the JDBC URI, test with SELECT 1, and confirm no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/java-queryhive-select1]]

## Tools Used

- [[tools/java]]
- [[tools/Hive-JDBC]]
- [[tools/DataGrip]]

## Tags

- [[hive]]
- [[connection]]
- [[unauthenticated]]
