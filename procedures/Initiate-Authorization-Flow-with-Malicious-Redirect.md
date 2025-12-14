---
tags:
  - phishing
  - authorization-flow
  - redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-simulate-flow]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.958Z'
sub_techniques: []
id: b00ea788-b443-4ecb-8db2-c1c3402df527
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate Authorization Flow with Malicious Redirect

## Summary

This procedure starts the OpenID Connect authorization process using the crafted malicious redirect_uri, tricking users into authenticating and redirecting them to the attacker-controlled site upon success.

## Description

By providing a link or embedding the authorize URL with the bypassing redirect_uri, the flow proceeds normally until post-auth redirection, where the user lands on the malicious site with tokens exposed in the URI.

## Requirements

1. Malicious URI from prior step
2. Method to deliver link (e.g., email, malicious site)
3. User to interact and authenticate

## Defense

Defensive measures and detection strategies:

- Educate users on phishing links
- Implement state parameters to prevent CSRF
- Rate-limit authorization attempts

## Objectives

1. Trigger user authentication
2. Achieve post-auth redirect to attacker
3. Expose code/token in transit

## Instructions

### Step 1: Deliver the Malicious Link

**Context**: Create and send the authorize URL to the victim.

**Command** ([[commands/curl-simulate-flow]]):
```bash
curl -X GET "https://idp.login.gov/oauth/authorize?client_id=CLIENT_ID&redirect_uri=https://agency.gov.example.com/malicious&response_type=code&scope=openid&state=STATE" -v
```

> In practice, use a browser; curl simulates for testing. Include state for integrity.

### Step 2: Observe Authentication and Redirect

**Context**: User logs in; monitor for 302 to malicious URI.

**Command** ([[commands/curl-simulate-flow]]):
```bash
# Follow redirect with -L flag for full simulation
curl -X GET "https://idp.login.gov/oauth/authorize?..." -L -v
```

> Expect final redirect to attacker site with ?code=...

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-simulate-flow]]

## Tools Used


## Tags

- [[Phishing]]
- [[authorization-flow]]
