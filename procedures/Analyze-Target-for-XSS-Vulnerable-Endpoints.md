---
id: proc-analyze-xss-endpoints
tags:
  - xss
  - recon
  - web-vulnerability
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
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
updated_at: '2025-12-14T00:11:15.974Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Target-for-XSS-Vulnerable-Endpoints

## Summary

This procedure involves inspecting a web application's endpoints, particularly authentication-related ones like logout, to identify reflected XSS vulnerabilities where user input is echoed back without proper sanitization.

## Description

In the context of the DoD national levee database subdomain, analyze the /auth/logout.jsx endpoint to check the 'home' GET parameter for direct reflection in HTML attributes, such as link hrefs. This allows injection of javascript: URIs that execute on user click. Prerequisites include browser access to the public site; no authentication needed. Expected outcome: Confirmation of vulnerability for payload crafting.

## Requirements

1. Web browser for manual inspection
2. Network access to the target subdomain (e.g., https://████████████/)
3. Basic knowledge of HTML/JS and URL encoding

## Defense

Defensive measures and detection strategies:

- Implement output encoding for all user inputs in HTML contexts (e.g., using libraries like DOMPurify)
- Validate and whitelist allowed URI schemes in redirect parameters
- Monitor for anomalous JavaScript execution in browser logs or WAF rules

## Objectives

1. Discover unsanitized input reflection points
2. Assess potential for javascript: injection
3. Prepare for payload testing

## Instructions

### Step 1: Navigate and Inspect Logout Endpoint

**Context**: Load the target logout page and examine network requests to identify parameters.

**Instructions**: Open the browser and visit https://████████████/. Trigger a logout to capture the /auth/logout.jsx request. Use developer tools (F12) to inspect the GET parameters and response HTML.

> Look for the 'home' parameter in the query string and check if it's reflected in the page, e.g., <a href="[home value]">Return to app</a>.

### Step 2: Test Basic Reflection

**Context**: Append a benign payload to confirm reflection without execution.

**Instructions**: Modify the URL to include ?home=test and reload. View page source to verify 'test' appears unescaped in the HTML.

> If reflected directly, the vulnerability is likely present; proceed to crafting malicious payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[xss]]
- [[recon]]
