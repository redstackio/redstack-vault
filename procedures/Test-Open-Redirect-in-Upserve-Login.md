---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Test-Open-Redirect-in-Upserve-Login
tags:
  - open-redirect
  - phishing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:34.998Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Test-Open-Redirect-in-Upserve-Login

## Summary

This procedure tests for an open redirect vulnerability in the Upserve Inventory App login page by appending arbitrary external URLs to the path, allowing redirection to malicious sites for phishing without proper validation.

## Description

The Upserve Inventory App login page at https://inventory.upserve.com processes URL paths as redirect targets, enabling attackers to craft links like https://inventory.upserve.com/http://evil-site.com. This bypasses any intended login flow and redirects users to external domains. A similar flaw exists in the 'Cancel' button link. In an attack scenario, an attacker sends a phishing email with this crafted URL, tricking users into clicking and being redirected to a fake login page that steals credentials. The target environment is a web application, and success is confirmed by observing the redirect in browser dev tools or HTTP responses. Prerequisites include internet access and a tool to send HTTP requests.

## Requirements

1. Network access to https://inventory.upserve.com
2. Web browser or HTTP client like curl
3. No authentication required for testing

## Defense

Defensive measures and detection strategies:

- Implement URL validation to whitelist allowed domains or block external redirects
- Use Content Security Policy (CSP) headers to restrict navigation
- Monitor access logs for suspicious URL paths containing external domains
- Educate users on phishing risks and verify links before clicking

## Objectives

1. Confirm open redirect by testing crafted URLs
2. Demonstrate phishing potential through redirection
3. Identify lack of input sanitization in path handling

## Instructions

### Step 1: Craft Malicious URL

**Context**: Build a test URL by injecting an external domain into the path to check if the application redirects without validation.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -I -L "https://inventory.upserve.com/http://google.com/"
```

> This command follows redirects (-L) and shows headers (-I). Expected output includes a 302 status with Location: http://google.com, confirming the vulnerability.

### Step 2: Verify in Browser

**Context**: Manually test the redirect in a browser to observe user-facing behavior, including any UI elements like the Cancel button.

**Instructions**: Open https://inventory.upserve.com/http://evil-phish-site.com in a browser. Check dev tools (Network tab) for the redirect response. Inspect the page source or elements for the Cancel button href attribute, which may also allow arbitrary redirects.

> Successful execution shows automatic navigation to the external site, mimicking a phishing lure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1566.002]] Phishing: Spearphishing Link

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect]]

## Tools Used


## Tags

- open-redirect
- phishing
- web-vulnerability
