---
id: 95710ee7-d20e-4c88-98f8-b3600a51ee1d
name: Setup Multiple HackerOne Accounts
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.729Z'
updated_at: '2025-12-11T03:47:47.729Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - setup
  - authentication
  - web
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Proxy]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Setup Multiple HackerOne Accounts

## Summary

This procedure sets up authenticated sessions for multiple users on the HackerOne platform to facilitate testing of cross-account vulnerabilities like IDOR.

## Description

Involves logging into two separate HackerOne accounts using different browser sessions. This is a prerequisite for demonstrating unauthorized access to other users' data. The target environment is the HackerOne web platform, and the expected outcome is having active sessions for User A and User B.

## Requirements

1. Access to two valid HackerOne accounts (credentials required).
2. Two web browsers or incognito sessions.
3. Internet access to hackerone.com.

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication to prevent unauthorized logins.
- Monitor for multiple sessions from the same IP indicating testing activity.

## Objectives

1. Establish authenticated access for testing.
2. Prepare for cross-account exploitation.
3. Verify session management.

## Instructions

### Step 1: Open Browsers and Navigate to HackerOne

**Context**: Prepare separate sessions to avoid cookie conflicts.

Navigate to https://hackerone.com in two different browsers or incognito windows.

> This ensures isolated sessions.

### Step 2: Log In as User A and User B

**Context**: Authenticate each user.

In Browser A, log in with User A's credentials. In Browser B, log in with User B's credentials.

> Confirm login by accessing the user profile page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- setup
- authentication
- web
