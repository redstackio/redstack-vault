---
id: proc-replay-request
tags:
  - http-replay
  - privilege-escalation
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.666Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Replay-Intercepted-HTTP-Request-with-Burp

## Summary

This procedure resends a previously intercepted admin HTTP request using Burp Suite to bypass role-based access controls in the Omise dashboard after downgrade.

## Description

With the user's role set to none, use Burp Repeater to resend the captured request to https://dashboard.omise.co/v2/links for editing/adding links. The backend fails to revalidate the current role, allowing success. This exploits missing server-side checks. Prerequisites: Intercepted request and active session. Outcome: Unauthorized action completes.

## Requirements

1. Burp Suite with intercepted request
2. Downgraded user session
3. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Revalidate user roles on every request
- Implement short-lived session tokens
- Detect replay attempts via timestamps or unique IDs

## Objectives

1. Achieve privilege escalation via replay
2. Demonstrate broken access control
3. Confirm backend vulnerability

## Instructions

### Step 1: Load Request in Repeater

**Context**: Prepare the intercepted request for resending.

No specific command; in Burp, send captured request to Repeater tab.

> Request details (headers, payload) displayed.

### Step 2: Replay the Request

**Context**: Send without modifications to test bypass.

No specific command; click 'Send' in Repeater.

> Response: 200 OK with successful action (e.g., link updated).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- http-replay
- privilege-escalation
- burp-suite
