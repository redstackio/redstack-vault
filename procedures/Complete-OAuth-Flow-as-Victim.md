---
tags:
  - csrf
  - session-hijack
  - oauth-complete
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.240Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b326b8c4-4e9d-4503-a95c-6ad2f4cc7419
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete-OAuth-Flow-as-Victim

## Summary

This procedure describes how the victim's browser finalizes the OAuth exchange using the attacker's tokens, resulting in the victim being logged into Factlink as the attacker.

## Description

Upon visiting the crafted URL, the victim's browser sends the embedded tokens to Factlink's callback endpoint. Lacking state validation, the server processes them, creating a session tied to the attacker's Twitter identity, enabling unauthorized access.

## Requirements

1. Victim has visited the crafted URL
2. Factlink server processes OAuth 1.0A callbacks without state
3. Victim's browser supports standard redirects

## Defense

Defensive measures and detection strategies:

- Require state parameter in all OAuth flows
- Session fixation protection
- Audit logs for mismatched IP/user-agent in authentications

## Objectives

1. Bind victim's session to attacker's account
2. Achieve login without victim consent
3. Enable post-exploitation actions

## Instructions

### Step 1: URL Access Triggers Request

**Context**: Victim's browser parses the malicious URL.

**Instructions**: No attacker action needed; victim's GET request to `/auth/login/twitter:twitter.com/?oauth_token=...&oauth_verifier=...` is automatic upon click.

> The endpoint receives and validates tokens against Twitter.

### Step 2: Server Processes Tokens

**Context**: Factlink exchanges verifier for access token.

**Instructions**: Server-side, the flow completes: verifier sent to Twitter, access token received, user session created.

> Expected: Redirect to Factlink dashboard as attacker.

### Step 3: Verify Session Hijack

**Context**: Confirm the impersonation.

**Instructions**: If observable, check victim's Factlink view shows attacker's data.

> Success: Unauthorized login confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- session-hijack
