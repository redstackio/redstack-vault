---
tags:
  - user-creation
  - shopify
  - stocky
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
updated_at: '2025-12-14T17:30:27.388Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 265b5738-db91-4254-b403-4917f4e87d8b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Non-Privileged-User-in-Stocky

## Summary

This procedure creates a standard user account in the Stocky app without assigning admin privileges, providing a low-privilege entry point for further exploitation in privilege escalation attacks.

## Description

In the context of testing Stocky on Shopify, this involves accessing the app's user management interface via a Shopify store admin with 'Apps and channels' permissions. The user is created without elevated roles, ensuring it can authenticate but lacks admin access. This sets up the scenario for intercepting session data to exploit authorization flaws.

## Requirements

1. Shopify account with 'Apps and channels' permission
2. Access to Stocky app installation
3. Basic user details (name, email)

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) during user creation
- Log all user creation attempts and review for anomalies
- Require multi-factor authentication (MFA) for new users

## Objectives

1. Establish a non-privileged session for interception
2. Validate basic access to Stocky endpoints
3. Prepare for privilege escalation without alerting

## Instructions

### Step 1: Access Stocky User Management

**Context**: Navigate to the Stocky app within Shopify to initiate user creation.

Login to your Shopify admin, install or access Stocky, and go to the users or preferences section to add a new user.

### Step 2: Submit User Creation Form

**Context**: Fill in details for a non-admin user and submit.

Provide first name, last name, email, and ensure no admin checkbox is selected. Submit the form.

**Expected Output**: Success message confirming user creation, with the user appearing in the list without admin privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-creation]]
- [[shopify]]
- [[stocky]]
