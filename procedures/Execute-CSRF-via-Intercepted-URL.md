---
tags:
  - csrf
  - session-hijacking
type: procedure
tools:
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Man in the Browser]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e9e2ffd5-5783-4ccb-8dca-947ddc552845
created_at: '2025-12-13T09:01:26.389Z'
updated_at: '2025-12-13T09:01:26.389Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Man in the Browser]]'
---
# Execute CSRF via Intercepted URL

## Summary

This procedure exploits the intercepted state variable in the SSO redirect to perform CSRF, logging the attacker into the victim's Badoo session on their device.

## Description

By capturing the state-linked URL via MITM, the attacker authenticates with their own credentials and tricks the victim into loading the redirect URL, forcing a session takeover. This targets the lack of validation in the SSO flow. Expected outcome is attacker's control over victim's browser session.

## Requirements

1. MITM interception capability
2. Social engineering to make victim visit URL
3. Attacker's own Odnoklassniki credentials

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens with strict validation
- Use secure, short-lived state parameters
- Educate users on URL safety

## Objectives

1. Capture and manipulate redirect URL
2. Authenticate with attacker's credentials
3. Force victim to load URL for session injection

## Instructions

### Step 1: Intercept URL with State

**Context**: Capture the OAuth authorize URL.

Use [[tools/mitmproxy]] to log the URL including state parameter.

> State is linked to victim's session.

### Step 2: Authenticate with Own Credentials

**Context**: Use intercepted URL to log in as attacker.

Navigate to the captured URL and enter attacker's credentials.

> Generates a return URL with code.

### Step 3: Trick Victim to Visit Return URL

**Context**: Deliver the manipulated URL to victim.

Provide the URL to https://badoo.com/external/redirector.phtml to the victim.

> Victim loading it injects attacker's session.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Man in the Browser]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/mitmproxy]]

## Tags

- [[csrf]]
- [[session-hijacking]]
