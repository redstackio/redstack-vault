---
id: proc-trigger-stocky-redirect
tags:
  - redirect-trigger
  - open-redirect
  - phishing-execution
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
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:31.249Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Trigger-Post-Login-Redirect-to-Malicious-Site

## Summary

This procedure executes the open redirect by completing authentication, causing the Stocky app to navigate to the attacker-controlled site specified in return_to, enabling phishing or session hijacking.

## Description

Upon successful login, the app's redirect logic blindly follows the return_to parameter, allowing external URLs. This leads to the victim landing on a malicious page that can mimic the app or capture data. The attack scenario involves luring users to the crafted login link. Expected outcomes: Unblocked redirect to //evil.com, potential exposure of session tokens in referer headers.

## Requirements

1. Successful prior authentication.
2. Malicious site hosted and ready (e.g., evil.com with phishing page).
3. Browser allowing redirects.

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist of allowed domains.
- Strip or encode user-controlled redirect parameters server-side.
- Use referrer policy to limit leaked data during redirects.

## Objectives

1. Confirm redirect execution without validation.
2. Land on malicious site post-login.
3. Facilitate downstream phishing.

## Instructions

### Step 1: Observe Automatic Redirect

**Context**: After form submission, the app handles the redirect based on return_to.

No manual action; browser follows the 302.

> Check address bar: Changes from stocky.shopifyapps.com to evil.com. Use dev tools to inspect Location header.

### Step 2: Validate Malicious Site Load

**Context**: Ensure the redirect completes and the phishing page loads.

Monitor for any errors or blocks; confirm session cookies are sent to evil.com.

> Expected: Full page load of malicious domain; potential phishing form or data capture.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- redirect
- exploitation
