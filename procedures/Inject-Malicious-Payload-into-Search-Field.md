---
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2025-12-14T03:15:30.642Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:30.642Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8e55d7cb-2ed6-4331-9b94-494125edaccb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject Malicious Payload into Search Field

## Summary

This procedure details the manual injection of a malicious JavaScript payload into the search input field of the Kartpay settlements page to test for reflected XSS.

## Description

Reflected XSS occurs when user-supplied input is immediately rendered back in the browser without escaping, allowing attackers to inject HTML or JavaScript. Here, the search parameter on https://merchant.kartpay.com/settlements lacks proper output encoding, enabling the payload '"><img src=x onerror=alert(domain)>' to break out of the input context and execute code. This step assumes the page is loaded and focuses on crafting and entering the payload to exploit the insufficient input validation. Prerequisites include browser access, and outcomes involve the payload being accepted, leading to potential code execution upon submission.

## Requirements

1. Access to the loaded settlements page
2. Knowledge of basic XSS payloads
3. Web browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and sanitization on all user inputs
- Apply content security policy (CSP) headers to restrict script execution
- Monitor for unusual input patterns in application logs

## Objectives

1. Deliver unsanitized JavaScript code via the search parameter
2. Break out of the HTML context to enable execution
3. Set up for reflection and arbitrary code injection

## Instructions

### Step 1: Locate Search Input Field

**Context**: Identify the vulnerable search box on the page.

Focus on the search input element, typically labeled for filtering settlements.

> The field should accept text input without restrictions.

### Step 2: Enter the Payload

**Context**: Craft and input the XSS payload to test reflection.

Type the following payload into the search field: '"><img src=x onerror=alert(domain)>'

> This payload closes any open HTML attributes or tags and injects an image element that triggers an alert on error, displaying the domain to confirm execution context.

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
- [[payload-injection]]
