---
tags:
  - xss
  - payload-trigger
  - browser
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c7fe71d7-d491-40ea-8928-b504e27688f1
created_at: '2025-12-13T23:52:49.655Z'
updated_at: '2025-12-13T23:52:49.655Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-via-Page-Reload

## Summary

This procedure triggers the reflected XSS payload in the Shopify admin by reloading the page after navigating to the malicious URL, causing the browser to execute the injected javascript: URI.

## Description

Once the malicious URL is loaded, the javascript: payload in return_url is reflected but not immediately executed. Reloading the page forces the browser to re-process the URI scheme, executing the JavaScript in the admin context. This exploits the improper handling of URI redirections during authentication.

## Requirements

1. Browser session on the crafted malicious URL
2. Ability to perform page reload actions
3. Target page in a state where admin authentication can be simulated

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected parameters to strip URI schemes
- Implement nonce-based script validation
- Log and alert on reloads with suspicious query parameters

## Objectives

1. Force execution of the injected JavaScript
2. Confirm payload activation in the DOM
3. Set up for impact assessment

## Instructions

### Step 1: Prepare Browser

**Context**: Ensure the malicious URL is loaded and inspect the page source to verify reflection.

Open browser developer tools (F12) and check for the return_url in the HTML.

> Reflection visible in source, e.g., href="javascript:alert(100)//".

### Step 2: Execute Reload

**Context**: Trigger the payload by reloading the page.

Press Ctrl+R (or Cmd+R on Mac) or click the browser reload button.

> The javascript: URI executes as the page reloads, running the alert.

### Step 3: Monitor Execution

**Context**: Watch for immediate JS execution indicators.

Observe the alert popup during reload.

> Successful trigger shows the alert without page errors.

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
- [[reload-trigger]]
- [[JavaScript]]
