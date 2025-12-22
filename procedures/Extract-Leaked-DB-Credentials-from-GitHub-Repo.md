---
id: proc-uuid-8
tags:
  - credential-leak
  - github
  - md5-crack
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:55.516Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Leaked-DB-Credentials-from-GitHub-Repo

## Summary

This procedure recovers accidentally committed database credentials from a GitHub repository's commit history for the forum software, uses them to access phpMyAdmin, extracts MD5 hashes, and cracks them to log in as admin and view the flag post.

## Description

Source code repos often leak creds in history; search commits for config files with DB details. Access phpMyAdmin, dump users table, crack MD5 (e.g., 'grinch' -> 'BahHumbug' via Google). Targets MySQL-backed PHP forums.

## Requirements

1. GitHub access to repo
2. phpMyAdmin login
3. MD5 rainbow tables or search

## Defense

Defensive measures and detection strategies:

- .gitignore sensitive files
- Scrub repo history before public
- Use env vars for creds

## Objectives

1. Recover leaked secrets
2. Access backend DB
3. Gain admin forum access

## Instructions

### Step 1: Search Repo History

**Context**: Browse GitHub commits for config leaks.

Manually search forum software repo for DB creds in files like config.php.

> Note username/password for phpMyAdmin.

### Step 2: Access and Dump Hashes

**Context**: Log into phpMyAdmin, query users table.

Execute SELECT * FROM users; extract MD5 for grinch.

### Step 3: Crack and Login

**Context**: Search hash online.

Google MD5 hash; login to forum as grinch:BahHumbug, view admin post flag.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[credential-leak]]
- [[github]]
- [[md5-crack]]
