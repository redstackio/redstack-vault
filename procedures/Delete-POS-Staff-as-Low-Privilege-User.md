---
id: proc-uuid-003
tags:
  - broken-access-control
  - unauthorized-deletion
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:20.146Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
# Delete POS Staff as Low-Privilege User

## Summary

This procedure exploits broken access controls to allow a staff member with no permissions to delete POS staff accounts from the account settings page, demonstrating unauthorized account manipulation.

## Description

Using a low-privilege staff login, access /admin/settings/account to view and delete POS staff without any authorization checks. This targets the lack of permission validation on the deletion endpoint, resulting in account removal and inconvenience to store owners, though limited to POS-only access and no data exposure.

## Requirements

1. Existing POS staff account from prior creation
2. Low-privilege staff credentials (no admin rights)
3. Access to /admin/settings/account endpoint

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) for all staff management actions
- Audit logs for deletion attempts by low-privilege users and alert anomalies
- Require confirmation and multi-factor approval for staff deletions

## Objectives

1. Perform unauthorized deletion of POS staff
2. Highlight missing permission checks
3. Cause operational disruption without broader compromise

## Instructions

### Step 1: Log In as Low-Privilege Staff

**Context**: Switch to a staff account with minimal permissions to test access controls.

No command; authentication:

Log in to Shopify admin with low-privilege staff credentials.

> The session grants basic access but no management rights.

### Step 2: Access Account Settings

**Context**: Navigate to the settings page where POS staff are listed.

Navigate to /admin/settings/account.

> The page loads, showing POS staff section without blocking low-priv access.

### Step 3: Execute Deletion

**Context**: Select and delete the target POS staff.

Click on the POS staff entry, then click the delete button.

> Deletion succeeds immediately without permission prompts or errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- broken-access-control
- unauthorized-deletion
- shopify
