---
tags:
  - csrf
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4a79d68e-0203-4283-9fff-4c5344164afb
created_at: '2025-12-14T17:33:34.311Z'
updated_at: '2025-12-14T17:33:34.311Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-Link-for-Account-Linking

## Summary

This procedure involves constructing a malicious URL that exploits the lack of CSRF protection in Rockstar Social Club's third-party account linking feature, allowing an attacker to force a victim's account to link to the attacker's controlled third-party service.

## Description

In the vulnerable setup, the account linking endpoint did not validate CSRF tokens, enabling cross-site requests from external sites. An attacker registers a third-party account, obtains its linking token, and embeds it in a URL that mimics a legitimate linking request. When a logged-in victim visits this URL, their browser submits the request automatically, linking their Social Club account without consent. This is particularly effective if the victim is already authenticated. Prerequisites include knowledge of the linking endpoint URL and a valid third-party account.

## Requirements

1. Access to a third-party service integrable with Social Club (e.g., external OAuth provider)
2. Victim must be authenticated to Social Club in their browser
3. Basic web development knowledge to construct URLs

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use SameSite cookies to prevent cross-site requests
- Monitor for unusual account linking events in logs

## Objectives

1. Generate a functional malicious linking URL
2. Enable unauthorized account association
3. Set up for subsequent takeover

## Instructions

### Step 1: Identify Linking Endpoint

**Context**: Locate the exact URL path for third-party linking in Social Club, typically under `/connect` or similar, by inspecting legitimate linking flows.

No specific command; use browser developer tools to capture the request structure during a normal link attempt.

> Expected: Base URL like `https://socialclub.rockstargames.com/connect/thirdparty`.

### Step 2: Embed Attacker Token

**Context**: Register an account on the third-party service and obtain its unique linking token or ID.

Construct the malicious URL by appending the attacker's token: `https://socialclub.rockstargames.com/connect/thirdparty?provider=external&account_id=attacker_id&token=malicious_token`.

> This URL, when visited, bypasses CSRF checks and links the victim's account.

### Step 3: Test the Link

**Context**: Verify the link works in a controlled environment, such as a test account.

Open the URL in a browser logged into a test Social Club account and confirm linking occurs without additional prompts.

> Expected: Account links silently if CSRF is absent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[account-linking]]
