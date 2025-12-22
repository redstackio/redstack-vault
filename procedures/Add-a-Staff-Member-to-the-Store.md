---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - shopify
  - user-management
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:49.430Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add-a-Staff-Member-to-the-Store

## Summary

This procedure details adding a staff member to a Shopify store, enabling the introduction of controllable accounts for payload injection in XSS attacks.

## Description

Shopify allows store owners to invite staff via email or direct addition, assigning limited permissions. In an attack scenario, this creates a vector for name manipulation. Prerequisites include store ownership; outcomes are a new user entry visible in activity logs.

## Requirements

1. Active Shopify store dashboard access.
2. Email address for the staff member (attacker-controlled).
3. Permissions to manage users.

## Defense

Defensive measures and detection strategies:

- Limit staff invitations to verified domains.
- Audit user addition logs for anomalies.

## Objectives

1. Introduce a new staff account.
2. Assign minimal permissions to avoid detection.
3. Prepare for name-based payload storage.

## Instructions

### Step 1: Navigate to User Settings

**Context**: Access the section for managing store users.

No specific command; go to Settings > Users and permissions.

> Select 'Add staff' or 'Invite staff'.

### Step 2: Invite or Add Staff

**Context**: Provide details to create the staff entry.

No specific command; enter email and set permissions (e.g., read-only).

> Send invitation; accept it with attacker credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- staff-addition
