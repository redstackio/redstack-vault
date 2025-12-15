---
id: proc-37signals-auth-session-001
tags:
  - session-management
  - authentication
  - basecamp
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
updated_at: '2025-12-14T17:30:07.308Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-User-Session-in-Basecamp

## Summary

This procedure ensures the victim has an active authenticated session in a 37signals application like Basecamp 3, which is necessary for the CSRF attack to leverage the user's cookies.

## Description

The attack relies on the victim's existing session; no direct action by the attacker is needed here beyond social engineering to keep the victim logged in. The session provides the authenticity for the CSRF-protected endpoint bypass via format trickery.

## Requirements

1. Victim access to Basecamp 3
2. Valid 37signals credentials for victim
3. Browser session persistence

## Defense

Defensive measures and detection strategies:

- Implement short session timeouts
- Use HttpOnly and Secure flags on session cookies
- Monitor for anomalous authorization grants

## Objectives

1. Establish valid user session
2. Ensure cookies are present for CSRF exploitation
3. Prepare browser for malicious form submission

## Instructions

### Step 1: Victim Login

**Context**: Initiate authentication in the target app.

Direct the victim to log in to Basecamp 3 via https://basecamp.com.

**Expected Output**: Dashboard access with session established.

### Step 2: Verify Session

**Context**: Confirm active authentication.

Check browser dev tools for _beanstalk_uuid cookie or similar session identifier.

**Expected Output**: Cookie present in requests to launchpad.37signals.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-management
- authentication
