---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - login
  - session
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.323Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-In-as-Victim-User

## Summary

Authenticate the victim account in a separate session to establish the context for iframe execution.

## Description

Use incognito mode to log in as the author/subscriber, ensuring the session is active when the malicious post is visited.

## Requirements

1. Victim credentials
2. Separate browser session

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication
- Monitor login patterns

## Objectives

1. Active victim session
2. No interference with attacker session

## Instructions

### Step 1: Open Incognito

**Context**: Isolate session.

Launch incognito browser.

### Step 2: Log In

**Context**: Authenticate victim.

Enter credentials at /wp-login.php.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login]]
- [[session]]
