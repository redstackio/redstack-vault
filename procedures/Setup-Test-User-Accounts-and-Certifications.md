---
id: proc-setup-hackerone-accounts
tags:
  - setup
  - authentication
  - web
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
updated_at: '2025-12-14T17:26:00.446Z'
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
# Setup-Test-User-Accounts-and-Certifications

## Summary

This procedure establishes authenticated sessions and populates test data (licenses and certifications) in multiple HackerOne user accounts to prepare for IDOR exploitation testing, simulating attacker and victim environments.

## Description

In the context of testing HackerOne's platform, this involves logging into two separate accounts using different browsers to avoid session overlap and creating sample certifications. This setup is crucial for demonstrating unauthorized deletion without affecting real user data. Expected outcomes include isolated sessions and identifiable certification IDs for targeting.

## Requirements

1. Valid credentials for at least two HackerOne accounts (e.g., test accounts)
2. Two separate web browsers (e.g., Chrome and Firefox)
3. Network access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for account creation and login
- Monitor for unusual login patterns from multiple browsers or IPs
- Use session isolation and rate limiting on profile modifications

## Objectives

1. Achieve authenticated access to multiple user profiles
2. Create traceable certifications for deletion testing
3. Ensure no cross-session interference

## Instructions

### Step 1: Log In to Accounts

**Context**: Create isolated sessions for User A (attacker) and User B (victim).

No specific command; use browser navigation:

Navigate to https://hackerone.com and log in with User A credentials in Browser 1, then User B in Browser 2.

> Successful login redirects to the dashboard; verify profile access.

### Step 2: Create Certifications

**Context**: Add sample data to enable IDOR targeting.

No specific command; use platform UI:

In each browser, go to the certifications/licenses section, fill in details (e.g., certification name, date), and submit to create.

> New entries appear in the profile; note any visible IDs or inspect network requests to capture them.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[authentication]]
- [[web]]
