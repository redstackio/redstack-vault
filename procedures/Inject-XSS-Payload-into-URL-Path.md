---
id: proc-uuid-2
tags:
  - xss
  - javascript
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.531Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into URL Path

## Summary

This procedure exploits a reflected XSS vulnerability by injecting a malicious JavaScript payload into the path of a user-supplied URL, causing the server to fetch and render it unsanitized, leading to script execution in the victim's browser.

## Description

The vulnerability arises when a web server fetches content from a user-controlled URL and renders the path directly into the HTML response without escaping. By embedding an XSS payload like an onerror handler in an img tag within the path, the script executes upon rendering. This was demonstrated on an endpoint like https://█████/████&url=, where the path triggers JavaScript via XMLHttpRequest responses.

## Requirements

1. Identified vulnerable endpoint from prior reconnaissance
2. Ability to craft and submit HTTP requests with custom URLs
3. Victim access to the rendered page (authenticated session enhances impact)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user-supplied content before rendering
- Implement strict URL path validation and stripping of script tags
- Use browser security headers like CSP to block inline scripts

## Objectives

1. Inject and execute arbitrary JavaScript
2. Confirm XSS without direct CSRF capability
3. Set up for chaining with UI manipulation techniques

## Instructions

### Step 1: Craft Malicious URL

**Context**: Build a URL with an XSS payload in the path to exploit rendering flaws.

No command; manually construct: http://galnagli.com/<img src=x onerror=alert(document.domain)> as the url parameter value.

> This payload uses an invalid src to trigger onerror, executing the alert on the current domain.

### Step 2: Submit and Verify Execution

**Context**: Send the payload via the vulnerable endpoint and observe browser behavior.

Submit via GET: https://█████/████&url=http://galnagli.com/<img src=x onerror=alert(document.domain)>. Load the response in a browser.

> Expected output: Alert box pops up showing the domain, confirming JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
- [[injection]]
