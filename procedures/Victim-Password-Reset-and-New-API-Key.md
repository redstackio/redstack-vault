---
tags:
  - password-reset
  - duplicate-key
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
updated_at: '2025-12-14T17:28:44.443Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 12d1a4f2-2d76-4a60-b3db-42d6fe259aad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Victim-Password-Reset-and-New-API-Key

## Summary

This procedure simulates the victim's response to a failed registration, using password reset to gain access and generate a new API key without revoking the attacker's.

## Description

When the victim tries to register, the email conflict prompts a reset. The reset process emails a link, allowing password change without invalidating existing keys or sessions. A new API key is then issued, coexisting with the attacker's, due to flawed key management.

## Requirements

1. Victim's email access for reset link
2. Web browser for reset and key generation
3. Coding platform for new key integration

## Defense

Defensive measures and detection strategies:

- Revoke all API keys on password reset
- Require re-verification post-reset
- Log reset events tied to prior activity anomalies

## Objectives

1. Grant victim legitimate access, enabling parallel sessions
2. Issue additional API key for concurrent use
3. Expose the lack of session invalidation

## Instructions

### Step 1: Initiate Password Reset

**Context**: Trigger reset after registration failure.

On the login page, enter the victim's email and select 'Forgot Password'.

> An email with a reset link is sent; click it to set a new password.

### Step 2: Generate Victim's API Key

**Context**: Post-reset, obtain a fresh key.

Log in with new password, go to Settings > API Keys, and generate a new one.

> Key issued without checking or revoking prior keys.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[duplicate-key]]
