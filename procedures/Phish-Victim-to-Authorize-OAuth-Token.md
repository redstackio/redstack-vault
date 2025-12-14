---
id: proc-uuid-003
tags:
  - phishing
  - oauth
  - twitter
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:35.377Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Phish Victim to Authorize OAuth Token

## Summary

This procedure involves socially engineering the victim to open and authorize the shared OAuth URL with their Twitter account, binding the token to their credentials.

## Description

The attacker sends the extracted authenticate URL to the victim (e.g., via email to xyz@mail.com), who is logged into a different Twitter account (e.g., TwitterAccount02). The victim opens the link, authenticates if needed, and grants app permissions, unknowingly authorizing the token for the attacker's use. This exploits the lack of session binding in Twitter's OAuth.

## Requirements

1. Extracted OAuth URL from prior step
2. Communication channel to victim (email, chat)
3. Victim's Twitter account active

## Defense

Defensive measures and detection strategies:

- User training on suspicious authorization requests
- OAuth flow verification prompts
- Anomaly detection in authorization logs for cross-account activity

## Objectives

1. Induce victim to authorize the token
2. Bind token to victim's account
3. Enable hijacking without direct credential theft

## Instructions

### Step 1: Deliver the URL

**Context**: Use social engineering to get victim to click the link.

Send the URL to the victim, e.g., "Check this unfollower stats link: https://api.twitter.com/oauth/authenticate?oauth_token=..."

### Step 2: Victim Interaction

**Context**: Observe or confirm victim authorization.

Victim opens URL in their browser, logs in to TwitterAccount02 if prompted, and clicks "Authorize app," granting permissions.

**Expected Output**: Victim logged into the third-party app with their account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- phishing
- oauth
