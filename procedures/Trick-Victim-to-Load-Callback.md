---
tags:
  - csrf
  - phishing
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
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:27:03.677Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 170c27dd-36d9-47db-8014-040ff0763435
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Trick Victim to Load Callback

## Summary

Uses social engineering to induce the victim to visit the captured callback URL while authenticated in Shopify, completing the CSRF.

## Description

The attacker crafts a link to the intercepted URL and sends it via email or message, exploiting the lack of origin verification. When loaded in the victim's session, it links the attacker's Pinterest account.

## Requirements

1. Captured callback URL with code
2. Communication channel to victim (email, chat)
3. Victim authenticated in Shopify admin

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Browser same-origin policy enforcement and CSP headers

## Objectives

1. Victim loads URL in session
2. OAuth completes unauthorized
3. Integration hijacked

## Instructions

### Step 1: Craft Malicious Link

**Context**: Disguise the URL.

Embed https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=... in a phishing page or shorten it.

> Expected: Clickable link ready.

### Step 2: Deliver to Victim

**Context**: Social engineer.

Send via email: 'Click to verify your Pinterest integration: [link]'.

> Expected: Victim clicks while logged in.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
- [[social-engineering]]
