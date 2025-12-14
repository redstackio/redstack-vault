---
tags:
  - link-compromise
  - token-leakage
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f672ae5c-e278-4398-9bf2-9f0e3c467ca5
created_at: '2025-12-14T17:28:58.785Z'
updated_at: '2025-12-14T17:28:58.785Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Compromise-Reset-Link

## Summary

This procedure exploits exposure of the password reset link, such as through referrer token leakage, allowing an attacker to obtain the link without legitimate access to the email.

## Description

In the Legal Robot vulnerability, the reset link could be leaked via browser referrers or other implementation flaws, enabling unauthorized acquisition. This step assumes the attacker has identified the leakage vector. Outcomes include possession of a valid, unauthenticated reset token. Requires monitoring for leaks in web traffic or logs.

## Requirements

1. Identification of leakage mechanism (e.g., referrer headers)
2. Tools or access to intercept web requests (e.g., proxy like Burp Suite)
3. The reset link generated from prior step

## Defense

Defensive measures and detection strategies:

- Bind reset tokens to user sessions or IP addresses
- Avoid exposing tokens in referrers or logs
- Use HTTPS and HSTS to prevent interception

## Objectives

1. Acquire the reset link illicitly
2. Verify link validity without authentication
3. Enable password change

## Instructions

### Step 1: Identify Leakage Vector

**Context**: Determine how the reset link is exposed in the application's flow.

Inspect network traffic or application behavior for referrer token leakage during the reset process.

> For example, if the link is shared or logged insecurely, capture it from browser developer tools or proxy intercepts.

### Step 2: Extract and Validate Link

**Context**: Secure the link and test its accessibility.

Copy the full reset URL from the leakage source.

> Attempt to open the link in an incognito browser window to confirm it loads the reset form without requiring login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-leakage]]
- [[web-vuln]]
