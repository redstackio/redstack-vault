---
tags:
  - oauth
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/initiate-microsoft-oauth-consent]]'
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c3ddc26c-b30e-4265-a155-2d56d4c5ff2b
created_at: '2025-12-14T17:24:35.779Z'
updated_at: '2025-12-14T17:24:35.779Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-OAuth-Flow-for-Contact-Import

## Summary

This procedure initiates the OAuth authorization flow between Twitter and Microsoft Outlook for importing contacts, leveraging pre-existing user authorization to minimize interaction required for subsequent exploitation.

## Description

The attack scenario targets users accessing Twitter's 'Who to Follow' import feature, which triggers OAuth with Microsoft. If the user has previously authorized Twitter to access Outlook, no full re-authentication is needed, setting up for token theft. This works on the web platform using OAuth 2.0, requiring only browser access to Twitter.

## Requirements

1. Access to Twitter web interface
2. Victim pre-authorized with Microsoft Outlook via Twitter
3. No special tools; uses standard browser navigation

## Defense

Defensive measures and detection strategies:

- Enforce strict redirect_uri validation in OAuth apps
- Monitor for unusual OAuth consent triggers from import features
- User education on phishing links mimicking legitimate flows

## Objectives

1. Start OAuth flow without alerting user to full login
2. Position for chaining with malicious redirect
3. Obtain authorization code or direct token if pre-authorized

## Instructions

### Step 1: Navigate to Import Contacts

**Context**: Access Twitter's contact import page to trigger the OAuth handshake with Microsoft.

**Command** ([[commands/initiate-microsoft-oauth-consent]]):
```bash
# Simulate navigation; in practice, visit the URL in browser
curl -I "https://twitter.com/who_to_follow/import"
```

> This command checks the endpoint; expected output is a redirect to Microsoft's OAuth URL. In a real attack, direct the victim to https://twitter.com/who_to_follow/import.

### Step 2: Handle Pre-Authorization

**Context**: If pre-authorized, the flow proceeds directly; otherwise, consent is prompted.

No specific command; monitor for redirect to https://login.live.com/.

> Expected output: Silent progression or consent screen.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- [[commands/initiate-microsoft-oauth-consent]]

## Tools Used

- None

## Tags

- [[oauth]]
- [[initial-access]]
