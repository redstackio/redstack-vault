---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - phishing
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:35.632Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Phish-Victim-for-OAuth-Authentication

## Summary

This procedure uses social engineering to lure a victim into authenticating via a manipulated OAuth URL, resulting in the authorization code being redirected to the attacker's domain.

## Description

Building on the tampered redirect, this step involves delivering the malicious OAuth link to the victim, who, upon Gmail login, will be redirected with the code appended. This exploits trust in the admin setup process. Target environment is web-based with email or messaging for delivery. Expected outcome: Code leakage without victim suspicion.

## Requirements

1. Manipulated OAuth URL from prior step
2. Communication channel to victim (email, Slack, etc.)
3. Victim with target Gmail account

## Defense

Defensive measures and detection strategies:

- User training on suspicious links in admin contexts
- Email filters for OAuth-related phishing
- Monitor for unexpected OAuth consents in logs

## Objectives

1. Obtain victim authentication
2. Trigger redirect with code
3. Avoid detection during interaction

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create a convincing pretext for the victim to click the link.

Compose an email or message: "Please complete admin account setup by authenticating here: [manipulated OAuth URL]." Mask the URL if needed using a shortener.

> Ensure the message mimics official 8x8 communications.

### Step 2: Deliver and Monitor

**Context**: Send the link and wait for victim interaction.

Send to victim and monitor the attacker server for incoming redirects. Victim clicks, logs into Gmail, and consents to the app.

> The browser will redirect to attacker.com?code=abc123 upon success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.001]] Spearphishing Attachment

## Commands Used


## Tools Used


## Tags

- [[spearphishing]]
- [[oauth-phish]]
