---
tags:
  - xss
  - payload-injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.146Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 61491a23-edd6-48c0-8d97-2326fec1458f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Advanced-File-Search-Filter

## Summary

This procedure exploits the lack of input sanitization in Concrete CMS 8.5.2's advanced file search filter by injecting a stored XSS payload, which is saved and later rendered unsafely.

## Description

As an authenticated administrator, access the advanced search window in the file search interface. The phrase field allows arbitrary input without proper escaping, enabling storage of JavaScript code. Use a simple payload like an image tag with an onerror handler to test execution. This stored payload will execute in the context of any user's browser when they interact with the saved filter, potentially leading to session theft or other client-side attacks. Prerequisites include admin access from the setup procedure.

## Requirements

1. Administrative access to Concrete CMS dashboard
2. Access to Dashboard > Files > Search
3. Web browser to input and save the payload
4. Knowledge of basic JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in search filters using HTML entity encoding
- Implement content security policy (CSP) to restrict inline scripts
- Monitor for anomalous JavaScript execution in browser logs
- Audit saved search filters for malicious content

## Objectives

1. Inject unsanitized JavaScript into the filter phrase field
2. Save the filter to store the payload persistently
3. Verify storage without immediate execution

## Instructions

### Step 1: Access Advanced Search

**Context**: Open the interface for injecting the payload.

In the file search bar, click the 'Advanced' button to launch the filter window.

> The advanced window loads with fields including the phrase input.

### Step 2: Enter Malicious Payload

**Context**: Craft and input the XSS payload to bypass sanitization.

In the phrase field, enter or append: <img src=1 onerror=alert(1)> (replace with more malicious code for real attacks, e.g., to exfiltrate cookies).

> The field accepts the input without validation errors.

### Step 3: Save the Filter

**Context**: Persist the payload for later execution.

Click the 'Save' button to store the advanced filter.

> Filter saves successfully, confirming storage of the payload.

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
- [[stored-xss]]
