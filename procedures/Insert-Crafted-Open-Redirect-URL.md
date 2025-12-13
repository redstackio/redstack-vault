---
tags:
  - open-redirect
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2cecf987-4c21-4586-a7ea-e753042a54ac
created_at: '2025-12-13T09:01:26.458Z'
updated_at: '2025-12-13T09:01:26.458Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Insert Crafted Open Redirect URL

## Summary

This procedure involves crafting and inserting a URL with a double slash to exploit an open redirection vulnerability in a web endpoint, specifically bypassing validation in SSO-SAML sign-in.

## Description

The procedure targets insufficient URL validation in the HackerOne SSO-SAML endpoint. By inserting a double slash in the path, the attack bypasses a previous patch, allowing redirection to external sites without warnings. This is useful in scenarios where attackers aim to redirect users to phishing pages. The target environment is a web platform with SSO-SAML services, and the expected outcome is a clickable link that sets up the redirection.

## Requirements

1. Access to insert links in comments or reports on the target platform
2. Knowledge of the vulnerable endpoint URL
3. Basic web browser or HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation with improved regex to catch double slashes
- Monitor for suspicious URL patterns in user-submitted content

## Objectives

1. Set up the exploit by inserting the crafted URL
2. Prepare for user interaction to trigger redirection
3. Enable potential phishing without warnings

## Instructions

### Step 1: Craft the URL

**Context**: Create the URL with double slash to bypass validation.

**Command** ([[commands/curl-test-open-redirect]]):
```bash
curl -I 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
```

> This command tests the URL header to ensure it resolves without errors.

### Step 2: Insert into Comment or Report

**Context**: Add the URL to user-generated content on the platform.

Insert the following URL: https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true

> No specific command needed; perform this via the web interface. Expected: Link is saved successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-open-redirect]]

## Tools Used



## Tags

- [[open-redirect]]
- [[url-crafting]]
