---
id: proc-open-redirect-001
tags:
  - open-redirect
  - phishing
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:50.086Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Test-Open-Redirect-via-X-Forwarded-Host

## Summary

This procedure tests for open redirect vulnerability by setting the X-Forwarded-Host to an external domain, allowing attackers to redirect users to malicious sites during flows like sign-in, enabling phishing attacks.

## Description

The Omise server trusts the X-Forwarded-Host for redirect construction without validation, particularly in authentication flows. Using a simple payload like 'bing.com' redirects to external sites. This chains with XSS for more sophisticated attacks but stands alone for phishing. Repeat prior capture and modification steps, then interact with the page.

## Requirements

1. Captured and modifiable request in Burp
2. Access to site elements like 'Sign in' button
3. External domain for testing (e.g., bing.com)

## Defense

Defensive measures and detection strategies:

- Whitelist allowed hosts for redirects and validate against them
- Use absolute URLs with domain checks in redirect logic
- Monitor redirect logs for external domain attempts

## Objectives

1. Manipulate header to specify external redirect
2. Trigger and observe unwanted navigation
3. Demonstrate phishing potential

## Instructions

### Step 1: Modify Header for Redirect

**Context**: Simplify payload for redirect test.

No command; edit in Repeater:
- Set X-Forwarded-Host: bing.com in the request headers.

> This prepares the request to influence redirect behavior.

### Step 2: Send and Interact

**Context**: Execute and verify redirection.

No command; browser interaction:
- Send from Repeater, then in the browser, click 'Sign in' or similar to trigger flow.

> Expected: Page redirects to https://bing.com instead of internal Omise paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[open-redirect]]
- [[Phishing]]
