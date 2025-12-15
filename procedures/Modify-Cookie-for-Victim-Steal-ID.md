---
tags:
  - cookie-tampering
  - impersonation
  - idor-prep
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
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:25:47.975Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Application Access Token]]'
id: 677d6041-9270-481a-8da8-a704e23111e3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Modify-Cookie-for-Victim-Steal-ID

## Summary

Edit the 'steamid' cookie in the crafted sync request to match the victim's Steam ID, bypassing ownership verification in the IDOR vulnerability.

## Description

The /sync endpoint trusts the client-provided steamid without server-side checks against the session owner. This procedure involves intercepting or manually editing the Cookie header in the HTTP request using tools like Burp Suite or curl flags. Prerequisites: Captured legitimate request and victim's ID; outcome: Tampered request poised for unauthorized execution.

## Requirements

1. Captured sync request from authentication step
2. Victim's Steam ID from recon
3. HTTP client capable of header editing (e.g., curl, Burp)

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership validation (e.g., compare cookie ID to session token)
- Use signed cookies or JWTs for identity
- Detect cookie mismatches via logging and anomaly detection

## Objectives

1. Substitute victim ID in cookie
2. Maintain request validity
3. Set up for data tampering

## Instructions

### Step 1: Intercept Request

**Context**: Use a proxy to capture the request for editing.

No command; configure Burp or similar.

> Route traffic through proxy and trigger sync to get the request.

### Step 2: Edit Cookie Header

**Context**: Replace steamid value.

Manual edit:

Change Cookie: steamid=7656119XXXXXXXXXX to steamid=7656119YYYYYYYYYY.

> Expected output: Updated header ready for resend. Verify no syntax errors in JSON payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

- [[Application Access Token]]

## Commands Used


## Tools Used


## Tags

- cookie-tampering
- idor-prep
