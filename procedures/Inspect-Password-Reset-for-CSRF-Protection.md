---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 43cf5511-abe0-4863-a7b7-bd00dadf6d7e
created_at: '2025-12-14T17:27:23.441Z'
updated_at: '2025-12-14T17:27:23.441Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Password-Reset-for-CSRF-Protection

## Summary

This procedure involves examining the password reset functionality of a web application like RelateIQ to detect the absence of CSRF tokens, enabling the identification of a vulnerability that allows forged requests.

## Description

In web applications, CSRF vulnerabilities occur when state-changing actions, such as password resets, lack proper token validation to ensure requests originate from the legitimate site. This procedure targets the password reset flow by inspecting links, forms, and API endpoints for missing anti-CSRF measures. In the RelateIQ case, the reset request does not include or validate tokens, allowing cross-origin forgery. Prerequisites include access to the application's password reset page and a modern web browser. Expected outcomes are documentation of the vulnerable endpoint and confirmation of exploitability, setting the stage for demonstration via POC.

## Requirements

1. Web browser with developer tools (e.g., Chrome or Firefox)
2. Access to the target web application (RelateIQ domain)
3. Basic knowledge of HTTP requests and form submissions

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms and validate them server-side
- Enforce same-origin policy checks via CORS headers
- Monitor for anomalous password reset requests from unexpected referrers

## Objectives

1. Confirm the lack of CSRF protection in the password reset endpoint
2. Document the request structure for exploitation
3. Assess the potential for unauthorized password changes

## Instructions

### Step 1: Navigate to Password Reset

**Context**: Access the password reset feature to initiate the flow and prepare for inspection.

Open the RelateIQ login page and click the "Forgot Password" link. Enter a test email address to generate the reset link, then follow it to the reset form.

> This simulates user interaction and exposes the relevant endpoints.

### Step 2: Inspect Network Requests

**Context**: Use browser tools to analyze the HTTP requests during form submission.

In the browser's developer tools, go to the Network tab. Submit the password reset form and filter for POST requests to endpoints like `/api/reset-password` or similar. Examine the request headers, body, and response for any CSRF-related fields (e.g., `_token`, `X-CSRF-Token`).

> Expected output: No CSRF token present, confirming vulnerability. Note the endpoint URL, method (POST), and parameters (e.g., email, reset_token).

### Step 3: Verify Cross-Origin Behavior

**Context**: Test if the endpoint accepts requests from external origins.

Use the console to craft a simple XMLHttpRequest or fetch to the endpoint from a different origin (e.g., a local HTML file). Check if the request succeeds without token validation.

> Expected output: Successful response indicating lack of origin checks.

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
- [[web]]
- [[recon]]
