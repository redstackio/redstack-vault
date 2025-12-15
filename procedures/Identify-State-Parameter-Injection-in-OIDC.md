---
id: uuid-proc-1
tags:
  - xss
  - oidc
  - injection
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.607Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-State-Parameter-Injection-in-OIDC

## Summary

This procedure detects insufficient filtering of the state parameter in OIDC authentication flows using form_post response mode, allowing HTML characters to be injected into the response body without sanitization.

## Description

In World ID OIDC, the state parameter is used to maintain context during authentication but lacks proper validation, enabling attackers to inject HTML that renders in the callback form. This was discovered during a HackerOne meetup and serves as an entry point for further XSS exploitation. The procedure involves testing the parameter for injection flaws in a web-based authentication environment, with outcomes including confirmation of the vulnerability for chaining into token theft.

## Requirements

1. Access to initiate OIDC authentication flow (e.g., via browser or proxy like Burp Suite)
2. Knowledge of the target OIDC endpoint URL
3. Ability to intercept and modify HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping for state parameters
- Enforce Content Security Policy (CSP) to block inline scripts and unauthorized fetches
- Monitor authentication logs for anomalous state values containing HTML tags

## Objectives

1. Confirm HTML injection capability in state parameter
2. Identify response mode (form_post) as vulnerable
3. Prepare for payload injection in subsequent steps

## Instructions

### Step 1: Initiate Authentication Flow

**Context**: Start the OIDC process to access the state parameter in the authorization request.

Navigate to the World ID OIDC authorization endpoint, e.g., `https://worldid.com/auth?client_id=...&response_type=code&scope=openid&state=test&response_mode=form_post`.

> Observe the request; the state value is echoed back in the form_post response.

### Step 2: Test for Injection

**Context**: Append HTML to state and check rendering in response.

Modify state to `state=<b>Test Injection</b>` and submit. Inspect the callback response body for unescaped HTML.

> If `<b>Test Injection</b>` renders as bold text in the form, injection is confirmed.

### Step 3: Validate Impact

**Context**: Attempt script injection to assess execution potential.

Set state to `state=<script>alert(1)</script>` and complete flow. Check if alert fires (may be blocked by CSP).

> Success if HTML renders; note CSP mitigations for full XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[oidc]]
- [[injection]]
