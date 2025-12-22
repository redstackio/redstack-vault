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
verified: false
platforms:
  - Web
submitted: true
created_at: '2022-04-05'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:50.414Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0247289c-ff19-40a6-9a1f-bad5e01c9efe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Vulnerable-Endpoint

## Summary

This procedure involves inspecting web application endpoints to identify those vulnerable to Cross-Site Request Forgery (CSRF) attacks, specifically targeting state-changing actions like email updates without proper token validation.

## Description

In the context of the TikTok Ads platform, this procedure focuses on the endpoint for changing user verification emails. By simulating legitimate actions and monitoring network traffic, attackers can confirm the absence of CSRF protections, such as synchronizer tokens or same-site cookies. This reconnaissance step is crucial for crafting effective exploits and is typically performed in a controlled testing environment or against public-facing web apps.

## Requirements

1. Access to a web browser with developer tools (e.g., Chrome DevTools)
2. Valid user account on the target platform (for testing)
3. Knowledge of the application's functionality (e.g., email change feature)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Use SameSite=Strict cookies to prevent cross-site requests
- Monitor for anomalous POST requests from unexpected referers

## Objectives

1. Locate the exact URL and parameters of the vulnerable endpoint
2. Verify lack of CSRF protection by testing requests
3. Document payload structure for exploitation

## Instructions

### Step 1: Simulate Legitimate Action

**Context**: Log in to the TikTok Ads account and navigate to the verification email change section to trigger the real request.

Open browser developer tools (F12), go to the Network tab, and submit a legitimate email change. Inspect the POST request for tokens or headers.

**Expected Output**: POST request details, e.g., URL: `https://ads.tiktok.com/account/verification/email/update`, body: `new_email=example@test.com`.

### Step 2: Test for CSRF Protection

**Context**: Attempt to replay the request without tokens to confirm vulnerability.

Use the browser console or a tool like Postman to send the POST request with session cookies but no CSRF token. If it succeeds, the endpoint is vulnerable.

**Expected Output**: Successful email update without additional validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
