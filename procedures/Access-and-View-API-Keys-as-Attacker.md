---
tags:
  - idor-read
  - credential-discovery
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
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.045Z'
sub_techniques: []
id: 3e2a1850-9bab-4bb6-843e-f62cafa62205
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Access-and-View-API-Keys-as-Attacker

## Summary

Use the attacker's member session to unauthorizedly view private API keys, exploiting IDOR.

## Description

Directly access the API keys endpoint with the ORG-UUID in the attacker's browser session, bypassing role-based checks to reveal sensitive keys.

## Requirements

1. Attacker logged in as Member
2. ORG-UUID known
3. Valid session cookies

## Defense

Defensive measures and detection strategies:

- Implement object-level authorization (e.g., check user ownership)
- Log access to sensitive endpoints
- Use session-based permission enforcement

## Objectives

1. View all organization API keys
2. Copy target API-UUID
3. Confirm IDOR read vulnerability

## Instructions

### Step 1: Log In as Attacker

**Context**: Establish limited session.

Navigate to login and authenticate as attacker.

> Expected: Dashboard without full admin access.

### Step 2: Access Endpoint

**Context**: Trigger IDOR read.

Go to https://target-platform.com/organization/ORG-UUID/apiKeys.

> Expected: Full list of private keys displayed.

### Step 3: Extract UUID

**Context**: Prepare for manipulation.

Inspect the page or network tab to copy an API key's UUID.

> Expected: UUID like 'api-12345' obtained.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor-read
- credential-discovery
