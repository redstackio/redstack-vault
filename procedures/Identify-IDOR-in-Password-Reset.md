---
id: proc-uuid-1
tags:
  - idor
  - discovery
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.955Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-IDOR-in-Password-Reset

## Summary

This procedure involves testing Vimeo's password reset functionality to identify an Insecure Direct Object Reference (IDOR) vulnerability, where user identifiers can be manipulated to access unauthorized reset processes.

## Description

In the context of Vimeo's web application, the password reset endpoint fails to verify ownership of the referenced user object, allowing attackers to probe for IDOR by substituting parameters like user IDs. This is typically discovered by intercepting legitimate reset requests and modifying them with identifiers from other accounts, such as those found via public enumeration. Successful identification confirms the lack of authorization checks, setting the stage for exploitation. Prerequisites include basic web request interception capabilities and knowledge of target user IDs.

## Requirements

1. Access to a web proxy or browser dev tools for request manipulation
2. Knowledge of target user IDs (e.g., from Vimeo profiles)
3. Public access to Vimeo.com password reset page

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership verification for all user object references
- Log and monitor anomalous reset requests by IP or frequency
- Use rate limiting on reset endpoints to prevent probing

## Objectives

1. Confirm IDOR existence in password reset flow
2. Gather evidence for exploitation feasibility
3. Identify vulnerable parameters for further steps

## Instructions

### Step 1: Initiate Legitimate Reset and Intercept

**Context**: Start with a controlled reset to baseline the request structure.

Navigate to Vimeo's forgot password page, enter your email, and submit. Use a proxy to capture the POST request to the reset endpoint (e.g., `/api/password/reset`).

**Command** (using curl for simulation):
```bash
curl -X POST https://vimeo.com/api/password/reset -d 'email=your@email.com' -H 'Content-Type: application/x-www-form-urlencoded'
```

> This sends a standard reset request. Expected output: JSON response with a success message or token for your account.

### Step 2: Modify and Test for IDOR

**Context**: Alter the user reference to test authorization bypass.

In the captured request, replace the user identifier (e.g., `user_id=123` or email/token) with a target's (e.g., `user_id=456`). Resubmit.

**Command** (modified curl):
```bash
curl -X POST https://vimeo.com/api/password/reset -d 'user_id=456' -H 'Content-Type: application/x-www-form-urlencoded'
```

> If IDOR exists, expect a success response with reset details for the target. Failure would return an access error.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- web-testing
