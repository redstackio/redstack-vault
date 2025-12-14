---
tags:
  - javascript-analysis
  - url-vulnerability
  - code-review
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:27:29.145Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 46ebb3bb-b587-43d7-a199-15b139554e7c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Software]]'
---
---

# Analyze JavaScript for URL Manipulation Vulnerabilities

## Summary

This procedure involves inspecting GitLab's client-side JavaScript code to identify flaws in URL construction, specifically the unsafe use of `location.pathname` that allows manipulation via forged links, leading to potential CSRF token leakage.

## Description

In GitLab instances, JavaScript files like `environments_folder_view.js` construct relative URLs for AJAX requests using `location.pathname` without validation. This can be exploited by links starting with '//' to resolve to external domains. The procedure targets self-hosted or source-accessible GitLab installations, revealing how authenticity_tokens are included in requests, enabling remote leakage when requests are redirected.

## Requirements

1. Access to GitLab source code or a running instance for browser inspection
2. Browser developer tools (e.g., Chrome DevTools) for JS analysis
3. Knowledge of JavaScript and URL resolution rules

## Defense

Defensive measures and detection strategies:

- Validate all constructed URLs against the current origin before sending requests
- Use Content Security Policy (CSP) to restrict AJAX endpoints
- Monitor for unusual outbound requests from GitLab JS

## Objectives

1. Identify vulnerable URL construction patterns in JS code
2. Document inclusion of sensitive tokens like authenticity_token
3. Assess potential for external domain redirection

## Instructions

### Step 1: Access and Inspect JavaScript Files

**Context**: Locate and examine key JS files in the GitLab installation to find URL building logic.

Open the GitLab instance in a browser and use DevTools to view source files. Search for `environments_folder_view.js` and navigate to lines 21 and 86, where `location.pathname` is concatenated to form request URLs.

### Step 2: Analyze AJAX Request Construction

**Context**: Verify how requests are sent and what data is included.

Trace the code to see usage of `Vue.http` or `$.ajax` for requests. Confirm that the Rails authenticity_token (from meta tags) is attached to these requests, making it leachable if the URL is manipulated.

### Step 3: Test URL Manipulation Potential

**Context**: Simulate forged URL resolution to confirm vulnerability.

In the console, test constructing a URL with a manipulated pathname, e.g., set `location.pathname` temporarily and observe if it forms an absolute external URL when prefixed with '//'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[javascript-analysis]]
- [[url-vulnerability]]
- [[code-review]]
