---
id: proc-uuid-002
tags:
  - open-redirect
  - phishing
  - web
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
updated_at: '2025-12-14T17:24:31.749Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Open-Redirect-Payload-on-dev-twitter-com

## Summary

This procedure crafts a malformed URL to bypass validation and redirect users to arbitrary external sites via the Location header on dev.twitter.com.

## Description

Due to lack of target URL validation, encoded URIs like https:/%5c allow external redirects. Works in Chrome, Firefox, Opera by exploiting URI parsing. Scenario: Lure user to click the crafted link for phishing. Outcome: User redirected to malicious site, bypassing same-origin checks.

## Requirements

1. Knowledge of URL encoding (%5c for \)
2. Browser for testing
3. Target external domain under control

## Defense

Defensive measures and detection strategies:

- Validate redirect targets against whitelist
- Log and alert on external redirects
- Use referrer checks on destination sites

## Objectives

1. Achieve 302 to external domain
2. Confirm cross-browser compatibility
3. Demonstrate phishing potential

## Instructions

### Step 1: Encode Malformed URL

**Context**: Create payload using double slash and backslash encoding to trick parser.

Construct: https://dev.twitter.com/https:/%5cblackfan.ru/

### Step 2: Test Redirect

**Context**: Verify Location header points external.

Access the URL in browser or use curl:

```bash
curl -I 'https://dev.twitter.com/https:/%5cblackfan.ru/'
```

> Location: https://blackfan.ru. Browser follows to external site.

**Expected Output**: Redirect to external domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
