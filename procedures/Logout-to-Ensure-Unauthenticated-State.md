---
tags:
  - session-management
  - logout
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:33:11.923Z'
sub_techniques: []
id: 71731f10-72ba-4519-a898-cd3acb2e1bcc
validated: true
---
# Logout-to-Ensure-Unauthenticated-State

## Summary

This procedure logs out the test account to simulate an unauthenticated state, critical for testing the IDOR vulnerability without session interference.

## Description

Logging out clears cookies and session data, ensuring the subsequent POST request to /chkUser.aspx is unauthenticated. This targets the ASP.NET app's session handling flaws.

## Requirements

1. Active session from login
2. Access to logout functionality

## Defense

Defensive measures and detection strategies:

- Secure session invalidation on logout
- Log session terminations

## Objectives

1. Clear authentication
2. Prepare for unauthenticated exploit

## Instructions

### Step 1: Initiate Logout

**Context**: Use the logout button or endpoint.

No command; browser action.

> Expected: Redirect to login; session expired.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-management]]
