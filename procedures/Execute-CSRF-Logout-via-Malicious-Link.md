---
tags:
  - csrf
  - exploit
  - malicious-link
  - web
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:49.479Z'
sub_techniques: []
id: 4a0c6b32-2a53-4a52-b7d2-7190b5b8ae6a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute-CSRF-Logout-via-Malicious-Link

## Summary

This procedure crafts and deploys a malicious link exploiting CSRF on Weblate's logout endpoint, forcing an authenticated user to logout by tricking them into clicking it from an external site.

## Description

CSRF attacks rely on the victim's browser sending authenticated requests to the target without consent. Here, an external HTML page hosts a disguised link to /logout/, bypassing protections due to missing token validation. In a SAML-authenticated Weblate environment, this disrupts user sessions, potentially causing denial of service. Expected outcome is involuntary logout upon interaction.

## Requirements

1. Authenticated user session on Weblate
2. Ability to host or simulate an external webpage (local HTML file suffices)
3. Victim to interact with the malicious link

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all POST/GET actions affecting sessions
- Validate referer headers and enforce same-origin policy
- Educate users on phishing links and use browser extensions for CSRF protection

## Objectives

1. Forge a cross-site request to the logout endpoint
2. Trigger session termination without user awareness
3. Demonstrate impact on authenticated access

## Instructions

### Step 1: Craft Malicious Payload

**Context**: Create an external page mimicking a legitimate lure to host the CSRF link.

Create an HTML file with content: <html><body><a href="https://weblate.org/logout/">Click me to see bonus pack</a></body></html>. Save as index.html and open in browser or host on a server.

> The link points directly to the vulnerable endpoint.

### Step 2: Lure and Execute

**Context**: Have the authenticated user visit the external page and click the link.

Direct the victim (with active Weblate session) to the external page. Upon clicking, the browser forges the request using session cookies.

> No additional prompts; logout occurs silently.

### Step 3: Verify Exploitation

**Context**: Confirm the session disruption.

Switch to the original Weblate tab (https://weblate.org/pl/) and refresh.

> User is logged out, requiring re-authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[malicious-link]]
- [[web]]
