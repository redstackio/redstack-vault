---
id: proc-uuid-004
tags:
  - phishing
  - csrf
  - malicious-link
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-malicious-link-craft]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:15.851Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-and-Deliver-Malicious-Link

## Summary

This procedure creates a malicious callback URL using the fixed state and attacker's auth code, then delivers it to the victim to execute the CSRF and link accounts.

## Description

By embedding the attacker's authorization code in the callback with the stolen fixed state, clicking the link submits a forged request from the victim's browser, connecting the attacker's Facebook to the victim's Shopify without consent.

## Requirements

1. Attacker's own Facebook auth code (obtained via legitimate flow)
2. Fixed state from previous step
3. Delivery method (e.g., email, site)

## Defense

Defensive measures and detection strategies:

- Validate state on all callbacks
- Require user confirmation for account linking
- Block cross-origin requests without tokens

## Objectives

1. Forge callback URL
2. Trick victim interaction
3. Achieve unauthorized linking

## Instructions

### Step 1: Generate Malicious URL

**Context**: Replace [attacker_token] with actual code and fixed state.

**Command** ([[commands/curl-malicious-link-craft]]):
```bash
curl -X GET "https://facebookstore.shopifyapps.com/authenticated?code=ATTACKER_AUTH_CODE&state=c2f449f2df5ee64df6173702846bce72e3a57319#=_"
```

> Test the URL; expected silent redirect or success page indicating link.

### Step 2: Deliver to Victim

**Context**: Embed in HTML or phishing page for click.

**Instructions**: Create <a href="https://facebookstore.shopifyapps.com/authenticated?code=ATTACKER_AUTH_CODE&state=c2f449f2df5ee64df6173702846bce72e3a57319">Click here to connect</a> and host/deliver.

> Expected: Victim click submits CSRF, linking accounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/curl-malicious-link-craft]]

## Tools Used


## Tags

- [[Phishing]]
- [[csrf]]
- [[malicious-link]]
