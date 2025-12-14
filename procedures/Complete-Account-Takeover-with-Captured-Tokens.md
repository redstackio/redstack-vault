---
id: proc-periscope-oauth-ato-complete
tags:
  - account-takeover
  - oauth
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/attacker-completion-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.672Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Complete-Account-Takeover-with-Captured-Tokens

## Summary

This procedure uses the captured OAuth token and verifier to complete the login on Periscope TV, linking the victim's account to the attacker's session for takeover.

## Description

With the token and verifier, the attacker sends a request to Periscope's /i/twitter/loginComplete endpoint. The server validates the tokens (from the victim's authorization) and grants access, effectively taking over any existing Periscope account or creating a new one linked to the victim's Twitter.

## Requirements

1. Captured oauth_token and oauth_verifier
2. Access to Periscope TV domain
3. Browser or proxy to send the completion request

## Defense

Defensive measures and detection strategies:

- Bind OAuth sessions to specific user agents or IPs
- Require additional verification for account linking
- Audit OAuth completions for anomalies like rapid token usage

## Objectives

1. Submit tokens to loginComplete endpoint
2. Achieve authenticated session
3. Access victim's Periscope account

## Instructions

### Step 1: Send Completion Request

**Context**: Replay the tokens on the legitimate Periscope domain to finalize auth.

**Command** ([[commands/attacker-completion-request]]):
```http
www.periscope.tv/i/twitter/loginComplete?oauth_token=[attacker's oauth token]&oauth_verifier=[victim's oauth verifier]
```

> Server processes tokens; expected output is successful login page or redirect to dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/attacker-completion-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-takeover
- oauth
