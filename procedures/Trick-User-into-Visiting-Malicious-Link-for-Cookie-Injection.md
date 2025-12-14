---
id: proc-trick-user-malicious-link
tags:
  - phishing
  - cookie-injection
  - google-analytics
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
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
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:27:57.514Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[T1566.001]]'
---
# Trick-User-into-Visiting-Malicious-Link-for-Cookie-Injection

## Summary

This procedure uses social engineering to lure an authenticated user to a malicious URL that exploits Google Analytics' __utmz cookie setting to inject a forged CSRF token via unfiltered referer paths.

## Description

The attack relies on crafting a URL where the referer includes delimiters like ']' in the path, causing Google Analytics to set __utmz with injected 'csrftoken=x'. This persists for 6 months. Target: Sites with GA integration. Prerequisites: User authenticated on target.

## Requirements

1. Control over a domain or URL shortener for the malicious link
2. Knowledge of target domain (e.g., .instagram.com)
3. Social engineering vector (email, message)

## Defense

Defensive measures and detection strategies:

- Sanitize referer headers in analytics scripts
- Disable or filter GA cookie setting for user-controlled inputs
- Educate users on phishing links

## Objectives

1. User visits malicious link
2. __utmz cookie injected with forged token
3. Token persists across sessions

## Instructions

### Step 1: Craft Malicious URL

**Context**: Build URL using referer manipulation with delimiter.

Example URL: `http://blackfan.ru/r/,%5Dcsrftoken=x,;domain=.instagram.com;path=/;...;?r=http://blog.instagram.com/`

> Explanation: The %5D (']') in path acts as delimiter when GA sets __utmz.

### Step 2: Distribute Link

**Context**: Send via phishing to authenticated user.

Embed in email or message.

> Expected: User clicks, triggering cookie set on target domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[Phishing]]
- [[cookie-injection]]
- [[google-analytics]]
