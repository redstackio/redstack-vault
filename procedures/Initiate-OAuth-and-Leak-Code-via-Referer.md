---
id: uuid-initiate-leak
tags:
  - oauth-leak
  - user-interaction
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/github-oauth-manipulate-redirect-to-about]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:35.837Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Initiate-OAuth-and-Leak-Code-via-Referer

## Summary

This procedure simulates tricking a user into OAuth authentication via manipulated URL, followed by clicking external links to leak the code through Referer headers to third-party sites.

## Description

Exploitation requires social engineering to get the victim to auth and click links on /about/ or /metadata. The code, short-lived, leaks to sites like keybase.io, twitter.com, etc., but impact is low without attacker control over the leaked site.

## Requirements

1. Crafted phishing-like OAuth URL
2. Victim with GitHub access
3. External sites for leakage

## Defense

Defensive measures and detection strategies:

- Implement JavaScript to add rel='noreferrer' dynamically
- Educate users on suspicious auth prompts

## Objectives

1. Obtain code via user interaction
2. Leak to multiple third-parties
3. Assess interception potential

## Instructions

### Step 1: Trick User into Auth

**Context**: Send manipulated URL to victim.

**Command** ([[commands/github-oauth-manipulate-redirect-to-about]]):
```bash
# Victim visits
https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252Fabout%252f%26scope%3Dpublic_repo
```

> Victim auths; lands on /about/?code=abc123.

### Step 2: Induce Link Click and Capture Leak

**Context**: Monitor for Referer on external click.

**Command** (Network Monitor):

Victim clicks link (e.g., to twitter.com); inspect Referer.

> Expected: Referer includes full URL with code to twitter.com, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

-

## Commands Used

- [[commands/github-oauth-manipulate-redirect-to-about]]

## Tools Used

-

## Tags

- referer
- leakage
