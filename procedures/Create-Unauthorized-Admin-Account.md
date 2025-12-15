---
id: proc-create-unauth-admin
tags:
  - privilege-escalation
  - account-creation
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
  - '[[Create Account]]'
updated_at: '2025-12-14T17:30:07.537Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Create Account]]'
---
# Create-Unauthorized-Admin-Account

## Summary

This procedure creates a new administrative account in an unprotected DoD web application user management interface, generating credentials for unauthorized access and site compromise.

## Description

Within the accessed admin directory, the 'Add New User' form allows input of details like email, name, and agency ('Non-Agency') to create an account with admin privileges. Submission triggers credential generation and email delivery, enabling full control over user privileges and the application.

## Requirements

1. Access to the unprotected 'Add New User' form
2. Valid email address for credential receipt
3. Knowledge of agency selection options

## Defense

Defensive measures and detection strategies:

- Lock user creation behind multi-factor authentication
- Audit all new account creations with alerts
- Disable self-service admin account provisioning

## Objectives

1. Register a new user with admin rights
2. Obtain login credentials
3. Enable privilege escalation

## Instructions

### Step 1: Fill User Form

**Context**: Enter details in the creation interface.

**Command** (Form Submission):
Input: Email (e.g., attacker@example.com), First Name (e.g., Test), Last Name (e.g., Admin), Agency (Non-Agency).

> Form validates inputs; select admin role if prompted.

### Step 2: Submit and Monitor Email

**Context**: Process the request and retrieve credentials.

**Command** (Manual Submit):
Click 'Add New User' button.

> System generates and emails username/password; check inbox for delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Create Account]] Create Account

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[account-creation]]
