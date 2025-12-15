---
id: proc-001
tags:
  - open-redirect
  - recon
  - nordvpn
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:34.711Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Open-Redirect-in-NordVPN-Support

## Summary

This procedure involves analyzing the client-side JavaScript on the NordVPN support website to identify an open redirect vulnerability where URLs starting with '#/path' trigger unconditional redirects to arbitrary external domains.

## Description

The NordVPN support site, powered by NanoRep, uses hash-based routing in JavaScript. Without proper validation, the code processes the path after '#/path' by slicing the string after the first 6 characters and setting window.location.href, allowing redirects to any domain. This can be discovered by inspecting the site's source code or testing URL patterns, enabling attackers to chain it with social engineering for phishing.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Public internet access to https://support.nordvpn.com
3. Basic knowledge of JavaScript and URL manipulation

## Defense

Defensive measures and detection strategies:

- Implement URL validation in client-side redirects to whitelist allowed domains.
- Use server-side redirects instead of client-side to enforce security checks.
- Monitor for unusual redirect patterns in web logs or browser security tools like CSP.

## Objectives

1. Confirm the presence of unvalidated redirect logic in the JavaScript.
2. Document the exact URL pattern that triggers the vulnerability.
3. Assess potential for exploitation in phishing scenarios.

## Instructions

### Step 1: Inspect the Support Site

**Context**: Load the NordVPN support page and examine the JavaScript responsible for handling hash routes.

Open https://support.nordvpn.com in your browser, right-click and select "Inspect Element," then navigate to the Sources or Console tab. Search for code handling '#/path' or window.location assignments.

> Look for JavaScript that extracts the path after '#/path' + 6 and redirects without checking the origin.

### Step 2: Test Basic URL Patterns

**Context**: Manually test hash URLs to observe redirect behavior.

In the browser address bar, modify the URL to https://support.nordvpn.com/#/path/test and observe if it attempts any navigation. Then try https://support.nordvpn.com/#/path///example.com to see if it redirects externally.

> Expected behavior: The browser navigates to example.com, confirming the open redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[web-vulnerability]]
- [[nordvpn]]
