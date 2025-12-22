---
id: proc-uuid-003
tags:
  - validation
  - login
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:30:58.754Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Unrestricted-Successful-Login

## Summary

This procedure confirms that multiple prior failed attempts do not trigger any restrictions, allowing successful authentication immediately after, proving the full extent of the rate limiting flaw.

## Description

Following failed tests, this step uses valid credentials on the same endpoint. In LinkedIn's case, access is granted without issues, as captured in successful request images and XML data. This validates the vulnerability's impact on real logins in a web environment.

## Requirements

1. Valid LinkedIn account credentials
2. Burp Suite for request handling
3. Recent failed attempt session (same IP)

## Defense

Defensive measures and detection strategies:

- Temporary session invalidation after failures
- Multi-factor authentication enforcement
- Behavioral analysis for login patterns

## Objectives

1. Ensure no lockout from prior failures
2. Confirm normal access post-attempts
3. Document successful exploitation path

## Instructions

### Step 1: Submit Valid Credentials

**Context**: Replay with correct details after invalids.

**Instructions**: In Burp Repeater, update password to valid and send POST.

> Expected output: 200 OK with session cookies and redirect to dashboard.

### Step 2: Check Access

**Context**: Validate full account functionality.

**Instructions**: Follow redirect and interact with account features.

> Expected output: Unhindered access, no warnings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[validation]]
- [[successful-login]]
