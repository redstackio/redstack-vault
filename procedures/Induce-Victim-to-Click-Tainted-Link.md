---
tags:
  - social-engineering
  - oauth-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f3ea9549-939c-4a23-a228-26a1c3fb75db
created_at: '2025-12-14T00:11:25.333Z'
updated_at: '2025-12-14T00:11:25.333Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce Victim to Click Tainted Link

## Summary

This procedure involves luring the victim to visit the malicious page and click the tainted Apple sign-in link, leading to token leakage in the URL fragment.

## Description

The victim completes the sign-in, which redirects with tokens exposed in the fragment due to modified OAuth parameters.

## Requirements

1. Malicious page hosted and accessible
2. Victim with Reddit account using Apple sign-in
3. Social engineering to direct victim to page

## Defense

Defensive measures and detection strategies:

- Educate users on phishing risks
- Monitor for unusual redirects

## Objectives

1. Trigger victim interaction
2. Leak OAuth tokens
3. Set up for theft

## Instructions

### Step 1: Direct Victim to Page

**Context**: Send the malicious URL to the victim via phishing or other means.

Victim visits the page and clicks the Apple sign-in link.

### Step 2: Complete Sign-In

**Context**: Victim authenticates with Apple.

Redirect occurs to https://reddit.com/#state=xxx&code=xxx&id_token=xxx, leaking tokens.

> Tokens are now in the fragment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- social-engineering
- oauth-leak
