---
id: proc-uuid-1
tags:
  - csrf
  - token-extraction
  - web-recon
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:15.261Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Extract-CSRF-Token-from-Liberapay-Sign-in-Page

## Summary

This procedure involves accessing the Liberapay sign-in page and using browser developer tools to extract the CSRF token, which can then be reused in a malicious form to bypass protections on the profile edit endpoint.

## Description

In the context of a CSRF attack on Liberapay, the sign-in page exposes a CSRF token that is not sufficiently bound to the session or origin, allowing extraction via inspection. This token is required for POST requests to sensitive endpoints like profile editing. The procedure targets https://liberapay.com/sign-in?back_to=/ and assumes the attacker has no authentication, making it a low-barrier reconnaissance step. Expected outcome is obtaining a valid token string for subsequent exploitation.

## Requirements

1. Web browser with developer tools enabled (e.g., Chrome, Firefox)
2. Internet access to reach Liberapay's public sign-in page
3. Basic knowledge of HTML inspection

## Defense

Defensive measures and detection strategies:

- Implement SameSite=Strict cookies for CSRF tokens to prevent cross-site reuse
- Bind tokens to user sessions and validate origin headers on POST endpoints
- Monitor for anomalous token extractions via web application firewall (WAF) logs

## Objectives

1. Retrieve a functional CSRF token from the public sign-in page
2. Enable reuse in cross-origin requests without invalidation
3. Prepare for forging requests to protected endpoints

## Instructions

### Step 1: Navigate to Sign-in Page

**Context**: Load the Liberapay sign-in page to access the embedded CSRF token in the HTML.

Navigate to https://liberapay.com/sign-in?back_to=/ in your web browser.

> This loads the page with the form containing the token. No authentication is needed.

### Step 2: Inspect Page Source

**Context**: Use developer tools to locate and copy the CSRF token value.

Right-click on the page and select "Inspect" or press F12. Search for "csrf_token" in the Elements tab or view the page source (Ctrl+U). Look for an input field like <input type="hidden" name="csrf_token" value="APJk0T5NR7Ut5q4mABPvh61Az8Ro1NtE">. Copy the value attribute.

> Expected output: A 32-character hexadecimal token string. If not visible in HTML, check network requests in the Network tab for any AJAX calls exposing it.

### Step 3: Validate Token

**Context**: Optionally test the token in a non-malicious request to ensure validity.

Use the browser console to log the token or make a simple fetch request to a GET endpoint if needed, but for this attack, direct copy suffices.

> Success: Token copied without errors; it should match the format observed in Liberapay's forms.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
