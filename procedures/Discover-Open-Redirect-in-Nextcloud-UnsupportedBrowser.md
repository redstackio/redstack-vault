---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - open-redirect
  - nextcloud
  - phishing
  - code-review
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
updated_at: '2025-12-14T17:24:30.490Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Discover-Open-Redirect-in-Nextcloud-UnsupportedBrowser
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]]
techniques: [[Exploit Public-Facing Application]], [[T1566.002]]
sub_techniques: []
tags: [open-redirect, nextcloud, phishing, code-review]
commands: []
platforms: [Web]
tools: []
---

# Discover-Open-Redirect-in-Nextcloud-UnsupportedBrowser

## Summary

This procedure outlines the process of reviewing Nextcloud's source code to identify and exploit an open redirect vulnerability in the UnsupportedBrowser.vue component, where the redirect_url parameter is base64-decoded and used for redirection without validation, enabling phishing attacks by redirecting users to arbitrary sites.

## Description

In Nextcloud, the UnsupportedBrowser.vue component handles browser compatibility warnings and includes logic to redirect users based on a redirect_url query parameter. The parameter is base64-decoded and directly assigned to window.location without any validation, such as checking for trusted domains or relative paths. This allows attackers to craft URLs that, when loaded in an unsupported browser or triggered via the warning page, redirect victims to malicious sites for phishing or social engineering. The vulnerability was found by static code analysis on GitHub, and exploitation requires no authentication, making it suitable for drive-by or link-based attacks on Nextcloud users.

## Requirements

1. Access to the Nextcloud GitHub repository for source code review
2. A web browser to test the crafted URLs
3. Basic knowledge of JavaScript, base64 encoding, and URL manipulation
4. Publicly accessible Nextcloud instance to trigger the warning page

## Defense

Defensive measures and detection strategies:

- Implement URL validation in frontend code to restrict redirects to the same domain or whitelisted hosts
- Use Content Security Policy (CSP) headers to block unsafe navigations
- Monitor for unusual redirect patterns in web logs, such as base64-encoded parameters leading to external domains
- Educate users on phishing risks and verify URLs before clicking

## Objectives

1. Identify the open redirect flaw through code review
2. Confirm the vulnerability by analyzing redirection logic
3. Construct and test a proof-of-concept to demonstrate phishing potential
4. Redirect users to attacker-controlled sites for social engineering

## Instructions

### Step 1: Review Source Code

**Context**: Locate and examine the UnsupportedBrowser.vue component to understand the vulnerable redirection logic.

Navigate to the Nextcloud GitHub repository (https://github.com/nextcloud/server) and search for UnsupportedBrowser.vue in the apps/files/src/components directory. Inspect the JavaScript code that parses the URL query parameters, specifically the handling of redirect_url.

> The code typically looks like: const urlParams = new URLSearchParams(window.location.search); const encodedRedirect = urlParams.get('redirect_url'); if (encodedRedirect) { const redirectPath = atob(encodedRedirect); window.location = redirectPath; } Note the use of atob() for base64 decoding and direct assignment without validation.

### Step 2: Identify the Vulnerability

**Context**: Analyze the code to confirm the lack of sanitization, enabling arbitrary redirects.

Review the redirection mechanism: the decoded value is assigned to window.location without checks for protocol (e.g., http/https), domain matching, or path restrictions. This allows external URLs like http://evil.com to be set directly.

> Expected outcome: Documentation of the root cause as insufficient input validation on the base64-decoded parameter.

### Step 3: Construct and Test Proof-of-Concept

**Context**: Build a malicious URL and verify the redirect in a browser.

Encode a target external URL in base64, e.g., using an online tool or JavaScript console: btoa('http://attacker.com/phishing-page'). Append it to the Nextcloud warning URL: https://nextcloud.example.com/apps/files/?redirect_url=<base64-string>. Load the URL in an unsupported browser (e.g., simulate via dev tools) or directly if the page triggers.

> Expected outcome: The browser redirects to the attacker site, confirming the open redirect. Use browser dev tools to inspect network requests and verify no validation occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1566.002]] Phishing: Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[nextcloud]]
- [[Phishing]]
- [[code-review]]
