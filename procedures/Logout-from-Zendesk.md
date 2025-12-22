---
tags:
  - session-management
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 97956108-2a7a-4bd2-8258-b994f932bf7c
created_at: '2025-12-13T09:01:26.692Z'
updated_at: '2025-12-13T09:01:26.692Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Logout from Zendesk

## Summary

This procedure ensures no active Zendesk session exists before attempting impersonation.

## Description

The attacker logs out of Zendesk to clear any existing sessions, preventing conflicts during the use of a tampered JWT. This is crucial in web-based SSO scenarios to simulate a clean login attempt.

## Requirements

1. Access to Zendesk dashboard
2. Browser cookies cleared if necessary

## Defense

Defensive measures and detection strategies:

- Implement session timeouts and monitoring
- Detect rapid login/logout patterns

## Objectives

1. Clear active sessions
2. Prepare for fresh authentication
3. Avoid detection from session overlaps

## Instructions

### Step 1: Perform Logout

**Context**: Ensure session is terminated.

Navigate to Zendesk and log out, or clear browser data for the domain.

> Confirm no active session remains.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[session-management]]
