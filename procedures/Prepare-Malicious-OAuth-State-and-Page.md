---
tags:
  - oauth
  - setup
type: procedure
tools:
  - '[[tools/Google-Tag-Manager]]'
  - '[[tools/Chrome-Browser]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/postmessage-oauthdone]]'
  - '[[commands/fetch-logged-tokens]]'
  - '[[commands/php-log-querystring]]'
  - '[[commands/php-parse-logs]]'
  - '[[commands/history-pushstate-monitor]]'
  - '[[commands/top-postmessage-relay]]'
  - '[[commands/parent-onmessage-listener]]'
  - '[[commands/setinterval-monitor]]'
  - '[[commands/sanitize-oauth-params]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 902135e0-b84f-4e6e-9529-b1b9f3f6dd29
created_at: '2025-12-11T06:10:22.350Z'
updated_at: '2025-12-11T06:10:22.350Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Prepare Malicious OAuth State and Page

## Summary

This procedure involves obtaining a valid OAuth state from Reddit's Apple sign-in and setting up a malicious page with an XSS-exploiting iframe to prepare for token theft.

## Description

The attacker initiates their own Apple sign-in on Reddit to capture a state parameter, then crafts a page that loads a vulnerable iframe on www.redditmedia.com using Google Tag Manager to inject malicious JavaScript. This sets the stage for modifying OAuth parameters and leaking tokens.

## Requirements

1. Access to Reddit and Apple ID sign-in.
2. Ability to host a malicious web page.
3. Google Tag Manager configuration for custom ID.

## Defense

Defensive measures and detection strategies:

- Enforce strict OAuth response modes and validate redirect URIs.
- Monitor for unusual GTM ID loads and iframe communications.

## Objectives

1. Obtain valid state for OAuth tampering.
2. Prepare iframe for XSS exploitation.
3. Enable token leakage via modified response_type.

## Instructions

### Step 1: Obtain State Parameter

**Context**: Initiate Apple sign-in on reddit.com to extract state from URL.

Use browser tools to capture the state value.

### Step 2: Create Malicious Page

**Context**: Load iframe with custom GTM ID and encoded state.

Set up monitoring in the page using [[commands/history-pushstate-monitor]]:

```javascript
history.pushState('/','/',location.pathname +'?monitor&state='+ st)
```

### Step 3: Taint OAuth Link

**Context**: Modify response_type to 'code+id_token' and response_mode to 'fragment'.

Craft the link with redirect_uri as https://reddit.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/history-pushstate-monitor]]

## Tools Used

- [[tools/Google-Tag-Manager]]
- [[tools/Chrome-Browser]]

## Tags

- [[commands/sanitize-oauth-params]]
- [[setup]]
