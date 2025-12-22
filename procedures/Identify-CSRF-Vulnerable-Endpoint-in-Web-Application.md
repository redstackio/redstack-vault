---
tags:
  - csrf
  - discovery
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.995Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2d5bf768-52a4-4bb4-a245-f083e4aa2706
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CSRF-Vulnerable-Endpoint-in-Web-Application

## Summary

This procedure involves testing web endpoints to detect Cross-Site Request Forgery (CSRF) vulnerabilities by checking for the absence of protection mechanisms like tokens or origin validation, as demonstrated in the Rockstar Games Red Dead Online feedback endpoint.

## Description

In a typical attack scenario, the tester inspects a web application's feedback or form submission endpoints to determine if they enforce CSRF protections. The target environment is a web application where users are authenticated, and the endpoint processes state-changing requests (e.g., POST to submit.json). Expected outcomes include confirmation of vulnerability if requests from untrusted origins succeed without tokens. Prerequisites include access to the application and a browser for testing.

## Requirements

1. Access to the target web application with an authenticated session.
2. Browser developer tools for inspecting requests.
3. Knowledge of the endpoint URL (e.g., https://www.rockstargames.com/reddeadonline/feedback/submit.json).

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all forms and validate them server-side.
- Enforce same-origin policy checks via headers like Origin and Referer.
- Monitor for anomalous submission patterns from unexpected sources.

## Objectives

1. Confirm lack of CSRF protection on the endpoint.
2. Document the vulnerable URL and request format.
3. Assess exploitability for unauthorized actions.

## Instructions

### Step 1: Inspect Legitimate Request

**Context**: Submit legitimate feedback to capture the request structure and check for CSRF tokens.

Open the feedback form on the target site, submit a test entry, and use browser dev tools (Network tab) to examine the POST request to the endpoint.

> Look for anti-CSRF tokens in headers, cookies, or form fields. If absent, note the request payload (e.g., JSON with feedback data).

### Step 2: Test Cross-Origin Request

**Context**: Simulate a forged request from a different origin to verify vulnerability.

Create a simple HTML page on a local server with a form targeting the endpoint, or use curl to test (though browser context is needed for session cookies).

> If the request succeeds without token validation, the endpoint is vulnerable. Expected output: 200 OK response with submission confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]
