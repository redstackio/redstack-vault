---
id: uuid-3
tags:
  - phishing
  - social-engineering
  - authorization
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:33:34.359Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Trick-Victim-into-Authorizing-OAuth-Request

## Summary

Socially engineer the victim to visit the OAuth authorization URL, leveraging Periscope's auto-login feature if previously authenticated, to grant the request token.

## Description

Direct the victim to the Twitter authorization URL via phishing. Periscope's integration allows seamless approval if logged in. This relies on user interaction; targets mobile/web. Outcome: Authorization completed, verifier generated.

## Requirements

1. Valid authorization URL from request token.
2. Phishing vector (email, link, etc.).
3. Victim with linked Periscope/Twitter account.

## Defense

Defensive measures and detection strategies:

- User training on suspicious authorization prompts.
- App warnings for third-party logins.
- Monitor for unusual authorization spikes.

## Objectives

1. Get victim to approve the request.
2. Trigger callback with verifier.
3. Maintain stealth via familiar Periscope branding.

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create a lure directing to auth URL.

Send email/SMS: "Update your Periscope settings: [auth URL]".

> Mimic official Periscope communication to reduce suspicion.

### Step 2: Victim Interaction

**Context**: Victim visits URL and authorizes.

If logged in, Twitter redirects to Periscope callback automatically.

> Monitor for callback initiation; no direct control, but success via next steps.

### Step 3: Verify Authorization

**Context**: Check if verifier is appended to callback.

Observe redirect; if successful, proceed to bypass.

> Indicator: Callback URL includes `oauth_verifier` param.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (adapted for link)

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[Phishing]]
- [[social-engineering]]
