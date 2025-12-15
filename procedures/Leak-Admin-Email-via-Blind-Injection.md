---
tags:
  - data-leakage
  - blind-injection
  - email-exfil
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:32:20.455Z'
sub_techniques: []
id: 2af63972-7b85-490c-81f1-008418953a12
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Leak-Admin-Email-via-Blind-Injection

## Summary

This procedure extracts an admin's email address character-by-character using blind NoSQL injection oracles in the users.list endpoint, combining role checks with regex tests on the emails field.

## Description

Building on admin identification, the attacker crafts $where payloads that test email prefixes/suffixes with JavaScript regex (e.g., /^a/.test(this.emails[0].address)). Response differences allow guessing each character, reconstructing the full email for targeted attacks like password resets.

## Requirements

1. Known admin role filter
2. Script implementing boolean-based blind injection
3. Patience for iterative requests (26-100+ per email)

## Defense

- Disable $where operator in MongoDB config
- Use aggregation pipelines instead of raw queries
- Rate-limit API queries and monitor for repetitive patterns

## Objectives

1. Obtain admin contact email
2. Enable social engineering or reset attacks
3. Escalate to credential access

## Instructions

### Step 1: Initialize Oracle for Email

**Context**: Target the first email address of admin users.

**Instructions**: Send payload {"$where":"this.roles.includes('admin') && /^.test(this.emails[0].address)"} replacing . with guessed char.

> Expected: True response (e.g., different JSON length) confirms char.

### Step 2: Iterate and Reconstruct

**Context**: Guess full string position by position.

**Instructions**: Script automates from length detection to char enumeration.

> Expected: Complete email like 'admin@target.com'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data from Local System]] Data from Local System (adapted for DB)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- blind-leakage
- email
