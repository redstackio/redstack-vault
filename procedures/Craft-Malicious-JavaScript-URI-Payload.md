---
id: proc-craft-js-uri-payload
tags:
  - xss
  - payload-crafting
  - javascript-uri
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
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
updated_at: '2025-12-14T00:11:15.968Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-javascript-URI-Payload

## Summary

This procedure crafts a URL payload exploiting the reflected 'home' parameter to inject a javascript: URI scheme, setting up for client-side code execution without immediate triggering.

## Description

Targeted at the DoD /auth/logout.jsx endpoint, encode a JavaScript payload (e.g., alert or exfiltration script) into the 'home' parameter using URL encoding. The payload reflects into a link on the logout page. Visiting the URL loads the page with the injection, but execution requires further interaction. Prerequisites: Confirmed vulnerable endpoint from reconnaissance.

## Requirements

1. Knowledge of URL encoding (%27 for ')
2. Browser for testing
3. Target URL access

## Defense

Defensive measures and detection strategies:

- Strip or block javascript: schemes in URI parameters
- Use Content Security Policy (CSP) to restrict inline scripts
- Log and alert on suspicious parameter values in access logs

## Objectives

1. Inject executable JavaScript via URI scheme
2. Ensure payload survives reflection
3. Test for execution potential

## Instructions

### Step 1: Encode the Payload

**Context**: Create the JavaScript code to inject, such as a simple alert for proof-of-concept.

**Instructions**: Write the JS: alert('XSS Success!'). Wrap in javascript: URI: javascript:alert('XSS Success!')(). URL-encode: javascript%3A(alert(%27XSS%20Success!%27))%28%29.

> Use an online encoder or browser console to verify.

### Step 2: Construct and Visit URL

**Context**: Append the encoded payload to the endpoint.

**Instructions**: Form the full URL: https://████████████/auth/logout.jsx?home=javascript%3A(alert(%27XSS%20Success!%27))%28%29. Paste into browser address bar and load.

> Page should load with the payload in the source; no execution yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[xss]]
- [[payload-crafting]]
