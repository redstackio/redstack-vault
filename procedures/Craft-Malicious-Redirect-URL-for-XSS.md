---
id: craft-xss-redirect-url
tags:
  - xss
  - url-manipulation
  - javascript-uri
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
updated_at: '2025-12-13T23:52:49.833Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Redirect-URL-for-XSS

## Summary

This procedure constructs a malicious URL targeting the redirect_url parameter in the Acronis licensing-check endpoint, injecting a javascript: URI scheme to enable XSS payload delivery.

## Description

The vulnerability stems from the lack of validation on the redirect_url parameter at https://learn.acronis.com/portal/licensing-check, allowing schemes like javascript: to execute code in the browser. This step prepares the payload, such as alert(document.domain) for testing, which can be escalated to steal cookies or perform actions. It requires an active session from prior authentication.

## Requirements

1. Authenticated session to the Acronis portal
2. Knowledge of the target endpoint (/portal/licensing-check)
3. Web browser or URL encoder for payload crafting

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed redirect schemes (e.g., http/https only)
- Sanitize parameters to block javascript: URIs
- Log and monitor unusual parameter values in redirects

## Objectives

1. Create a valid injectable URL payload
2. Ensure the javascript: scheme bypasses any basic checks
3. Prepare for execution without alerting the application

## Instructions

### Step 1: Identify Base Endpoint

**Context**: Start with the vulnerable URL structure.

Use the base: https://learn.acronis.com/portal/licensing-check?

> Append the parameter for manipulation.

### Step 2: Inject Payload

**Context**: Embed the JavaScript code via javascript: scheme.

Construct: redirect_url=javascript:alert(document.domain)

Full URL: https://learn.acronis.com/portal/licensing-check?redirect_url=javascript:alert(document.domain)

> Encode if needed (e.g., %3A for :), but raw works for testing. Verify in browser address bar.

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
- [[url-manipulation]]
- [[javascript-uri]]
