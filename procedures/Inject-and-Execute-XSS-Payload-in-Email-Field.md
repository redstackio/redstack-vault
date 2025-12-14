---
tags:
  - xss-injection
  - javascript-execution
  - payload-delivery
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
updated_at: '2025-12-14T03:15:53.200Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 05c14325-5dc7-4e9c-b556-9d6c3644497d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Execute-XSS-Payload-in-Email-Field

## Summary

This core procedure involves injecting a JavaScript payload into the vulnerable email field on the RelateIQ error page and submitting it to execute arbitrary code, exploiting the reflected XSS flaw for browser-based attacks like alerts or data theft.

## Description

Once the error page is triggered, the email field allows injection of HTML/JS due to poor sanitization. The payload closes the input tag and inserts an onload error handler to run JavaScript. Submission causes reflection and execution in the current browser context, affecting the victim's session on app.relateiq.com. This can lead to stealing cookies, session tokens, or redirecting to phishing sites.

## Requirements

1. Error page loaded with reflected fields from previous step
2. Basic knowledge of XSS payloads (e.g., img onerror)
3. Target browser supporting JavaScript

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) to all reflected inputs
- Implement Web Application Firewall (WAF) rules to block common XSS patterns
- Monitor for JavaScript errors or unexpected alerts in client-side logs

## Objectives

1. Deliver and execute malicious JavaScript in the victim's browser
2. Demonstrate impact through domain alert or further exploitation
3. Validate the vulnerability for reporting or remediation

## Instructions

### Step 1: Craft and Inject Payload

**Context**: Modify the email input to include a breaking payload that injects executable script.

In the email field, enter: `dada@c.com"><img src=x onerror=alert(document.domain)>`. In 'Override Endpoint Address', enter `google.com`.

> Payload is placed to break out of the attribute context. Expected output: Form accepts the input.

### Step 2: Submit and Execute

**Context**: Trigger the reflection by resubmitting the form.

Click 'Connect email' to process.

> The error handler fires on submission. Expected output: Alert box shows 'app.relateiq.com', confirming execution.

### Step 3: Verify Impact

**Context**: Assess the execution for potential escalations.

Inspect browser console or network tab for any additional effects.

> Success if JS runs; extend payload for real attacks like document.cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-injection
- javascript-execution
- payload-delivery
