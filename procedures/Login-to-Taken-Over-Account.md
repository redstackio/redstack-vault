---
tags:
  - account-takeover
  - login
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.137Z'
sub_techniques: []
id: 51be68bd-465b-4664-baa0-11370d91fccd
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Taken-Over-Account

## Summary

This procedure uses the intercepted password to log in to the victim's account, achieving full control.

## Description

With the new password and known username, submit login form at the app's root /. Target: ColdFusion login endpoint. Outcome: Attacker gains access to all account data and functions.

## Requirements

1. Victim's username
2. New password from reset
3. Valid session or clean login

## Defense

Defensive measures and detection strategies:

- Multi-factor authentication
- Alert on logins from new locations
- Session invalidation on resets

## Objectives

1. Authenticate as victim
2. Access sensitive data
3. Perform further actions

## Instructions

### Step 1: Navigate to Login

**Context**: Go to the login page.

Visit https://target.com/.

> Login form appears.

### Step 2: Submit Credentials

**Context**: Enter username and password.

Input username and new password, then submit.

> Authentication succeeds.

### Step 3: Verify Access

**Context**: Confirm control.

Navigate to account pages; make a test change.

> Full access granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[valid-accounts]]
