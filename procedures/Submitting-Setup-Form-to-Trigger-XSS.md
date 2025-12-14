---
tags:
  - xss
  - submission
  - trigger
  - execution
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
updated_at: '2025-12-14T03:15:26.427Z'
sub_techniques: []
id: a7648b7e-887d-4736-8414-e77cccd9e3c1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submitting Setup Form to Trigger XSS

## Summary

This procedure covers submitting the Nextcloud setup form after payload injection, causing the server to reflect the unsanitized input and execute the JavaScript in the user's browser.

## Description

Upon form submission, the Nextcloud server processes the input and includes the 'mysql Username' value directly in the HTML response without escaping, leading to immediate script execution. This demonstrates the reflected XSS flaw but is confined to self-execution during setup, posing low risk.

## Requirements

1. Completed form with injected payload from prior procedure
2. Browser session active on the setup page
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs using libraries like htmlspecialchars in PHP
- Disable or restrict setup access in production environments
- Monitor browser console and network responses for unauthorized script execution

## Objectives

1. Trigger payload reflection via form POST
2. Observe JavaScript execution
3. Confirm vulnerability impact

## Instructions

### Step 1: Submit the Form

**Context**: Initiate the server-side processing to reflect the payload.

Click the 'Finish setup' button or equivalent submit control on the form.

> The page will process and reload, embedding the payload in the response.

### Step 2: Validate Execution

**Context**: Check for successful JS invocation.

Observe the alert(1) dialog popping up in the browser.

> If the alert appears, the XSS is confirmed. Use browser dev tools to inspect the response HTML for the unescaped `<script>` tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- submission
- trigger
- execution
