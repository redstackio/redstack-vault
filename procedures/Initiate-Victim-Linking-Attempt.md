---
id: proc-003
tags:
  - linking-attempt
  - invalid-input
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
updated_at: '2025-12-14T17:31:11.395Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Victim-Linking-Attempt

## Summary

This procedure switches to the victim's session to start the external account linking process, submitting an invalid password to prepare for response modification, exploiting the client-side reliance on server feedback.

## Description

With the victim's session active, navigate to the linking interface and input arbitrary credentials. This triggers the same client-side validation flow as the legitimate attempt, but sets up an interceptable request. The vulnerability lies in the lack of server-side re-authentication for the linking action itself, allowing client deception. Target: Khan Academy web app; outcome: Ready state for response injection.

## Requirements

1. Persistent victim session
2. Proxy configured for victim's browser traffic
3. Access to linking feature in victim account

## Defense

Defensive measures and detection strategies:

- Require full re-authentication on session switch or linking
- Use device binding to detect session anomalies
- Rate-limit linking attempts per session

## Objectives

1. Activate linking flow in victim context
2. Submit invalid data to generate interceptable traffic
3. Maintain session integrity for bypass

## Instructions

### Step 1: Switch to Victim Browser

**Context**: Ensure victim's session is focused and active.

Select the victim's browser tab. Refresh the dashboard if needed to confirm login state.

> Expected: No session timeout; user profile visible.

### Step 2: Start Linking Process

**Context**: Trigger the password prompt for external service.

Navigate to account settings > Link account (e.g., Gmail). Proceed to the confirmation step.

> Prompt appears; browser traffic routes through proxy.

### Step 3: Submit Invalid Password

**Context**: Enter wrong data to initiate a failing request.

Input an arbitrary password (e.g., "invalid") and submit. Intercept in Burp before server processes.

> Expected: Request captured; prepare to alter response.

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

- [[linking-attempt]]
- [[invalid-input]]
