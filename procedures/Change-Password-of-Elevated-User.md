---
tags:
  - wordpress
  - password-change
  - credential-access
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
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:44.828Z'
sub_techniques:
  - '[[Credentials In Files]]'
id: b11f055e-1513-4623-8754-a4d742d3262b
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Change-Password-of-Elevated-User

## Summary

This procedure updates the password of an elevated user account to allow takeover with the new Editor privileges in WordPress.

## Description

After role assignment, the Shop Manager can directly modify the target user's password via the admin interface, hashing it with WordPress's default (e.g., PHPass). This grants full control without notifying the original user. Targets the user_pass field in the wp_users table. Expected outcome: Ability to authenticate as the Editor.

## Requirements

1. Active editing session on the target user
2. Knowledge of a secure new password
3. Shop Manager or higher permissions

## Defense

Defensive measures and detection strategies:

- Enable email notifications on password changes
- Log all admin-initiated user updates with plugins like Activity Log
- Restrict password reset capabilities for non-Admin roles

## Objectives

1. Secure the elevated account
2. Prepare for login with new credentials
3. Maintain stealth in takeover

## Instructions

### Step 1: Access Password Fields

**Context**: Locate the account management section during user edit.

In the user edit form, scroll to the 'Account Management' area.

> This section includes new password input fields.

### Step 2: Update and Save

**Context**: Set and confirm the new password.

Enter and confirm a new password, then click 'Update User'.

> WordPress hashes and stores the new password; confirmation message appears on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Password Policy Discovery

## Commands Used


## Tools Used


## Tags

- wordpress
- password-change
