---
tags:
  - nosql-injection
  - discovery
  - blind-injection
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:20.459Z'
sub_techniques: []
id: 16a56ffa-d87e-43aa-a162-97d66489e12f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Identify-Admin-Users-via-Blind-NoSQL-Injection

## Summary

This procedure uses blind NoSQL injection in the users.list API to identify admin users by injecting $where operators that check for admin roles, inferring presence from response characteristics.

## Description

The 'query' parameter in /api/v1/users.list is unsanitized, allowing MongoDB $where JavaScript execution. An authenticated attacker sends payloads to filter users with 'admin' in roles array, using blind techniques like response length or timing to detect matches without direct output.

## Requirements

1. Authenticated API session
2. Knowledge of MongoDB query structure
3. Script for sending and analyzing requests

## Defense

- Sanitize query parameters to block $where and operators
- Implement query whitelisting or parameterized queries
- Log and alert on anomalous query patterns

## Objectives

1. Locate admin user IDs or usernames
2. Confirm vulnerability presence
3. Prepare for targeted leakage

## Instructions

### Step 1: Craft Injection Payload

**Context**: Build $where to test for admin roles.

**Command** (No direct bash; via script):
Use post_auth_nosqli.py to send {"$where":"this.roles.includes('admin')"} as query.

> Expected: If admins exist, response differs (e.g., user count >0).

### Step 2: Analyze Response

**Context**: Infer admin presence blindly.

**Instructions**: Compare response size/timing for true/false branches.

> Expected: Admin identified if oracle confirms match.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- nosql-injection
- admin-discovery
