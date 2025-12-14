---
id: proc-uuid-003
name: Trigger-XSS-by-Clicking-Element
tags:
  - xss
  - click-trigger
type: procedure
tools:
  - '[[tools/Local-Web-Server]]'
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
updated_at: '2025-12-13T23:52:33.465Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Clicking-Element

## Summary

This procedure triggers the XSS payload execution by interacting with a clickable element in the POC, causing the injected JavaScript to run on the www.shopify.com domain.

## Description

Upon clicking the element (e.g., button), the POC sends a request to Shopify with the unsanitized parameter, reflecting the JavaScript back into the victim's browser context. This one-click mechanism bypasses some defenses. Applicable in phishing scenarios. Expected: Payload execution in Shopify's origin.

## Requirements

1. Loaded POC page with malicious parameter
2. User interaction capability (click)
3. Vulnerable reflection endpoint on target

## Defense

Defensive measures and detection strategies:

- Escape user inputs in reflected contexts
- Implement clickjacking protection (X-Frame-Options)
- Monitor for cross-origin requests with suspicious payloads

## Objectives

1. Execute arbitrary JavaScript via one-click
2. Gain control in the target's domain context
3. Enable follow-on impacts like data exfiltration

## Instructions

### Step 1: Identify Clickable Element

**Context**: Locate the button or link in the POC designed to trigger the request.

Inspect the poc.html for the onclick handler or similar event.

> Ensure the element is visible and interactive on the loaded page.

### Step 2: Perform the Click

**Context**: Simulate victim interaction to fire the payload.

Click the element in the browser.

> Watch the developer console for any immediate errors. The request should hit Shopify with the injected parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Local-Web-Server]]

## Tags

- [[xss]]
- [[click-trigger]]
