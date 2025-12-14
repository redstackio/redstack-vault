---
tags:
  - admin-login
  - verification
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:27.384Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: bd0e1765-922e-4c8f-a63c-46cf379a2ee8
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-New-Admin-User

## Summary

This procedure verifies the success of admin creation by logging out of the current session and authenticating as the new admin user, confirming elevated privileges in Stocky.

## Description

After exploiting the create_admin endpoint, end the existing session to avoid conflicts, then use the new credentials (email and auto-generated password or direct login) at the Stocky login page. Successful login grants access to admin-only features, demonstrating the escalation.

## Requirements

1. New admin credentials from creation response
2. Access to https://stocky.shopifyapps.com login
3. Prior logout from non-privileged session

## Defense

Defensive measures and detection strategies:

- Alert on new admin logins from unusual IPs
- Require approval workflows for admin promotions
- Audit login events for privilege changes

## Objectives

1. Validate admin creation success
2. Access elevated Stocky functionalities
3. Confirm impact on inventory and order management

## Instructions

### Step 1: Logout Current Session

**Context**: Clear the non-privileged session.

Navigate to logout in Stocky or close the browser session.

### Step 2: Login with New Admin Credentials

**Context**: Authenticate to verify privileges.

Go to https://stocky.shopifyapps.com, enter the new admin email and password, and submit.

**Expected Output**: Redirect to admin dashboard with options for inventory updates, vendor management, and purchase orders.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[admin-login]]
- [[verification]]
