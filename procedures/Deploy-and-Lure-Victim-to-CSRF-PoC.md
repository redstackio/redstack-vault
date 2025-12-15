---
id: proc-uuid-004
tags:
  - csrf
  - web
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:35.911Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deploy-and-Lure-Victim-to-CSRF-PoC

## Summary

This procedure hosts the CSRF PoC on an attacker-controlled server and uses social engineering to trick the victim into visiting it while authenticated, executing the account deletion.

## Description

In scenarios like the DoD application, hosting involves simple HTTP servers or cloud services. Luring relies on phishing-like tactics. Success deletes the victim's account silently, assuming same-site cookie policy allows the forged request.

## Requirements

1. Generated CSRF PoC HTML from prior step
2. Hosting server (e.g., GitHub Pages, local ngrok tunnel)
3. Communication channel to victim (email, link in message)

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links and same-site warnings
- Monitor for anomalous deletions and cross-origin requests
- Deploy Content Security Policy (CSP) to restrict form submissions

## Objectives

1. Make the PoC accessible via public URL
2. Induce victim interaction for request forgery
3. Achieve unauthorized account impact

## Instructions

### Step 1: Host the PoC

**Context**: Serve the HTML file externally for victim access.

Upload the HTML to a hosting service or run a local server (e.g., python -m http.server) and expose via ngrok for a public URL.

**Expected Output**: Public link like https://attacker.com/delete-poc.html.

### Step 2: Distribute Link to Victim

**Context**: Trick the victim into opening the link while logged in.

Send the URL disguised as a legitimate resource (e.g., 'Check this profile update'). Victim clicks, form submits to target endpoint.

**Expected Output**: Account deletion executed; victim loses access.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[social-engineering]]
