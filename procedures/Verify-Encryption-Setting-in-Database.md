---
tags:
  - database-query
  - verification
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/sql-query-nextcloud-encryption-setting]]'
verified: false
platforms:
  - Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:27:49.432Z'
skill_level: beginner
impact_level: low
detection_risk: high
sub_techniques: []
id: e6da2c20-a982-4a85-8c1c-bdda7fb1e60a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Verify-Encryption-Setting-in-Database

## Summary

This procedure queries the Nextcloud database to confirm changes to the encryption_enabled configuration after CSRF exploitation.

## Description

Nextcloud stores app configurations in the oc_appconfig table. This SQL query filters for the core app's encryption_enabled key to retrieve its value, verifying if the exploit succeeded. It assumes MySQL-like access and requires database credentials. Expected outcome: Row showing updated configvalue ('yes' or 'no').

## Requirements

1. Database access to Nextcloud's backend (e.g., MySQL)
2. SQL client or direct query capability
3. Knowledge of table structure (oc_appconfig)

## Defense

Defensive measures and detection strategies:

- Restrict database query access to admins
- Log all SELECT queries on config tables
- Use read-only views for verification
- Integrate with SIEM for anomalous config queries

## Objectives

1. Query oc_appconfig for encryption setting
2. Confirm exploit impact
3. Validate persistence of change

## Instructions

### Step 1: Connect to Database

**Context**: Access the Nextcloud database.

**Command** (Connection):
Use a SQL client to connect (e.g., mysql -u user -p dbname).

> Ensure connection to the correct instance.

### Step 2: Execute Query

**Context**: Retrieve the specific config value.

**Command** ([[commands/sql-query-nextcloud-encryption-setting]]):
```sql
select * from oc_appconfig where appid='core' and configkey='encryption_enabled';
```

> This returns appid, configkey, and configvalue; check if value matches the exploit (e.g., 'no' after disable).

### Step 3: Interpret Results

**Context**: Analyze the output for success.

**Command** (No command; review results):

> Success if configvalue changed; failure if unchanged.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/sql-query-nextcloud-encryption-setting]]

## Tools Used


## Tags

- [[database-query]]
- [[verification]]
- [[nextcloud]]
