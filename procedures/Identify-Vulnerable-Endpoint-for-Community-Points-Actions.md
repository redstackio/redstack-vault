---
id: p-concrete-identify-endpoint
tags:
  - csrf
  - recon
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:03.717Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Endpoint for Community Points Actions

## Summary

This procedure involves inspecting the Concrete CMS dashboard to identify the POST endpoint for saving community points actions, confirming the absence of CSRF protection and input sanitization on key parameters like upaName and upaHandle.

## Description

In Concrete CMS, the community points feature allows admins to create actions that award points to users. The save endpoint at `/index.php/dashboard/users/points/actions/save` processes POST requests without validating CSRF tokens or sanitizing inputs, making it vulnerable to unauthorized submissions and XSS injection. This step is reconnaissance to map the attack surface before crafting exploits. Prerequisites include access to a Concrete CMS instance and basic web inspection skills. Expected outcome: Detailed endpoint parameters and vulnerability confirmation.

## Requirements

1. Access to a running Concrete CMS instance (version 5.7.x or similar)
2. Logged-in administrator session for inspection (non-destructive)
3. Browser with developer tools (e.g., Chrome DevTools)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing forms
- Enable web application firewall (WAF) rules to detect anomalous POSTs to admin endpoints
- Log and monitor access to dashboard endpoints for unusual patterns

## Objectives

1. Confirm the vulnerable POST endpoint and its parameters
2. Verify lack of CSRF protection and sanitization
3. Gather details for payload crafting

## Instructions

### Step 1: Access the Community Points Dashboard

**Context**: Navigate to the admin section to locate the actions management page.

Log in as an administrator and go to Dashboard > Users > Points > Actions. Attempt to create a test action to observe the form.

### Step 2: Inspect Network Traffic

**Context**: Use browser tools to capture the form submission and analyze the endpoint.

Open developer tools (F12), go to the Network tab, and submit a test action form. Look for the POST request to `/index.php/dashboard/users/points/actions/save`. Note parameters: upaID, upaIsActive, upaHandle, upaName, upaDefaultPoints, gBadgeID. Confirm no CSRF token in headers or body.

### Step 3: Test Input Sanitization

**Context**: Probe for XSS by submitting special characters.

Submit a test form with `<script>alert(1)</script>` in upaName. If it saves without escaping, sanitization is absent. Check the saved action for raw output.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning (endpoint reconnaissance)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- recon
- web-vuln
