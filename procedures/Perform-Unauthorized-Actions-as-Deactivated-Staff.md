---
tags:
  - privilege-escalation
  - shopify
  - unauthorized-access
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:24:44.985Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 07df0200-7cc0-46bc-ae15-0a181c146e03
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Perform-Unauthorized-Actions-as-Deactivated-Staff

## Summary

This procedure exploits the bypassed authentication to execute unauthorized actions in the Shopify mobile app, such as changing account status or accessing sensitive store data, resulting in privilege escalation for a supposedly deactivated user.

## Description

Once authenticated via the bypass, the mobile app treats the deactivated staff as active, allowing interactions with store resources. This targets features like account management and notifications in a Shopify store environment. The procedure assumes successful prior login and demonstrates impacts like data exposure or modifications. Outcomes include confirmed unauthorized access, underscoring the need for consistent enforcement across clients.

## Requirements

1. Active session in Shopify mobile app with deactivated staff credentials
2. Target store with configurable features (e.g., staff permissions, notifications)
3. Device with mobile app permissions enabled

## Defense

Defensive measures and detection strategies:

- Audit mobile app actions for privilege mismatches with web status
- Implement session revocation that propagates to all clients immediately
- Use role-based access controls (RBAC) with real-time checks on sensitive operations

## Objectives

1. Access restricted store features post-bypass
2. Execute modifications like status changes
3. View sensitive information such as timeline notifications

## Instructions

### Step 1: Navigate to Account Settings

**Context**: Access areas where privileged actions can be performed.

From the mobile app dashboard, tap into Settings or Account Management.

> Settings menu opens, allowing navigation to status or permissions.

### Step 2: Attempt Status Change or Modification

**Context**: Test escalation by altering account details.

Select an option to change status (e.g., reactivate or edit permissions) and apply changes.

> Changes save without blocking, confirming escalation.

### Step 3: Access Sensitive Features

**Context**: Retrieve or interact with protected data.

Go to notifications or store timeline to view recent activity.

> Sensitive data loads, indicating full unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[unauthorized-access]]
