---
tags:
  - xss
  - stored-xss
  - javascript-execution
  - apache-airflow
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6b13d8fa-0f65-4c08-8782-2f27248493a1
created_at: '2025-12-13T23:52:55.731Z'
updated_at: '2025-12-13T23:52:55.731Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-Provider-Documentation-Link

## Summary

This procedure details clicking the malicious documentation link in the Apache Airflow providers UI to execute the stored XSS payload, resulting in arbitrary JavaScript running in the authenticated user's browser context.

## Description

The stored XSS is triggered when the browser processes the unsanitized javascript: URL from the provider metadata. The payload executes client-side, potentially accessing DOM elements, cookies, or local storage for theft or manipulation. This requires user interaction but leverages the trust in the Airflow UI. Expected outcomes: Immediate JS execution, such as alerts or data exfiltration to an attacker server, enabling session hijacking or further attacks.

## Requirements

1. Active authenticated session in Airflow web UI
2. Visibility of the malicious provider in the providers section
3. Browser without strict JS blocking (e.g., no NoScript extension)

## Defense

Defensive measures and detection strategies:

- Sanitize all provider metadata on display (fixed in Airflow 2.10.0)
- Implement browser-based protections like disabling javascript: URIs via extensions or policies
- Monitor for unexpected network requests from the UI (e.g., to external domains)
- Educate users on avoiding clicks in admin interfaces and enable UI logging for click events

## Objectives

1. Initiate payload execution via link click
2. Achieve JavaScript control in the victim browser
3. Exfiltrate sensitive data like session tokens

## Instructions

### Step 1: Locate the Link

**Context**: Identify the documentation link for the malicious provider.

In the providers table, find the row for the custom provider and focus on the 'Documentation' column.

> The link text may appear normal, but inspection reveals the javascript: scheme.

### Step 2: Click to Trigger

**Context**: Execute the payload by interacting with the link.

Click the documentation link directly.

> Browser executes the JS immediately; for POC, use `javascript:alert('XSS')`; for real attacks, include fetch to exfiltrate `document.cookie`.

### Step 3: Validate Execution

**Context**: Confirm the XSS fired and assess impact.

Observe effects like pop-ups or check browser dev tools for executed scripts/network requests.

> Success: Payload runs, e.g., data sent to attacker server; failure if CSP blocks it.

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
- [[stored-xss]]
- [[javascript-execution]]
