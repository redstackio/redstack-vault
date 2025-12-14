---
id: proc-3
tags:
  - social-engineering
  - oauth
  - user-interaction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:35.291Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Victim-OAuth-Authorization

## Summary

This procedure involves social engineering to get the victim to click the malicious OAuth URL and authorize the flow, triggering Facebook's redirect to the attacker's domain with the access token in the URL fragment. The token survives Phabricator's 302 redirect in browsers like Chrome and Firefox due to implicit form actions.

## Description

The victim receives the phishing URL (e.g., via email posing as Phabricator login) and clicks 'Continue' on Facebook's dialog, granting implicit access. Facebook appends the token to the redirect_uri, and Phabricator's handling preserves the fragment across the redirect to the custom domain. This works in most browsers except Safari, which strips anchors. Prerequisites: Crafted URL from prior procedure and victim targeting. Outcome: Token exposed in attacker's browser context.

## Requirements

1. Distributable phishing vector (email, link sharing)
2. Target victim likely to interact with Phabricator/Facebook links
3. No technical barriers; relies on user trust

## Defense

Defensive measures and detection strategies:

- User training on recognizing suspicious OAuth prompts
- Browser policies to block or warn on cross-domain redirects with fragments
- Facebook app review to detect anomalous authorization patterns

## Objectives

1. Obtain victim authorization for token issuance
2. Trigger redirect chain preserving sensitive fragment
3. Deliver token to attacker domain

## Instructions

### Step 1: Distribute Phishing Link

**Context**: Send the crafted OAuth URL to the victim via social engineering.

Embed or send the URL in an email or message claiming it's for Phabricator-Facebook integration.

> Manual distribution. Expected: Victim receives and clicks the link.

### Step 2: Victim Authorizes Flow

**Context**: Victim interacts with Facebook's dialog to grant permissions.

Upon clicking, victim sees the OAuth prompt and selects 'Continue', initiating the implicit grant.

> Victim action; monitor via network tools if testing. Expected: Redirect to redirect_uri with #access_token.

### Step 3: Handle Redirect Preservation

**Context**: Ensure the browser preserves the fragment through Phabricator's redirect.

Phabricator issues a 302 after POST, but implicit action keeps the anchor intact in Chrome/Firefox.

> Passive; test in target browsers. Expected: Final URL on attacker domain includes token fragment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[social-engineering]]
- [[oauth]]
- [[user-interaction]]
