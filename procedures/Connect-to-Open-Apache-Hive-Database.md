---
tags:
  - hive
  - misconfiguration
  - initial-access
type: procedure
tools:
  - '[[tools/DataGrip]]'
  - '[[tools/Apache-Hive-JDBC-Driver]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/connect-hive-datagrip]]'
platforms:
  - GCP
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: ddba9054-eac9-44ad-bcd2-3b4806abec99
created_at: '2025-12-13T09:00:27.789Z'
updated_at: '2025-12-13T09:00:27.789Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Connect to Open Apache Hive Database

## Summary

This procedure involves connecting to a misconfigured Apache Hive database that is openly accessible without authentication, serving as the entry point for further exploitation such as XXE injection.

## Description

The target Apache Hive database is exposed on port 10000 in a GCP non-production environment. By using a compatible client like DataGrip with a custom Hive JDBC driver, an attacker can establish a connection and execute queries, leading to potential data exposure and chained attacks.

## Requirements

1. Network access to the target IP on port 10000
2. DataGrip or similar database client
3. Custom compiled Hive JDBC driver version 1.1.0

## Defense

Defensive measures and detection strategies:

- Restrict database access with firewalls and authentication
- Monitor for unauthorized connections to port 10000

## Objectives

1. Establish unauthorized connection to Hive database
2. Verify ability to execute queries
3. Prepare for injection attacks

## Instructions

### Step 1: Set Up Client and Connect

**Context**: Configure the database client and connect to the open Hive instance.

**Command** ([[commands/connect-hive-datagrip]]):
```bash
# Use DataGrip to connect to ██████████:10000 with custom Hive JDBC driver
```

> This establishes a connection without credentials, allowing query execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/connect-hive-datagrip]]

## Tools Used

- [[tools/DataGrip]]
- [[tools/Apache-Hive-JDBC-Driver]]

## Tags

- [[hive]]
- [[misconfiguration]]
- [[initial-access]]
