---
tags:
  - oauth
  - authorization
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
detection_risk: medium
sub_techniques: []
id: 5b6a550f-b7be-4e8b-a7fb-4553edbb4b75
created_at: '2025-12-11T06:10:15.769Z'
updated_at: '2025-12-11T06:10:15.769Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Prompt OAuth Authorization on Facebook

## Summary

This procedure initiates the OAuth authorization flow on Facebook for the Uber app by directing the victim to a crafted authorization URL with a vulnerable redirect_uri, setting up the chain for token leakage.

## Description

The attack targets a misconfigured OAuth app allowing arbitrary redirect_uris matching https://auth.uber.com/login?*. The victim is tricked into authorizing, which appends an authorization code and redirects to the crafted URI. This is the entry point for chaining redirects in Uber's authentication system.

## Requirements

1. Knowledge of Uber's Facebook OAuth client ID
2. Victim with Uber account linked to Facebook
3. Ability to deliver malicious link (e.g., phishing email)

## Defense

Defensive measures and detection strategies:

- Enforce strict allowlists for OAuth redirect_uris
- Monitor for unusual OAuth authorization requests in logs

## Objectives

1. Obtain victim's authorization for Uber app on Facebook
2. Initiate redirect chain with authorization code
3. Set up for token leakage

## Instructions

### Step 1: Craft Authorization URL

**Context**: Create a malicious URL that prompts the victim to authorize the Uber app on Facebook with a crafted redirect_uri.

Craft the URL as follows:

```
https://www.facebook.com/v2.5/dialog/oauth?client_id=UBER_CLIENT_ID&redirect_uri=https://auth.uber.com/login?next_url=https://login.uber.com/logout&scope=profile%20email
```

> This URL initiates the flow; replace UBER_CLIENT_ID with the actual ID and ensure the redirect_uri matches the vulnerable pattern.

### Step 2: Deliver to Victim

**Context**: Send the URL to the victim via social engineering.

Upon clicking, the victim will be prompted to authorize, leading to the redirect with code.

> Monitor for authorization and proceed to next procedures in the chain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[oauth]]
- [[authorization]]
