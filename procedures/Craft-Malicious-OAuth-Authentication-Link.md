---
tags:
  - oauth
  - phishing-link
  - url-crafting
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
updated_at: '2025-12-14T17:25:17.827Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b4b6a249-d40f-4fd8-846d-c1997d1fc0cd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Craft-Malicious-OAuth-Authentication-Link

## Summary

This procedure involves constructing a malicious URL that exploits Shopify's OAuth endpoint by specifying an attacker-controlled redirect URI, tricking the victim into initiating an authentication flow that benefits the attacker.

## Description

In Shopify's livechat authentication, the return_to parameter in the OAuth flow at https://tasker-merchant-auth.herokuapp.com/auth/shopify/ is not properly validated, allowing any .myshopify.com domain. The attacker crafts a link using the victim's shop domain for initial auth but redirects to their own shop afterward, setting up token theft. This requires knowledge of the victim's shop domain and control over a Shopify shop.

## Requirements

1. Attacker-owned Shopify shop (e.g., attacker-shop.myshopify.com)
2. Victim's shop domain (e.g., victim-shop.myshopify.com)
3. Ability to deliver the link to the victim (e.g., email, chat)

## Defense

Defensive measures and detection strategies:

- Implement strict whitelisting for OAuth redirect URIs
- Monitor for unusual redirect patterns in auth logs
- Educate users on phishing links mimicking legitimate auth flows

## Objectives

1. Initiate OAuth flow with victim's credentials
2. Set up redirection to attacker-controlled domain
3. Position for token capture in subsequent steps

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the URL to start OAuth with victim's shop but redirect to attacker's shop.

No specific command; manually construct:

```url
https://tasker-merchant-auth.herokuapp.com/auth/shopify/?utf8=%E2%9C%93&auth_type=chat&return_to=https://attacker-shop.myshopify.com/&shop=victim-shop.myshopify.com
```

> Replace attacker-shop and victim-shop with actual domains. This URL, when opened, prompts auth with victim's shop.

### Step 2: Deliver the Link to Victim

**Context**: Send the crafted URL to the victim to initiate the flow.

Use email or messaging to share the link, disguising it as a legitimate Shopify support request.

> Victim clicks and proceeds to authorization if not previously granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[phishing-link]]
