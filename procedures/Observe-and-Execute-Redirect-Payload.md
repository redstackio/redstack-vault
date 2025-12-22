---
id: proc-uber-observe-redirect
tags:
  - xss
  - redirect-execution
  - browser-vuln
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:35.188Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-and-Execute-Redirect-Payload

## Summary

This procedure monitors the post-interaction response from the OAuth endpoint, identifying intermediate redirect pages, and executes the javascript: payload by clicking links or allowing auto-redirects in vulnerable browsers.

## Description

After consent interaction, the server may serve an HTML page with 'Redirecting...' and a <a> link to the malicious URI, or directly issue the redirect. In browsers like older Mozilla/Firefox or Opera Mini, clicking the link or auto-handling executes the JS. This step confirms payload delivery and execution, potentially leading to data exfiltration.

## Requirements

1. Vulnerable browser (Opera Mini, Firefox 302 disabled, older Mozilla)
2. Access to developer tools for inspecting responses
3. Prior steps completed (URL visit and interaction)

## Defense

Defensive measures and detection strategies:

- Avoid serving intermediate redirect pages; use meta-refresh or JS redirects with validation
- Block javascript: URIs in link hrefs via server-side rendering
- Detect unusual browser agents or redirect patterns in access logs
- Patch browsers to prevent JS execution from Location headers

## Objectives

1. Identify redirect response format
2. Trigger payload execution manually or automatically
3. Verify XSS impact (e.g., alert popup)

## Instructions

### Step 1: Inspect Post-Interaction Response

**Context**: Use browser dev tools to observe the server's response after clicking Allow/Deny.

Open Network tab in dev tools; click the button and check the response.

> Expected: 302 with Location: javascript://... or HTML page with redirect link.

### Step 2: Execute the Payload

**Context**: Interact with the redirect page to run the JS.

If 'Redirecting...' page appears, click the link to the javascript: URI; in auto-redirect browsers, wait for execution.

> Expected: JS alert shows document.domain; console logs payload success.

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
- [[redirect-execution]]
- [[browser-vuln]]
