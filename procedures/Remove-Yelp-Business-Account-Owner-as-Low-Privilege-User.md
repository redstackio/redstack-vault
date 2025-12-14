---
id: proc-remove-yelp-owner-low-priv
tags:
  - privilege-escalation
  - owner-removal
  - access-control
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:27.023Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Remove Yelp Business Account Owner as Low-Privilege User

## Summary

This procedure exploits improper access controls in Yelp's business account system, allowing a low-privilege invited user to remove the account owner despite lacking permissions for the user management module.

## Description

Yelp's user management lacks consistent authorization checks, enabling low-privilege users to perform sensitive actions like owner removal. This procedure details logging in as the invited user and executing the removal via the web interface. The target is the Yelp Business dashboard, with prerequisites including an active low-privilege session. Successful execution disrupts account ownership, potentially leading to control loss, though the impact is rated low due to limited downstream effects.

## Requirements

1. Active low-privilege user session in the Yelp business account.
2. Web browser access to the business dashboard.
3. Prior invitation and acceptance as the low-privilege user.

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization checks on all user removal endpoints, verifying role permissions server-side.
- Audit logs for removal actions by non-admin users and alert on anomalies.
- Implement confirmation dialogs and secondary verification (e.g., email) for owner-level changes.

## Objectives

1. Bypass restrictions to access owner removal functionality.
2. Successfully remove the account owner.
3. Validate privilege escalation by confirming control disruption.

## Instructions

### Step 1: Log In as Low-Privilege User

**Context**: Establish a session with limited permissions to test escalation.

Log in to Yelp with the low-privilege user's credentials and navigate to the business account dashboard. Verify inability to access full user management but proceed to member list or removal options.

### Step 2: Access Removal Functionality

**Context**: Locate and target the owner for removal despite restrictions.

In the team or users section, search for the owner account. Select the removal option (e.g., 'Remove User' button) and confirm the action. The system processes the request without proper checks.

### Step 3: Verify Removal

**Context**: Confirm the escalation's success.

Refresh the dashboard and check the user list. The owner should no longer appear, indicating successful removal and potential ownership transfer or lockout.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- privilege-escalation
- owner-removal
- access-control
