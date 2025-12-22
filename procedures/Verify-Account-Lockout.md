---
id: proc-lichess-lockout-verify
tags:
  - dos
  - verification
  - web
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-valid-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:31:52.592Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify-Account-Lockout

## Summary

This procedure tests the effectiveness of the lockout by attempting a legitimate login after failed attempts, confirming the denial-of-service impact on the target account.

## Description

Post-throttling, the Lichess authentication system blocks further logins for the username regardless of origin. Verification involves a clean attempt from a new IP/session, revealing lockout messages. This step validates the vulnerability's exploitability, showing disruption to new sessions while existing ones remain. Technical approach uses HTTP requests; outcomes include error responses indicating lockout.

## Requirements

1. Target username with recent failed attempts
2. New IP or incognito session
3. Optional: Known correct password for full verification

## Defense

Defensive measures and detection strategies:

- Notify users of lockouts via email/SMS for quick recovery
- Shorten lockout durations or require support intervention
- Analyze logs for patterns of distributed failed logins

## Objectives

1. Confirm lockout activation
2. Assess impact on legitimate access
3. Document DoS success for reporting

## Instructions

### Step 1: Initiate Clean Login Attempt

**Context**: Simulate a legitimate user login from a fresh session.

Use incognito mode or new IP to access https://lichess.org/login.

### Step 2: Submit Valid Credentials

**Context**: Attempt login with correct details to trigger lockout response.

Execute [[commands/curl-valid-login]] (assuming known creds; otherwise use guessed valid):

```bash
curl -X POST https://lichess.org/login \
  -d "username=targetuser" \
  -d "password=correctpass" \
  -d "next=https://lichess.org"
```

> Expected output: HTTP response with lockout error, e.g., "Too many attempts, try again later", confirming DoS.

### Step 3: Check Existing Sessions

**Context**: Verify partial impact.

If an existing session is active (e.g., via another device), confirm it persists while new logins fail.

> Output: Active session works, but login endpoint blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-valid-login]]

## Tools Used


## Tags

- [[dos]]
- [[web]]
