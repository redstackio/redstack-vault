---
id: proc-uuid-placeholder-001
tags:
  - xss
  - html-injection
  - oidc
  - validation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.100Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-State-Parameter-Validation-Issue

## Summary

This procedure tests for insufficient filtering of the state parameter in OIDC form_post response mode, allowing HTML injection that can lead to further exploitation like token theft.

## Description

In OIDC authentication flows using form_post, the state parameter is reflected into the response body without proper sanitization, enabling attackers to inject HTML elements. This is particularly dangerous in authentication contexts where access tokens are present. The procedure involves intercepting and tampering with requests to verify if HTML renders unsafely, setting the stage for payload injection. Prerequisites include access to the authentication endpoint and a proxy tool for request manipulation. Expected outcomes include confirmation of the flaw, with impacts limited by CSP but enabling chained attacks.

## Requirements

1. Proxy tool like Burp Suite for request interception
2. Ability to initiate OIDC login flow
3. Browser with developer tools for response inspection

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping for state parameter
- Enforce CSP to block inline scripts, though HTML injection may still occur
- Monitor for anomalous requests to authentication endpoints with unusual state values

## Objectives

1. Confirm lack of filtering in state parameter
2. Verify HTML injection renders in response body
3. Assess CSP impact on exploitation

## Instructions

### Step 1: Intercept OIDC Authentication Request

**Context**: Start the authentication flow to capture the request containing the state parameter.

Use Burp Suite to proxy traffic and intercept the POST to the OIDC endpoint.

### Step 2: Tamper with State Parameter

**Context**: Modify the state to include test HTML and submit to check reflection.

In the intercepted request, alter the state parameter to `<img src=x onerror=alert(1)>` and forward the request.

> Inspect the form_post response in the browser; if the HTML executes or renders (e.g., alert pops or image breaks), the vulnerability exists. Note any CSP blocks on script but allows HTML.

### Step 3: Validate Response Rendering

**Context**: Confirm injection without full XSS due to mitigations.

Examine the response body for unescaped HTML presence.

> Successful output: State value appears as raw HTML in the form, injectable for elements like buttons.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[html-injection]]
- [[oidc]]
