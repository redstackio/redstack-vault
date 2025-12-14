---
id: p3q4r5s6-t7u8-9012-defg-345678901234
name: Verify-Administrator-Access
tags:
  - access-verification
  - pii-exposure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:58.584Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Administrator-Access

## Summary

This procedure confirms successful privilege escalation by accessing admin-only features and sensitive data in the DoD web application post-registration.

## Description

After tampering, the new account should have admin rights (user_type=4), granting access to all applicant PII. This targets ColdFusion apps lacking role-based controls, with outcomes including data theft risks. No tools beyond browser needed if login succeeded.

## Requirements

1. Successful registration and login
2. Knowledge of admin endpoints (e.g., PII dashboard)
3. Target app session active

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) with server-side checks
- Audit logs for admin actions from new accounts
- Rate-limit or monitor unusual access patterns to sensitive data

## Objectives

1. Confirm admin privileges
2. Access and view PII to validate impact
3. Identify further exploitation paths

## Instructions

### Step 1: Navigate to Admin Features

**Context**: Test for elevated access.

**Instructions**: From the logged-in dashboard, attempt to access admin sections like user management or applicant lists.

> Look for URLs like /admin or /reports. Expected: Pages load without access denied errors.

### Step 2: Access Sensitive PII

**Context**: Verify data exposure.

**Instructions**: Go to applicant database or search features. Query for any SSN or name.

> Full records including SSNs, phones, emails should display. Expected: Unrestricted access to all data.

### Step 3: Document Impact

**Context**: Capture evidence of success.

**Instructions**: Screenshot or export visible PII to confirm escalation.

> Note any additional admin functions available. Expected: Proof of full system control.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-verification
- pii-exposure
