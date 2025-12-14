---
id: proc-004
tags:
  - account-hijack
  - data-exposure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.865Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Account-Hijack

## Summary

This procedure confirms successful authentication by checking access to target account data, validating the hijack.

## Description

Post-submission, the browser session is elevated to the target user, exposing sensitive info like billing details via WooCommerce integration.

## Requirements

1. Successful JWT submission
2. Access to account pages

## Defense

Defensive measures and detection strategies:

- Implement multi-factor auth (MFA)
- Audit logs for unexpected logins
- Session fingerprinting

## Objectives

1. Confirm unauthorized access
2. Exfiltrate personal data
3. Assess further exploitation potential

## Instructions

### Step 1: Navigate to Account Dashboard

**Context**: Check for user-specific content.

**Command** (Manual Navigation):

Visit /my-account/ or profile page.

> Expected output: Displays target user's name, email, billing address.

### Step 2: Inspect Sensitive Data

**Context**: Verify exposure of protected info.

**Command** (Browser Inspection):

Use dev tools to inspect page elements for user data.

> Expected output: Visible personal details confirming hijack.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-hijack
- data-exposure
