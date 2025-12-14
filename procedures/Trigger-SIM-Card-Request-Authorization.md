---
tags:
  - authorization
  - sim-request
  - cookie-reflection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:35.767Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: beed43b6-bfb4-4cd5-871e-552cea50f66c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SIM-Card-Request-Authorization

## Summary

This procedure involves a victim user submitting a SIM card request and authorizing it to the malicious user account, causing the backend to reflect the tainted username into a JSON-encoded flash message cookie without escaping.

## Description

In the Mobile Vikings application, SIM card requests require authorization from another user. Selecting the malicious user triggers a flash message like "Authorization will be given to [username] once this user confirms." This message is stored in a cookie (`messages`) as JSON, but the username is inserted raw, preserving the XSS payload. The target is a web app with SIM management features. Outcomes include cookie pollution with executable script, leading to XSS on next page load.

## Requirements

1. Valid user account (User B) with permission to request SIMs
2. Knowledge of the malicious user's ID or name
3. Active session on the platform

## Defense

Defensive measures and detection strategies:

- Escape all user inputs in JSON serialization for cookies
- Validate and sanitize authorization targets
- Log and alert on flash message cookie sizes or content anomalies

## Objectives

1. Reflect malicious username into application state
2. Set tainted cookie for subsequent execution
3. Maintain stealth in legitimate workflow

## Instructions

### Step 1: Initiate SIM Request

**Context**: Log in as User B and start the SIM card request process.

Navigate to the SIM request form and fill in details.

> Select the malicious User A from the authorization dropdown or input field.

### Step 2: Submit and Inspect Cookie

**Context**: Submit to trigger cookie set, then verify reflection.

Submit the form. Use browser dev tools (Application > Cookies) to inspect the `messages` cookie.

> Expected: Cookie value includes unescaped payload, e.g., `\"Authorization will be given to name<script>alert(1)</script> once this user confirms.\"`

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authorization]]
- [[cookie]]

