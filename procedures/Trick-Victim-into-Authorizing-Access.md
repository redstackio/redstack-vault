---
tags:
  - social-engineering
  - authorization-bypass
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:25:17.822Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6c309d7b-3b84-4f35-980a-6cc6d90de7ff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Trick-Victim-into-Authorizing-Access

## Summary

This procedure relies on social engineering to convince the victim to grant OAuth access during the authentication flow, resulting in a redirect that exposes the access token.

## Description

Once the victim clicks the malicious link, Shopify prompts for authorization to support access if not previously granted. Upon approval, the lax redirect validation sends the victim to the attacker's shop with the auth_code in the URL query parameters. This step hinges on the victim's trust in the seemingly legitimate flow.

## Requirements

1. Victim interaction with the crafted link
2. No prior authorization for Shopify support
3. Public access to the auth endpoint

## Defense

Defensive measures and detection strategies:

- Require user confirmation for sensitive authorizations
- Log and alert on OAuth grants from unusual sources
- Implement multi-factor prompts for auth flows

## Objectives

1. Obtain victim approval for access
2. Trigger redirect with exposed token
3. Enable token capture in attacker environment

## Instructions

### Step 1: Monitor Victim Interaction

**Context**: Wait for victim to open the link and encounter the auth prompt.

No command; observe via phishing delivery method or analytics on the link.

> Victim sees Shopify authorization page for livechat support.

### Step 2: Handle Authorization and Redirect

**Context**: Victim grants access, leading to automatic redirect.

The flow redirects to: https://attacker-shop.myshopify.com/?auth_code=<access_token>&auth_type=chat

> Token is appended as auth_code parameter; no further action needed here.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[authorization-bypass]]
