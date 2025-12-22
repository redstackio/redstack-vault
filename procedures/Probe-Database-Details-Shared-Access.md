---
id: proc-uuid-5
tags:
  - sqli
  - shared-db
  - pii
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/sql-shell-probe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T03:46:14.962Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Probe Database Details and Confirm Shared Access

## Summary

This procedure uses sqlmap's SQL shell to query system variables and confirm shared database access across subdomains, highlighting architecture flaws.

## Description

After enumeration, the SQL shell allows interactive queries. Probes reveal hostname, user, etc.; cross-subdomain sharing (e.g., with #311922) amplifies risk to PII and site compromise.

## Requirements

1. sqlmap session active from prior step
2. Knowledge of target system variables
3. Report IDs for correlation

## Defense

Defensive measures and detection strategies:

- Implement database isolation per subdomain
- Audit shared access privileges
- Monitor for shell-like query patterns

## Objectives

1. Extract system metadata
2. Verify shared DB exposure
3. Assess escalation potential

## Instructions

### Step 1: Launch SQL Shell and Probe

**Context**: Enter sqlmap SQL shell and run queries for variables.

**Command** ([[commands/sql-shell-probe]]):
```bash
# In sqlmap: --sql-shell
# Then: SELECT user(); SELECT @@version; SELECT @@basedir; SELECT @@port; SELECT @@hostname;
```

> Outputs 'ntmsender'@'localhost', '5.6.36', '███████', etc.; confirm sharing via db names.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/sql-shell-probe]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- shared-db
