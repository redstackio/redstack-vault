---
tags:
  - invitation
  - role-assignment
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
updated_at: '2025-12-14T17:25:23.056Z'
sub_techniques: []
id: f48fa8c2-ccb8-44d8-a178-9ca9572182ab
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Attacker-as-Member

## Summary

Invite the attacker account to the organization as a 'Member' to gain limited access for IDOR testing.

## Description

From the victim session, use the organization members page to invite the attacker email and assign the Member role, which lacks API key management permissions but allows IDOR bypass.

## Requirements

1. Victim logged in with organization access
2. Attacker email available
3. ORG-UUID known

## Defense

Defensive measures and detection strategies:

- Audit invitation logs for unusual patterns
- Require approval workflows for member additions
- Limit invitations to verified domains

## Objectives

1. Add attacker with minimal privileges
2. Confirm role assignment
3. Prepare for authorization testing

## Instructions

### Step 1: Access Members Page

**Context**: Navigate to invitation interface.

Log in as victim, go to https://target-platform.com/organization/ORG-UUID/members.

> Expected: Members list loads.

### Step 2: Send Invitation

**Context**: Assign limited role to attacker.

Enter attacker email, select 'Member' role, and submit invitation.

> Expected: Email sent; attacker can accept.

### Step 3: Accept as Attacker

**Context**: Join organization.

Log in as attacker, check email, and accept invitation.

> Expected: Attacker appears in members list as Member.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- invitation
- role-assignment
