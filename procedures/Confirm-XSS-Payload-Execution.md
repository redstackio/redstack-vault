---
id: proc-confirm-xss-execution
tags:
  - xss
  - execution
  - javascript
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
updated_at: '2025-12-14T00:11:16.013Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Confirm XSS Payload Execution

## Summary

This procedure verifies that the reflected XSS payload executes JavaScript in the browser, confirming the vulnerability's exploitability.

## Description

Load the crafted URL in a browser to observe script execution, such as an alert displaying document.cookie. This demonstrates the attack's impact, like session hijacking, in the victim's context on the Glassdoor page. No special tools beyond a browser are needed, with outcomes including visible execution effects.

## Requirements

1. Confirmed reflection from prior test
2. Modern web browser
3. Malicious URL ready

## Defense

Defensive measures and detection strategies:

- Deploy strict CSP headers blocking inline scripts
- Use HttpOnly and Secure flags on cookies
- Implement client-side validation and server-side escaping

## Objectives

1. Execute the payload in browser context
2. Observe JavaScript effects (e.g., alerts, data access)
3. Validate impact like data theft potential

## Instructions

### Step 1: Load Malicious URL

**Context**: Visit the endpoint with the payload in a browser.

Navigate to: https://help.glassdoor.com/gd_requestsubmitpage?lang=<script>alert(document.cookie)</script>

> An alert should pop up showing cookies if executed.

### Step 2: Inspect Browser Console

**Context**: Check dev tools for execution traces.

Open browser console (F12) and reload the page.

> Look for errors or successful script runs.

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
- [[JavaScript]]
