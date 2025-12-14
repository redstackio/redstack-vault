---
tags:
  - response-tampering
  - intercept
  - bypass-redirect
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T03:15:41.741Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6b9ee2a6-1d2c-4c14-bba1-b505b0ca81d2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-and-Modify-HTTP-Response-to-Remove-Redirect

## Summary

This procedure uses Burp Suite to intercept the HTTP response from the vulnerable /mission.php endpoint and remove redirection elements, preventing the page from navigating away before the reflected XSS payload executes.

## Description

The DoD application's response includes a redirect (e.g., meta refresh or JavaScript location.href) that interrupts payload execution. By tampering with the response body in Burp Suite, the redirect is excised, allowing the SVG onload event to fire and execute the alert or further JavaScript in the browser context.

## Requirements

1. Active Burp Suite interception from prior payload injection
2. Intercepted request from /mission.php with XSS payload
3. Knowledge of response structure (e.g., location of redirect code)

## Defense

Defensive measures and detection strategies:

- Validate response integrity with checksums or signed responses
- Log and alert on proxy-intercepted or modified traffic in WAF
- Enforce strict redirect policies and sanitize all reflected content

## Objectives

1. Neutralize the redirect to enable payload execution
2. Maintain session integrity during modification
3. Set up for immediate verification of XSS

## Instructions

### Step 1: Intercept the Response

**Context**: Switch Burp to intercept the response after the server processes the request.

In Burp Suite, right-click the intercepted request and select 'Do intercept -> Response to this request'.

> This halts the response; inspect the body for redirect elements like `<meta http-equiv="refresh" content="0; url=...">` or `window.location = '...'`.

### Step 2: Edit and Remove Redirect

**Context**: Manually delete the redirect code from the response body.

In the response editor, locate and excise the redirection (e.g., delete the entire meta tag or JS redirect line), then click 'Forward'.

> Expected: Clean response body without redirect; the reflected 'ped' parameter content now renders directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[response-tampering]]
- [[bypass-redirect]]
