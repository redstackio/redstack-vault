---
tags:
  - xss-injection
  - payload-testing
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
updated_at: '2025-12-13T23:52:49.879Z'
sub_techniques: []
id: e63cc0a0-3f1a-4eb3-a128-8354e5964d19
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Messages Input

## Summary

This procedure tests for reflected XSS by injecting a malicious JavaScript payload into the Messages input field, which gets echoed back unsanitized.

## Description

The Messages section accepts user input that is reflected in the response without HTML escaping or validation. Payloads like `<h1 onauxclick=confirm(document.domain)>RIGHT CLICK HERE</h1>` or `<img src=x onerror=alert('XSS')>` are entered and submitted. In a web browser context, this step confirms the root cause: lack of sanitization. Prerequisites include access to the Messages page; outcomes show the payload in the page content.

## Requirements

1. Access to the Messages input field
2. Knowledge of XSS payloads
3. Browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Implement input sanitization using libraries like DOMPurify
- Validate and escape all user inputs before rendering
- Deploy Content Security Policy (CSP) to block inline scripts

## Objectives

1. Introduce unsanitized JavaScript into the input
2. Observe reflection in the page output
3. Verify vulnerability to XSS

## Instructions

### Step 1: Enter and Submit Payload

**Context**: Type the payload into the input field and submit to trigger reflection.

No specific command; manual input.

> In the Messages input field, enter: `<h1 onauxclick=confirm(document.domain)>RIGHT CLICK HERE</h1>`. Alternative payloads: `<img src=x onerror=prompt('XSS')>` or `"><img/src="x"/onerror=prompt(1)>`. Submit the form. Inspect the page to see the payload reflected.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-testing]]
