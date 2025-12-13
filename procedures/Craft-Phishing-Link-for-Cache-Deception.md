---
tags:
  - phishing
  - web-cache-deception
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: db7c3968-7945-4c3d-b2cf-37c776206748
created_at: '2025-12-13T09:00:34.050Z'
updated_at: '2025-12-13T09:00:34.050Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Craft Phishing Link for Cache Deception

## Summary

This procedure details creating and distributing phishing links that trick victims into loading sensitive pages on vulnerable subdomains, forcing the web cache to store the content for later retrieval by the attacker.

## Description

By appending a cacheable file extension to a sensitive URL, the phishing link causes the victim's browser to request and cache the page. This exploits the improper caching on kaspersky.com subdomains, allowing unauthorized access to the cached data. Requires social engineering skills.

## Requirements

1. Identified vulnerable subdomain
2. Ability to send phishing messages
3. Knowledge of target user's sensitive endpoints

## Defense

Defensive measures and detection strategies:

- Educate users on phishing awareness
- Use URL filtering to block suspicious patterns

## Objectives

1. Force victim to cache sensitive page
2. Enable data theft in subsequent steps
3. Achieve initial compromise via deception

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL with cacheable extension.

Example: https://subdomain.kaspersky.com/account-info.css

> This tricks the cache into storing the /account-info page as CSS.

### Step 2: Distribute Phishing Link

**Context**: Send the link via email or messaging.

Craft a convincing message to entice the user to click.

> Expected: User visits and caches the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- phishing
- web-cache-deception
