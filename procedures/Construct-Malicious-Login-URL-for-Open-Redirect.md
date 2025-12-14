---
id: proc-construct-stocky-open-redirect-url
tags:
  - open-redirect
  - url-construction
  - phishing-setup
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
updated_at: '2025-12-14T17:24:31.260Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Construct-Malicious-Login-URL-for-Open-Redirect

## Summary

This procedure involves manually crafting a login URL for the Stocky app with an unvalidated return_to parameter pointing to a malicious domain, setting the stage for an open redirect attack post-authentication.

## Description

The Stocky app's login endpoint at https://stocky.shopifyapps.com/users/login accepts a return_to parameter without validation, allowing protocol-relative URLs like //evil.com. This procedure focuses on constructing such a URL in a browser to initiate the exploit. It targets web applications vulnerable to open redirects, where attackers can lure users to the crafted link via email or other means. Expected outcome: The login page loads with the malicious parameter embedded, ready for authentication.

## Requirements

1. Web browser with developer tools enabled for URL inspection.
2. Knowledge of a controlled malicious domain (e.g., evil.com).
3. Public access to the target login page.

## Defense

Defensive measures and detection strategies:

- Implement URL validation on return_to parameters to whitelist only internal domains.
- Use Content Security Policy (CSP) to restrict redirects.
- Monitor for unusual redirect patterns in application logs.

## Objectives

1. Prepare a functional login URL with embedded malicious redirect.
2. Ensure the parameter bypasses any basic checks.
3. Position for post-login exploitation.

## Instructions

### Step 1: Build the Target URL

**Context**: Append the return_to parameter to the base login URL using a protocol-relative scheme to evade simple protocol checks.

No command required; manually enter in browser address bar:

```plaintext
https://stocky.shopifyapps.com/users/login?return_to=//evil.com
```

> This loads the login page. Verify in the browser's address bar or network tab that the parameter is present and unaltered.

### Step 2: Verify Parameter Acceptance

**Context**: Confirm the page renders without errors, indicating the parameter is accepted.

Inspect the page source or use browser dev tools to ensure return_to is not stripped.

> Expected: Login form displays normally; no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- url-manipulation
