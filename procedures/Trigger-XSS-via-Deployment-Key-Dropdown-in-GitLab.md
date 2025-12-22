---
id: proc-trigger-gitlab-xss
tags:
  - xss
  - csp-bypass
  - gitlab
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.937Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Deployment-Key-Dropdown-in-GitLab

## Summary

This procedure triggers the XSS by interacting with the 'Allowed to push' dropdown in GitLab's protected branches settings, causing jQuery to render the malicious deployment key title and execute the injected script, bypassing CSP.

## Description

The dropdown uses jQuery's HTML insertion methods (e.g., .html() or .append()) to populate options with deployment key titles fetched from the server. Since the title is unsanitized, the script tag executes as part of the DOM, evading 'strict-dynamic' CSP because jQuery is a trusted parser. This allows arbitrary JS like domain alerts or API requests to private repos. Impacts include session-based attacks if the victim is an admin.

## Requirements

1. Malicious deployment key already injected.
2. Protected branches section expanded.
3. Victim or attacker session active on the page.

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered user inputs server-side before database storage or client rendering.
- Replace jQuery with safer DOM manipulation libraries or use textContent instead of innerHTML.
- Enable CSP reporting to log and block dynamic script executions; audit for 'unsafe-inline' fallbacks.

## Objectives

1. Execute injected JavaScript in the victim's browser context.
2. Bypass CSP restrictions for arbitrary code run.
3. Demonstrate potential for resource access or data theft.

## Instructions

### Step 1: Interact with Dropdown

**Context**: Click the dropdown to force loading and rendering of deployment key options, executing the payload.

In the protected branches form, locate the 'Allowed to push' field and click the dropdown arrow to open it.

> Expected output: The dropdown populates, and the script executes immediately—e.g., an alert pops up with the domain name. Check browser console for JS errors or network tabs for any unauthorized requests. CSP headers should not block due to 'strict-dynamic' and jQuery trust.

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
- [[csp-bypass]]
- [[gitlab]]
- [[JavaScript]]
