---
id: proc-gitlab-unauthorized-access
tags:
  - account-takeover
  - access
  - gitlab
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
updated_at: '2025-12-14T17:31:30.864Z'
skill_level: beginner
impact_level: critical
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Achieve Unauthorized Target Access

## Summary

This procedure validates and utilizes the bypassed authentication to gain full control of the target GitLab account, confirming the exploit's success.

## Description

After submission, the server authenticates based on the target's OTP and login param, issuing a session for the target. The attacker can now perform actions like viewing repos or changing settings. This exploits the lack of password check in 2FA flow.

## Requirements

1. Successful auth response from prior step
2. Target account permissions

## Defense

Defensive measures and detection strategies:

- Require password re-entry for sensitive actions post-2FA
- Log successful logins with IP/user mismatch alerts
- Enable anomaly detection in auth patterns

## Objectives

1. Confirm login as target
2. Access account resources
3. Validate no password needed

## Instructions

### Step 1: Observe Response

**Context**: Check server response for authentication success.

Look for redirect to /dashboard or similar, with target username in session.

> Success: No invalid code error; full access granted.

### Step 2: Perform Account Actions

**Context**: Test access by navigating to target-specific features.

Visit /dashboard or /profile to confirm control.

> Expected: View target's projects, settings without further auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[access]]
- [[gitlab]]
