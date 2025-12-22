---
id: proc-extract-key-005
tags:
  - auth-bypass
  - exfiltration
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sql-query-ithemes-cache]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T03:15:09.999Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Extract-iThemes-Sync-Auth-Key

## Summary

This procedure queries the wp_options table via SQLi to retrieve the plaintext iThemes-Sync authentication key and associated user ID.

## Description

iThemes-Sync stores cache data in wp_options with option_name='ithemes-sync-cache', containing serialized auth details. Using the ongoing SQLi, execute a SELECT to dump this, enabling hash computation for requests. This pivots from data exfil to privilege escalation.

## Requirements

1. Active SQLi session via sqlmap
2. Knowledge of wp_options table structure

## Defense

Defensive measures and detection strategies:

- Encrypt or hash stored keys instead of plaintext
- Rotate keys periodically and monitor option table access
- Remove unused plugins like iThemes-Sync

## Objectives

1. Retrieve serialized auth data
2. Extract key and user_id
3. Enable iThemes-Sync exploitation

## Instructions

### Step 1: Query Options Table

**Context**: Use SQLi to select the specific option_value.

**Command** ([[commands/sql-query-ithemes-cache]]):
```sql
SELECT option_value FROM [REDACTED] WHERE option_name='ithemes-sync-cache'
```

> Run via sqlmap --sql-query; output is PHP-serialized array with key, timestamp, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/sql-query-ithemes-cache]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- auth-bypass
- exfiltration
