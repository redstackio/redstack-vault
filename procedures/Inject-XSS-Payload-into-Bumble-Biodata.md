---
tags:
  - xss
  - injection
  - payload-testing
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
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6541eefe-7d3a-4ed7-b266-ea1dbde1b041
created_at: '2025-12-14T03:15:10.393Z'
updated_at: '2025-12-14T03:15:10.393Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Bumble-Biodata

## Summary

This procedure demonstrates injecting a JavaScript payload into the biodata field of a Bumble user profile, exploiting lack of input sanitization to store malicious code server-side for later execution.

## Description

In the context of the Bumble web application, the biodata field accepts user input without proper escaping or validation, allowing stored XSS. The attacker edits their profile, inserts a payload like `<script>alert('XSS');</script>`, and submits. Initial attempts may cause errors (e.g., post-OK button), but successful injection stores the code, setting up execution on profile views. This targets web browsers rendering the profile HTML.

## Requirements

1. Active Bumble account with profile editing permissions
2. Web browser access to Bumble's profile management interface
3. Basic knowledge of JavaScript payloads for XSS testing

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization using libraries like DOMPurify or OWASP ESAPI
- Apply Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous profile content via WAF rules detecting script tags

## Objectives

1. Store unsanitized JavaScript in the biodata field
2. Bypass any client-side validation errors
3. Prepare for payload reflection in viewer contexts

## Instructions

### Step 1: Access Profile Editor

**Context**: Log in and navigate to the editable biodata section to prepare for injection.

Log in to Bumble via web browser and go to account settings > profile edit. Locate the biodata input field.

### Step 2: Craft and Inject Payload

**Context**: Insert a test payload to verify storage without immediate execution.

Enter the payload `<script>alert('XSS Test');</script>` into the biodata field. Press save or OK. If an error occurs (e.g., validation fail), refine by encoding or shortening, e.g., `<svg onload=alert('XSS')>`. Submit again.

> On success, the profile updates without rejection, storing the payload. Use browser dev tools to inspect the submission request for confirmation.

### Step 3: Verify Storage

**Context**: Confirm the payload is persisted server-side.

Edit the profile again to view the biodata content; the injected script should remain unsanitized.

> Expected: Raw script tag visible in the input, indicating no stripping occurred.

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
- [[injection]]
