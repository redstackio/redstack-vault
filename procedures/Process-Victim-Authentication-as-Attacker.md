---
id: proc-process-victim-auth
tags:
  - account-takeover
  - session-hijacking
  - oauth
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
updated_at: '2025-12-14T17:27:03.723Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Process Victim Authentication as Attacker

## Summary

This procedure details how the victim's browser submission of the malicious OAuth parameters leads to server-side processing, authenticating them with the attacker's Google identity due to absent state validation.

## Description

When the victim visits the crafted URL, ThisData's server receives the GET request to `/oauth/redirect` with the attacker's state and code. Without checking state integrity, it exchanges the code for an access token via Google's token endpoint, creates a session for the attacker's account, and redirects the victim to the app dashboard. This results in session hijacking. Target is web apps with flawed OAuth implementations.

## Requirements

1. Valid, unconsumed code from attacker flow
2. Victim's browser session on the domain
3. Server vulnerability to state reuse

## Defense

Defensive measures and detection strategies:

- Validate state against stored session values
- Use PKCE for added code protection
- Audit OAuth logs for anomalous authentications

## Objectives

1. Force server to issue attacker session to victim
2. Achieve unauthorized access
3. Enable post-exploitation under victim's context

## Instructions

### Step 1: Victim Submits Parameters

**Context**: Trigger the callback processing.

Victim's browser sends GET to `/oauth/redirect?state=abc123&code=def456`. Server parses without validation.

### Step 2: Server Exchanges Code

**Context**: Backend handles token issuance.

Server POSTs to Google's token endpoint with code, receives access token for attacker's account, and sets session cookies in victim's browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[session-hijacking]]
- [[oauth]]
