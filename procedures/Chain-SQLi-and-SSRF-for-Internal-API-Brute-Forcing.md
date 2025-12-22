---
id: proc-uuid-11
tags:
  - sqli
  - ssrf
  - bruteforce
type: procedure
tools:
  - '[[tools/Curl]]'
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sqli-schema-dump]]'
  - '[[commands/python-brute-credentials]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:55.505Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1190.003]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Application Access Token]]'
---
# Chain-SQLi-and-SSRF-for-Internal-API-Brute-Forcing

## Summary

This procedure chains SQL injection in the album hash parameter with SSRF in the picture endpoint to access localhost API, then brute-forces credentials using non-404 responses to gain login and flag.

## Description

SQLi in /r3c0n_server_4fdk59/album?hash= allows schema dump; SSRF fetches internal http://localhost/api/user. Brute usernames/passwords via response diffs. Targets recon servers with MySQL.

## Requirements

1. SQLi payload knowledge
2. Python brute script
3. Access to hidden directory

## Defense

Defensive measures and detection strategies:

- Parameterize SQL queries
- Validate SSRF URLs (no localhost)
- Auth internal APIs

## Objectives

1. Dump DB schema
2. SSRF to internal services
3. Brute-force creds

## Instructions

### Step 1: SQLi Schema Dump

**Context**: Enumerate tables/columns.

**Command** ([[commands/curl-sqli-schema-dump]]):
```bash
curl -s 'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd' UNION SELECT 1,2,group_concat(concat(table_name,':',column_name)) from information_schema.columns WHERE table_schema='recon';/*'
```

> Lists structure for further exploits.

### Step 2: Exploit SSRF

**Context**: Use SQLi to set image path to internal API.

Inject UNION SELECT to fetch http://localhost/api/user via picture?data=.

### Step 3: Brute Credentials

**Context**: Script SSRF responses for brute.

**Command** ([[commands/python-brute-credentials]]):
```bash
./brute.py
```

> Finds 'grinchadmin': 's4nt4sucks' via non-404.

### Step 4: Login

**Context**: Use creds for API access.

Flag retrieved.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Application Access Token]] Steal Application Access Token (via SSRF)

### Sub-Techniques

- [[T1190.003]] SQLi

## Commands Used

- [[commands/curl-sqli-schema-dump]]
- [[commands/python-brute-credentials]]

## Tools Used

- [[tools/Curl]]
- [[tools/Python]]

## Tags

- [[sqli]]
- [[ssrf]]
- [[bruteforce]]
