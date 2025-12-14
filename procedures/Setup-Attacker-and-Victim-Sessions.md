---
id: proc-001
tags:
  - session-management
  - auth-bypass
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
updated_at: '2025-12-14T17:31:11.401Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Attacker-and-Victim-Sessions

## Summary

This procedure establishes isolated browser sessions for both the victim and attacker on Khan Academy, ensuring persistent authentication without interference, as a prerequisite for response manipulation during account linking.

## Description

In a controlled testing environment, such as a shared device or virtual browsers, log in to the victim's account in one session to maintain active cookies and session state. Simultaneously, create a separate session for the attacker's account. This setup exploits the lack of server-side session isolation checks, allowing parallel operations. The target environment is the Khan Academy web application, where account linking features are accessible via the user dashboard. Expected outcomes include two active, non-conflicting sessions ready for linking attempts.

## Requirements

1. Access to Khan Academy login credentials for both attacker and victim accounts
2. Multiple browser instances (e.g., Chrome and Firefox) or incognito modes
3. Stable internet connection to khanacademy.org
4. Optional: Proxy tool like Burp Suite configured for traffic interception

## Defense

Defensive measures and detection strategies:

- Implement server-side session validation and rate limiting on linking attempts
- Enforce logout on suspicious parallel sessions via IP or device fingerprinting
- Monitor for anomalous linking patterns, such as rapid successive attempts from similar IPs

## Objectives

1. Maintain victim's active session for unauthorized linking
2. Isolate attacker's session for legitimate response generation
3. Prepare environment for response capture without alerting the application

## Instructions

### Step 1: Launch Victim Session

**Context**: Create and verify the victim's login to ensure session persistence.

Open a standard browser window and navigate to khanacademy.org. Log in with victim's credentials. Do not close the tab or perform actions that could invalidate the session.

> Verify by accessing the account dashboard; look for personalized content indicating successful login.

### Step 2: Launch Attacker Session

**Context**: Isolate the attacker's login to avoid cross-contamination with victim's cookies.

Open a new incognito window or different browser. Navigate to khanacademy.org and log in with attacker's credentials. Confirm access to account settings.

> Expected: Dashboard loads with attacker's profile data, no overlap with victim session.

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

- [[session-management]]
- [[auth-bypass]]
