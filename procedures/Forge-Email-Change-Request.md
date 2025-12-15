---
tags:
  - csrf
  - account-takeover
  - email-change
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[SAML Tokens]]'
updated_at: '2025-12-14T17:33:06.070Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3453336c-8ece-4354-8788-6d3c2890ca8e
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[SAML Tokens]]'
---
# Forge-Email-Change-Request

## Summary

This procedure forges an authenticated POST request using the fixed fkey to change the victim's email on Khan Academy, achieving account takeover.

## Description

With the known fkey, an attacker crafts a malicious form submission to the email link endpoint, bypassing CSRF protection due to token fixation. This can be delivered via phishing page or injected via XSS, allowing unauthorized email updates that grant password reset control to the attacker.

## Requirements

1. Known fixed fkey from prior extraction
2. Victim's active session (inherited)
3. Malicious HTML form or XSS vector

## Defense

Defensive measures and detection strategies:

- Validate CSRF tokens against session-specific values
- Rate-limit and log sensitive actions like email changes
- Require additional confirmation (e.g., 2FA) for account modifications

## Objectives

1. Submit forged request to alter victim's email
2. Confirm takeover via reset email receipt
3. Exploit for full account control

## Instructions

### Step 1: Craft Malicious Form

**Context**: Build an HTML form that posts the fixed fkey and attacker's email.

Create a simple HTML page with: <form action="https://www.khanacademy.org/settings/linkemail" method="POST"><input type="hidden" name="fkey" value="[extracted_fkey]"><input type="email" name="email" value="attacker@example.com"><input type="submit" value="Update Email"></form>

> Host or deliver this to victim (e.g., via link) while their session is active.

### Step 2: Trigger Submission

**Context**: Get victim to submit or automate via XSS.

In shared scenario, lure victim to click; in XSS, inject script: document.forms[0].submit();

> Server accepts due to matching fkey, updates email to attacker's.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[SAML Tokens]] Forge Web Credentials (CSRF)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[ato]]
