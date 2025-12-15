---
tags:
  - account-takeover
  - data-modification
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.797Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 29697106-2b6b-4955-8851-7f5a0bba79cc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Achieve-Unauthorized-Account-Access

## Summary

This procedure exploits the replayed session to perform unauthorized actions in the victim's account, such as modifying profile details, demonstrating full takeover.

## Description

With the session hijacked via cookie reuse, the attacker can access and alter sensitive data without credentials. This leads to potential data breaches or further escalation in web applications with poor session handling.

## Requirements

1. Active hijacked session from cookie replay
2. Knowledge of target account's sensitive endpoints
3. No additional tools beyond browser or proxy

## Defense

Defensive measures and detection strategies:

- Require re-authentication for sensitive actions
- Audit logs for unauthorized changes
- Multi-factor authentication to complement session tokens

## Objectives

1. Edit account information without credentials
2. Confirm takeover by performing modifications
3. Highlight impact of session vulnerabilities

## Instructions

### Step 1: Access Edited Page

**Context**: Use the replayed session to load the admin edit interface.

Navigate to the edit page; it should load fully authenticated.

**Expected Output**: Editable fields for username, email, password visible.

### Step 2: Perform Modifications

**Context**: Alter data to demonstrate control.

Change values like username or password and submit the form.

### Step 3: Verify Changes

**Context**: Confirm the unauthorized actions succeeded.

Refresh or log in legitimately to see modifications applied.

**Expected Output**: Changes persisted in the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-takeover
- data-modification
